# Documento Unificado de Padronização para Arquivos e Projetos

## 1. Padrão para Cabeçalhos em Arquivos de Prompt

### Estrutura Obrigatória para Arquivos de Prompt
```markdown
file-name: tmpl-[titulo-em-kebab-case]-[versao].md
title: [Título curto e descritivo (max 43 caracteres)]
prompt-category: [Categoria temática]
language: pt-BR
version: [Versão no formato a33, b33, etc.]
author: Chico Alff
updated-at: [AAAA-MM-DD HH:MM:SS]
```

### Diretrizes Específicas:
- **Título**: Deve refletir objetivamente o conteúdo principal (ex: "Refinamento de User Stories")
- **Nome do arquivo**: Formato kebab-case sem conectores ("de", "a", "e")
- **Versão**: Incremental (a33 → b33 → c33...)
- **Atualização**: Sempre registrar data/hora da última modificação

## 2. Template Genérico para Cabeçalhos de Arquivos

### Estrutura Completa:
```markdown
file-name: [prefixo]-[nome-descritivo]-[versao].[extensao]
title: [Título descritivo (max 50 caracteres)]
document-type: [Tipo de documento]
category: [Categoria temática]
language: [Código ISO 639-1]
version: [Versão (vX.X.X ou [letra][numero])]
author: [Autor principal]
contributors: [Opcional: colaboradores]
department: [Opcional: área responsável]
status: [Status atual]
created-at: [AAAA-MM-DD HH:MM:SS]
updated-at: [AAAA-MM-DD HH:MM:SS]
tags: [Opcional: palavras-chave]
description: [Opcional: breve descrição (max 100 caracteres)]
```

### Campos Prioritários:
1. **Obrigatórios**: file-name, title, document-type, version, author, updated-at
2. **Recomendados**: category, language, status, created-at
3. **Opcionais**: contributors, department, tags, description

## 3. Template para Apresentação de Projetos

### Estrutura Básica:
```markdown
# Projeto: [nome-do-projeto]

## Descrição
[2-3 frases sobre propósito e diferencial]

## Contextualização
[Contexto, objetivo e público-alvo]

## 1. Visão Geral
[Definição, escopo e finalidade]

## 2. Diferenciais Competitivos
- [Diferencial 1]: [explicação]
- [Diferencial 2]: [explicação]

## 3. [Estrutura Técnica/Recursos]
- [Componente 1]: [função]
- [Componente 2]: [função]

## 4. Funcionalidades Principais
- [Funcionalidade 1 detalhada]
- [Funcionalidade 2 detalhada]

## 5. Benchmark de Concorrentes
[Tabela comparativa]

## 6. Oportunidades de Mercado
[Análise de potencial]

## Palavras-chave
[lista separada por vírgulas]

**Site Oficial:** [link]
```

### Diretrizes de Formatação:
- **Permitido**:
  - Títulos com # e ##
  - Negrito para ênfase (**texto**)
  - Listas com - ou números
  - Tabelas em markdown básico
  - Separadores --- entre blocos

- **Proibido**:
  - Ícones/emojis
  - Cores ou formatação visual
  - Títulos aninhados (### ou mais)
  - Citações (>) desnecessárias

## 4. Princípios Comuns a Todos os Templates

### Organização:
- Agrupar informações similares em blocos coesos
- Manter sequência lógica de apresentação
- Preservar todo conteúdo informacional original

### Versionamento:
- Atualizar sempre `version` e `updated-at` em modificações
- Usar convenções consistentes (a33, v1.0.0, etc.)

### Estilo:
- Tom profissional e direto
- Linguagem clara e concisa
- Frases completas e parágrafos curtos
- Foco em informação acionável

## 5. Checklist de Validação Unificada

- [ ] Estrutura de blocos completa e ordenada
- [ ] Formatação conforme diretrizes
- [ ] Conteúdo original preservado
- [ ] Metadados atualizados (versão, data)
- [ ] Campos obrigatórios preenchidos
- [ ] Tom profissional mantido
- [ ] Nomenclatura consistente
- [ ] Informações logicamente agrupadas

## Exemplo Integrado

**Cabeçalho de Arquivo:**
```markdown
file-name: tmpl-apresentacao-projetos-b33.md
title: Template para Apresentação de Projetos
document-type: Template
category: Documentação
language: pt-BR
version: b33
author: Chico Alff
status: Ativo
created-at: 2025-06-20 09:00:00
updated-at: 2025-06-21 10:30:00
tags: template, projeto, documentação
description: Template unificado para apresentação de projetos
```

**Seção de Projeto:**
```markdown
# Projeto: ProductNauta

## Descrição
Plataforma de gestão de produtos com IA. Integra análise de mercado e desenvolvimento ágil em uma única solução.

## 1. Visão Geral
SaaS para PMEs com ferramentas de priorização e roadmap visual...

## 2. Diferenciais Competitivos
- **IA Predictiva**: Antecipa tendências com 92% de acurácia...
```

