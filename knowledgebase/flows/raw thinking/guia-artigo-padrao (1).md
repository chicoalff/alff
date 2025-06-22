# **Guia para artigos de conteúdo padrão - https://analisederequisitos.com.br/**

## **📌 Visão Geral**  
Este documento consolida as melhores práticas para criação de artigos técnicos, baseado na análise do blog "Análise de Requisitos". Serve como base de conhecimento para um CustomGPT especializado em produção de conteúdo técnico.

---

## **🔧 Estrutura Básica do Artigo**

### **1. Títulos e Hierarquia**  
#### **1.1 Título Principal (H1)**  
- **Formato**: 5-9 palavras (45-65 caracteres)  
- **Subtítulo opcional**: 8-12 palavras  
- **Exemplo**:  
  ```markdown
  # Guia Avançado para Diagramas UML  
  Entenda como modelar sistemas complexos com a linguagem padrão do mercado  
  ```

#### **1.2 Seções (H2)**  
- **Quantidade**: 4-7 por artigo  
- **Formato obrigatório**:  
  ```markdown
  ## [Título H2 com 3-5 palavras]  
  [Parágrafo introdutório de 2-3 frases. Contextualiza a seção e faz transição do conteúdo anterior.]  
  ```  
- **Exemplo**:  
  ```markdown
  ## Tipos de Diagramas UML  
  Os diagramas UML se dividem em estruturais e comportamentais. Esta seção cobre os 13 tipos oficiais e seus casos de uso em desenvolvimento de software.  
  ```

#### **1.3 Subtítulos (H3)**  
- **Quantidade**: 2-4 por H2  
- **Formato obrigatório**:  
  ```markdown
  ### [Título H3 com 2-4 palavras]  
  [Parágrafo introdutório de 1-2 frases. Explica o foco específico deste subtópico.]  
  ```  
- **Exemplo**:  
  ```markdown
  ### Diagrama de Classes  
  Fundamental para modelagem estática, este diagrama representa a estrutura do sistema. Vamos explorar seus componentes essenciais.  
  ```

---

### **2. Conteúdo Textual**  
#### **2.1 Parágrafos**  
- **Por H2**: 3-6 parágrafos  
- **Tamanho**: 40-70 palavras (2-4 frases)  
- **Regra**: Sempre iniciar seções H2/H3 com parágrafo introdutório  

#### **2.2 Listas**  
- **Formato obrigatório**:  
  ```markdown
  [Parágrafo contextual explicando o propósito da lista]  
  - Item 1  
  - Item 2  
  ```  
- **Exemplo**:  
  ```markdown
  Para casos de uso eficientes, inclua estes elementos-chave conforme o padrão IEEE 830:  
  1. Identificador único  
  2. Atores principais  
  3. Fluxo básico  
  ```

---

## **📐 Métricas Recomendadas**  
| **Elemento**         | **Posts Padrão**       | **Guias Completos**    | **Artigos Introdutórios** |  
|-----------------------|------------------------|------------------------|---------------------------|  
| **Palavras**          | 900-1330           | 1,400-2,500           | 800-1,200                |   
| **H2**               | 4-7                   | 5-8                   | 3-5                      |  
| **H3 por H2**        | 2-4                   | 3-5                   | 1-3                      |  
| **Imagens**          | 2-4                   | 4-6                   | 1-3                      |  
| **Links Internos**   | 3-5                   | 5-7                   | 2-4                      |  
| **Links Externos**   | 4-8                   | 6-10                  | 3-5                      |  

---

## **🖼️ Diretrizes para Elementos Visuais**  
### **Imagens**  
- **Legenda**: 5-10 palavras (ex.: "Figura 1: Diagrama de Sequência UML")  
- **Alt Text**: 3-8 palavras descritivas (ex.: "Diagrama UML mostrando interação entre classes")  
- **Dimensões**: 600-800px de largura  

### **Exemplo de Uso**:  
```markdown
As ferramentas de prototipagem moderna oferecem recursos avançados:  
![Ferramenta Figma com protótipo aberto](figma.jpg)  
*Figura 2: Interface do Figma com protótipo interativo*  
```

---

## **✅ Checklist Final**  
Antes de publicar, verifique:  

1. **Estrutura**  
   - [ ] Todo H2 tem introdução (2-3 frases)  
   - [ ] H3 relevantes têm introdução (1-2 frases)  

2. **Conteúdo**  
   - [ ] Listas precedidas por contexto  
   - [ ] Parágrafos com 40-70 palavras  

3. **Elementos**  
   - [ ] 2-4 imagens com legenda e alt text  
   - [ ] 3-5 links internos e 4-8 externos  

4. **Otimização**  
   - [ ] Título H1 dentro do padrão  
   - [ ] Subtítulo quando necessário  

---

## **📊 Template Prático**  
```markdown
# [Título H1]  
[Subtítulo opcional]  

## [Seção H2]  
[Introdução de 2-3 frases]  

### [Subseção H3]  
[Introdução de 1-2 frases]  
[Parágrafo com conteúdo]  

[Contexto para lista]  
- Item 1  
- Item 2  

![Descrição da imagem](imagem.jpg)  
*Legenda da imagem*  
```

---

## **🎯 Objetivo do CustomGPT**  
Este padrão garante:  
- **Consistência** em todos os artigos  
- **Otimização SEO** (1000+ palavras, estrutura clara)  
- **Experiência do leitor** (transições suaves entre tópicos)  

**Nota**: Adaptar quantidades conforme complexidade do tópico, mantendo sempre a estrutura base.