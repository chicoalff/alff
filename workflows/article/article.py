import os
import re
import requests
import google.generativeai as genai

# --- Configuração de variáveis de ambiente e API Gemini ---
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    print("ERRO: variável de ambiente GOOGLE_API_KEY não configurada.")
    exit()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

# --- URLs dos prompts diretamente do repositório GitHub (raw) ---
PROMPT_COLETA    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F1.md"
PROMPT_SEMANTICA = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F2.md"
PROMPT_TITULO    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F3.md"
PROMPT_TOC       = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F4.md"
PROMPT_BLOCOS    = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F6.md"
PROMPT_REVISAO   = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F7.md"
PROMPT_CHECKLIST = "https://github.com/chicoalff/alff/raw/master/workflows%2Farticle%2Fcot%2F8.md"

# --- Parâmetros do artigo ---
ARTIGO_PARAMETROS = {
    "H1": {"min_palavras":5,"max_palavras":9,"min_caracteres":45,"max_caracteres":65,"subtitulo_min_palavras":8,"subtitulo_max_palavras":12},
    "H2": {"min_por_artigo":4,"max_por_artigo":7,"titulo_min_palavras":3,"titulo_max_palavras":5,"intro_frases_min":2,"intro_frases_max":3},
    "H3": {"min_por_H2":2,"max_por_H2":4,"titulo_min_palavras":2,"titulo_max_palavras":4,"intro_frases_min":1,"intro_frases_max":2},
    "Paragrafos": {"min_por_H2":3,"max_por_H2":6,"min_palavras":40,"max_palavras":70,"min_frases":2,"max_frases":4},
    "Imagens": {"min_por_artigo":2,"max_por_artigo":4,"legenda_min_palavras":5,"legenda_max_palavras":10,"alt_text_min_palavras":3,"alt_text_max_palavras":8},
    "Links": {"internos_min":3,"internos_max":5,"externos_min":4,"externos_max":8},
    "Artigo_Geral": {"min_palavras":1200,"max_palavras":1800}
}

# --- Utilitários ---
def carregar_prompt(url: str) -> str:
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.text.strip()
    print(f"ERRO ao baixar prompt: {url}")
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

# --- Fases do fluxo ---
def coleta_dados_usuario() -> dict:
    prompt = carregar_prompt(PROMPT_COLETA)
    tema = obter_input_usuario("Tema principal do artigo")
    diretrizes = obter_input_usuario("Diretrizes (opcional)")
    print(f"\nPrompt de coleta utilizado:\n{prompt}\n")
    return {"tema": tema, "diretrizes": diretrizes}

