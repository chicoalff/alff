import os
import re
import requests
import json
import google.generativeai as genai

# --- Configuração de variáveis de ambiente e API Gemini ---
GOOGLE_API_KEY = os.environ.get('AIzaSyAx6NUQweIl3Zj-a9gxZkKIhpqYLPOxbcA')
if not GOOGLE_API_KEY:
    print("ERRO: variável de ambiente GOOGLE_API_KEY não configurada.")
    exit()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

# --- URLs dos prompts (github raw) ---
PROMPT_COLETA    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F1.md"
PROMPT_SEMANTICA = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F2.md"
PROMPT_TITULO    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F3.md"
PROMPT_TOC       = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F4.md"
PROMPT_BLOCOS    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F6.md"
PROMPT_REVISAO   = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F7.md"
PROMPT_CHECKLIST = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F8.md"

# --- URL do agent.md e do config.json (itumb repo) ---
AGENT_INFO_URL    = "https://github.com/chicoalff/itumb/raw/master/agent.md"
ARTIGO_CONFIG_URL = "https://github.com/chicoalff/itumb/raw/master/article_config.json"

# --- Utilitários ---
def carregar_url(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text.strip()
    print(f"ERRO ao baixar: {url}")
    exit()

def carregar_json_url(url: str) -> dict:
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    print(f"ERRO ao baixar arquivo JSON: {url}")
    exit()

def gerar_conteudo_gemini(prompt: str, temperatura: float=0.7, max_tokens: int=2048) -> str:
    try:
        resp = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperatura,
                max_output_tokens=max_tokens
            )
        )
        return resp.text or ""
    except Exception as e:
        print(f"Erro Gemini: {e}")
        return ""

def obter_input_usuario(rotulo: str) -> str:
    return input(f"{rotulo}: ").strip()

def obter_aprovacao_usuario(pergunta: str) -> bool:
    while True:
        r = input(f"{pergunta} (s/n): ").strip().lower()
        if r in ('s','sim'): return True
        if r in ('n','nao','não'): return False

# --- Inicialização de contexto e parâmetros ---
def carregar_contexto_agente():
    print("\n--- Carregando informações do agente ---")
    agente_contexto = carregar_url(AGENT_INFO_URL)
    print(agente_contexto)
    return agente_contexto

def carregar_configuracao_artigo():
    print("\n--- Carregando configurações do artigo (JSON) ---")
    return carregar_json_url(ARTIGO_CONFIG_URL)

# --- Fases do fluxo ---
def coleta_dados_usuario(agent_contexto: str, artigo_conf: dict) -> dict:
    prompt = carregar_url(PROMPT_COLETA)
    print(f"\n[AGENTE]\n{agent_contexto}\n")
    print(f"[CONFIG ARTIGO]\n{json.dumps(artigo_conf, indent=2, ensure_ascii=False)}\n")
    print(f"[PROMPT COLETA]\n{prompt}\n")
    tema = obter_input_usuario("Tema principal do artigo")
    diretrizes = obter_input_usuario("Diretrizes (opcional)")
    return {"tema": tema, "diretrizes": diretrizes}

