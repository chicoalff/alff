file-name: tmpl-cabecalho-prompt-a33.md title: Padrão para Cabeçalho em Arquivos de Prompt prompt-category: Documentação e Padronização language: pt-BR version: a33 author: Chico Alff updated-at: 2025-06-20 14:15:00

## INSTRUÇÃO DE CRIAÇÃO DE CABEÇALHO PADRÃO

Este documento define o padrão obrigatório para criação de cabeçalhos em arquivos Markdown contendo prompts de instrução para modelos de Inteligência Artificial. Siga rigorosamente as instruções abaixo para garantir consistência e fácil identificação dos arquivos gerados.

### 1. `title`

* Deve ser curto, claro e descritivo, com no máximo 43 caracteres.
* Deve refletir objetivamente o conteúdo principal do prompt.
* Exemplo válido: `Refinamento de User Stories`

### 2. `prompt-category`

* Identifique claramente a categoria temática do prompt.
* Utilize termos técnicos ou de domínio específicos.
* Exemplos: `Gestão de Produto`, `Análise de Dados`, `Desenvolvimento Ágil`.

### 3. `file-name`

* Utilize o formato padrão:

```
tmpl-[titulo-em-kebab-case]-[versao].md
```

* Não utilize conectores como "de", "a", "e" entre as palavras.
* Exemplo válido: `tmpl-refinamento-user-stories-a33.md`

### 4. `version`

* Utilize versão incremental no formato letra+número, iniciando sempre com `a33`.
* Exemplo: primeira versão `a33`, segunda versão `b33`, etc.

### 5. `author`

* Utilize sempre `Chico Alff`, exceto se explicitamente informado outro autor.

### 6. `updated-at`

* Informe data e hora exatas da última atualização no formato:

```
AAAA-MM-DD HH:MM:SS
```

* Exemplo: `2025-06-20 14:15:00`

**Exemplo Completo:**

```markdown
file-name: tmpl-refinamento-user-stories-a33.md
title: Refinamento de User Stories
prompt-category: Desenvolvimento Ágil
language: pt-BR
version: a33
author: Chico Alff
updated-at: 2025-06-20 14:15:00
```