def busca_e_extracao_palavras_chave(tema: str, diretrizes: str) -> dict:
    prompt = carregar_prompt(PROMPT_SEMANTICA).format(tema=tema, diretrizes=diretrizes)
    print(f"\nPrompt semântica utilizado:\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.6, max_tokens=2500)
    top = re.findall(r'\d+\.\s*\*\*(.+?)\*\*', out)[:5]
    print(f"\nResposta da busca e extração:\n{out}\n")
    return {"raw_output": out, "top_palavras_chave": top}

def sugerir_e_aprovar_titulo(tema: str, diretrizes: str, dados_pesquisa: dict) -> tuple:
    prompt_tpl = carregar_prompt(PROMPT_TITULO)
    while True:
        prompt = prompt_tpl.format(
            tema=tema,
            diretrizes=diretrizes,
            raw_output=dados_pesquisa['raw_output'],
            **ARTIGO_PARAMETROS['H1']
        )
        print(f"\nPrompt título utilizado:\n{prompt}\n")
        out = gerar_conteudo_gemini(prompt, temperatura=0.8)
        t = re.search(r'Título:\s*(.+)', out)
        s = re.search(r'Subtítulo:\s*(.+)', out)
        o = re.search(r'Outline:\s*\n(.+)', out, re.DOTALL)
        titulo = t.group(1).strip() if t else ""
        subtitulo = "" if not s or "Nenhum" in s.group(1) else s.group(1).strip()
        outline = o.group(1).strip() if o else ""
        print(f"\nResposta do título:\n{out}\n")
        if obter_aprovacao_usuario("Aprova título e outline inicial?"):
            return titulo, subtitulo, outline

def sugerir_e_aprovar_toc(titulo: str, subtitulo: str, outline: str, dados_pesquisa: dict) -> tuple:
    prompt_tpl = carregar_prompt(PROMPT_TOC)
    prompt = prompt_tpl.format(
        titulo=titulo,
        subtitulo=subtitulo or 'Nenhum',
        outline=outline,
        raw_output=dados_pesquisa['raw_output'],
        **ARTIGO_PARAMETROS['H2'],
        **ARTIGO_PARAMETROS['H3']
    )
    print(f"\nPrompt TOC utilizado:\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.8, max_tokens=3000)
    print(f"\nResposta da TOC:\n{out}\n")
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

def construir_artigo_em_blocos(titulo: str, subtitulo: str, toc: list, dados_pesquisa: dict) -> str:
    tpl_h2 = carregar_prompt(PROMPT_BLOCOS)
    tpl_h3 = carregar_prompt(PROMPT_BLOCOS)  # use outro prompt caso queira H3 separado
    tpl_final = carregar_prompt(PROMPT_REVISAO)
    markdown = [f"# {titulo}", subtitulo, ""]
    for sec in toc:
        if sec["level"] == 2:
            markdown.append(f"## {sec['title']}\n{sec['intro'].strip()}\n")
            prompt = tpl_h2.format(
                titulo=titulo, subtitulo=subtitulo or 'Nenhum',
                raw_output=dados_pesquisa['raw_output'],
                h2_title=sec['title'], h2_intro=sec['intro'].strip(),
                **ARTIGO_PARAMETROS['Paragrafos']
            )
            print(f"\nPrompt bloco H2 utilizado:\n{prompt}\n")
            out = gerar_conteudo_gemini(prompt, temperatura=0.9, max_tokens=1500)
            print(f"\nResposta bloco H2:\n{out}\n")
            if obter_aprovacao_usuario(f"Aprova bloco H2 '{sec['title']}'?"):
                markdown.append(out)
            for sub in sec["subsections"]:
                markdown.append(f"### {sub['title']}\n{sub['intro'].strip()}\n")
                prompt = tpl_h3.format(
                    titulo=titulo, subtitulo=subtitulo or 'Nenhum',
                    raw_output=dados_pesquisa['raw_output'],
                    h3_title=sub['title'], h3_intro=sub['intro'].strip(),
                    **ARTIGO_PARAMETROS['Paragrafos']
                )
                print(f"\nPrompt bloco H3 utilizado:\n{prompt}\n")
                out = gerar_conteudo_gemini(prompt, temperatura=0.9, max_tokens=1000)
                print(f"\nResposta bloco H3:\n{out}\n")
                if obter_aprovacao_usuario(f"Aprova bloco H3 '{sub['title']}'?"):
                    markdown.append(out)
    prompt = tpl_final.format(
        titulo=titulo,
        raw_output="\n".join(markdown),
        **ARTIGO_PARAMETROS['Artigo_Geral'],
        **ARTIGO_PARAMETROS['Imagens'],
        **ARTIGO_PARAMETROS['Links']
    )
    print(f"\nPrompt revisão final utilizado:\n{prompt}\n")
    out = gerar_conteudo_gemini(prompt, temperatura=0.7)
    print(f"\nResposta revisão final:\n{out}\n")
    markdown.append(out)
    return "\n".join([m for m in markdown if m])

def main():
    dados = coleta_dados_usuario()
    pesquisa = busca_e_extracao_palavras_chave(dados['tema'], dados['diretrizes'])
    h1, sub, outline = sugerir_e_aprovar_titulo(dados['tema'], dados['diretrizes'], pesquisa)
    toc_md, toc_struct = sugerir_e_aprovar_toc(h1, sub, outline, pesquisa)
    artigo = construir_artigo_em_blocos(h1, sub, toc_struct, pesquisa)
    print("\n\nARTIGO COMPLETO:\n")
    print(artigo)

if __name__ == '__main__':
    main()