def busca_e_extracao_palavras_chave(tema: str, diretrizes: str, artigo_conf: dict) -> dict:
    prompt = carregar_url(PROMPT_SEMANTICA).format(tema=tema, diretrizes=diretrizes)
    print(f"[PROMPT SEMANTICA]\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.6, max_tokens=2500)
    top = re.findall(r'\d+\.\s*\*\*(.+?)\*\*', out)[:5]
    print(f"[RESPOSTA BUSCA PALAVRAS-CHAVE]\n{out}\n")
    return {"raw_output": out, "top_palavras_chave": top}

def sugerir_e_aprovar_titulo(tema: str, diretrizes: str, dados_pesquisa: dict, artigo_conf: dict) -> tuple:
    prompt_tpl = carregar_url(PROMPT_TITULO)
    while True:
        prompt = prompt_tpl.format(
            tema=tema,
            diretrizes=diretrizes,
            raw_output=dados_pesquisa['raw_output'],
            **artigo_conf["H1"]
        )
        print(f"[PROMPT TÍTULO]\n{prompt}\n")
        out = gerar_conteudo_gemini(prompt, temperatura=0.8)
        t = re.search(r'Título:\s*(.+)', out)
        s = re.search(r'Subtítulo:\s*(.+)', out)
        o = re.search(r'Outline:\s*\n(.+)', out, re.DOTALL)
        titulo = t.group(1).strip() if t else ""
        subtitulo = "" if not s or "Nenhum" in s.group(1) else s.group(1).strip()
        outline = o.group(1).strip() if o else ""
        print(f"[RESPOSTA TÍTULO]\n{out}\n")
        if obter_aprovacao_usuario("Aprova título e outline inicial?"):
            return titulo, subtitulo, outline

def sugerir_e_aprovar_toc(titulo: str, subtitulo: str, outline: str, dados_pesquisa: dict, artigo_conf: dict) -> tuple:
    prompt_tpl = carregar_url(PROMPT_TOC)
    prompt = prompt_tpl.format(
        titulo=titulo,
        subtitulo=subtitulo or 'Nenhum',
        outline=outline,
        raw_output=dados_pesquisa['raw_output'],
        **artigo_conf["H2"],
        **artigo_conf["H3"]
    )
    print(f"[PROMPT TOC]\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.8, max_tokens=3000)
    print(f"[RESPOSTA TOC]\n{out}\n")
    secoes = []
    current = None
    for line in out.splitlines():
        if line.startswith('## '):
            current = {"level":2, "title": line[3:].strip(), "intro":"", "subsections":[]}
            secoes.append(current)
        elif line.startswith('### ') and current:
            sec = {"level":3, "title": line[4:].strip(), "intro":""}
            current["subsections"].append(sec)
        elif current and not line.startswith('#'):
            if current["subsections"]:
                current["subsections"][-1]["intro"] += line + " "
            else:
                current["intro"] += line + " "
    if obter_aprovacao_usuario("Aprova TOC?"):
        return out, secoes

def construir_artigo_em_blocos(titulo: str, subtitulo: str, toc: list, dados_pesquisa: dict, artigo_conf: dict) -> str:
    tpl_h2 = carregar_url(PROMPT_BLOCOS)
    tpl_h3 = carregar_url(PROMPT_BLOCOS)
    tpl_final = carregar_url(PROMPT_REVISAO)
    markdown = [f"# {titulo}", subtitulo, ""]
    for sec in toc:
        if sec["level"] == 2:
            markdown.append(f"## {sec['title']}\n{sec['intro'].strip()}\n")
            prompt = tpl_h2.format(
                titulo=titulo, subtitulo=subtitulo or 'Nenhum',
                raw_output=dados_pesquisa['raw_output'],
                h2_title=sec['title'], h2_intro=sec['intro'].strip(),
                **artigo_conf['Paragrafos']
            )
            print(f"[PROMPT BLOCO H2]\n{prompt}\n")
            out = gerar_conteudo_gemini(prompt, temperatura=0.9, max_tokens=1500)
            print(f"[RESPOSTA BLOCO H2]\n{out}\n")
            if obter_aprovacao_usuario(f"Aprova bloco H2 '{sec['title']}'?"):
                markdown.append(out)
            for sub in sec["subsections"]:
                markdown.append(f"### {sub['title']}\n{sub['intro'].strip()}\n")
                prompt = tpl_h3.format(
                    titulo=titulo, subtitulo=subtitulo or 'Nenhum',
                    raw_output=dados_pesquisa['raw_output'],
                    h3_title=sub['title'], h3_intro=sub['intro'].strip(),
                    **artigo_conf['Paragrafos']
                )
                print(f"[PROMPT BLOCO H3]\n{prompt}\n")
                out = gerar_conteudo_gemini(prompt, temperatura=0.9, max_tokens=1000)
                print(f"[RESPOSTA BLOCO H3]\n{out}\n")
                if obter_aprovacao_usuario(f"Aprova bloco H3 '{sub['title']}'?"):
                    markdown.append(out)
    prompt = tpl_final.format(
        titulo=titulo,
        raw_output="\n".join(markdown),
        **artigo_conf['Artigo_Geral'],
        **artigo_conf['Imagens'],
        **artigo_conf['Links']
    )
    print(f"[PROMPT REVISÃO FINAL]\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.7)
    print(f"[RESPOSTA REVISÃO FINAL]\n{out}\n")
    markdown.append(out)
    return "\n".join([m for m in markdown if m])

def main():
    agente_contexto = carregar_contexto_agente()
    artigo_conf = carregar_configuracao_artigo()
    dados = coleta_dados_usuario(agente_contexto, artigo_conf)
    pesquisa = busca_e_extracao_palavras_chave(dados['tema'], dados['diretrizes'], artigo_conf)
    h1, sub, outline = sugerir_e_aprovar_titulo(dados['tema'], dados['diretrizes'], pesquisa, artigo_conf)
    toc_md, toc_struct = sugerir_e_aprovar_toc(h1, sub, outline, pesquisa, artigo_conf)
    artigo = construir_artigo_em_blocos(h1, sub, toc_struct, pesquisa, artigo_conf)
    print("\n\nARTIGO COMPLETO:\n")
    print(artigo)

if __name__ == '__main__':
    main()