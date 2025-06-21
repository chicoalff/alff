# TEMPLATE DE CABEÇALHO GENÉRICO PARA ARQUIVOS

Este template fornece um padrão estruturado para criação de cabeçalhos em qualquer tipo de arquivo, garantindo organização, identificação e rastreabilidade consistentes. Adapte os campos conforme necessário para seu contexto específico.

## ESTRUTURA DO CABEÇALHO

### 1. `file-name`
* Nome do arquivo com extensão apropriada
* Utilize convenções de nomenclatura consistentes (kebab-case recomendado)
* Formato sugerido: `[prefixo]-[nome-descritivo]-[versao].[extensao]`
* Exemplo: `doc-manual-usuario-v1.0.md`

### 2. `title`
* Título claro e descritivo (máximo 50 caracteres)
* Deve refletir objetivamente o conteúdo do arquivo
* Exemplo: `Manual do Usuário - Sistema de Vendas`

### 3. `document-type`
* Tipo/categoria do documento
* Exemplos: `Documentação`, `Especificação`, `Manual`, `Relatório`, `Código`, `Configuração`

### 4. `category`
* Categoria temática ou departamental
* Exemplos: `Desenvolvimento`, `Recursos Humanos`, `Financeiro`, `Operações`

### 5. `language`
* Idioma principal do conteúdo
* Formato ISO 639-1 (ex: `pt-BR`, `en-US`, `es-ES`)

### 6. `version`
* Versão do documento/arquivo
* Formato sugerido: `v[major].[minor].[patch]` ou `[letra][numero]`
* Exemplos: `v1.0.0`, `a33`, `beta-2.1`

### 7. `author`
* Nome do autor principal ou responsável
* Pode incluir múltiplos autores separados por vírgula

### 8. `contributors` (opcional)
* Lista de colaboradores adicionais
* Formato: nomes separados por vírgula

### 9. `department` (opcional)
* Departamento ou área responsável
* Exemplo: `TI`, `Marketing`, `Qualidade`

### 10. `status`
* Status atual do documento
* Exemplos: `Rascunho`, `Em Revisão`, `Aprovado`, `Arquivado`, `Ativo`

### 11. `created-at`
* Data e hora de criação inicial
* Formato: `AAAA-MM-DD HH:MM:SS`

### 12. `updated-at`
* Data e hora da última atualização
* Formato: `AAAA-MM-DD HH:MM:SS`

### 13. `tags` (opcional)
* Palavras-chave para facilitar busca e categorização
* Formato: palavras separadas por vírgula

### 14. `description` (opcional)
* Breve descrição do conteúdo (máximo 100 caracteres)

## EXEMPLO DE CABEÇALHO COMPLETO

```
file-name: doc-manual-usuario-sistema-vendas-v1.2.md
title: Manual do Usuário - Sistema de Vendas
document-type: Documentação
category: Sistemas
language: pt-BR
version: v1.2.0
author: Maria Silva
contributors: João Santos, Pedro Costa
department: TI
status: Aprovado
created-at: 2025-01-15 09:30:00
updated-at: 2025-06-20 14:15:00
tags: manual, vendas, sistema, usuário
description: Guia completo para utilização do sistema de vendas da empresa
```

## EXEMPLO DE CABEÇALHO MÍNIMO

Para arquivos simples, utilize apenas os campos essenciais:

```
file-name: config-database-prod.yml
title: Configuração do Banco de Dados - Produção
document-type: Configuração
category: Infraestrutura
version: v2.1
author: Admin Sistema
updated-at: 2025-06-20 14:15:00
```

## DIRETRIZES DE USO

1. **Obrigatórios**: `file-name`, `title`, `document-type`, `version`, `author`, `updated-at`
2. **Recomendados**: `category`, `language`, `status`, `created-at`
3. **Opcionais**: `contributors`, `department`, `tags`, `description`
4. **Consistência**: Mantenha o mesmo padrão em todos os arquivos do projeto
5. **Atualização**: Sempre atualize `updated-at` e `version` quando modificar o arquivo

## BENEFÍCIOS

- **Organização**: Facilita a localização e categorização de arquivos
- **Rastreabilidade**: Histórico claro de versões e modificações
- **Colaboração**: Identificação clara de responsáveis e contribuidores
- **Manutenção**: Facilita a gestão e atualização de documentos
- **Busca**: Tags e categorias melhoram a descoberta de conteúdo