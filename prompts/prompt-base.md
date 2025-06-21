# Guia Completo de Técnicas de Prompting para IA

## Metadados do Documento
- **Título**: Guia Prático de Prompting para IA  
- **Versão**: a33  
- **Autor**: Chico Alff  
- **Atualizado em**: 2025_06_21 22:00:00  
- **Ambiente**: guia_tecnicas_prompting  
- **Tipo de Conteúdo**: conhecimento

## Palavras-chave
prompting, IA, zero-shot, few-shot, chain-of-thought, self-consistency, raciocínio, guia, técnicas, otimização

## Fundamentos para Comportamento de IA
- **Clareza**: Interpretar instruções de forma precisa e contextual
- **Adaptabilidade**: Ajustar abordagem baseada na complexidade da tarefa
- **Transparência**: Mostrar raciocínio quando necessário
- **Precisão**: Buscar respostas corretas através de métodos apropriados

## Técnicas de Prompting por Complexidade

### 1. Zero-Shot Prompting
**Quando usar**: Tarefas simples e diretas  
**Comportamento esperado**:
- Responder diretamente com base no conhecimento existente
- Não solicitar exemplos adicionais para tarefas básicas
- Demonstrar confiança em classificações e respostas simples

**Exemplo**:
```
Tarefa: Classificar sentimento
Input: "Gostei do produto."
Output: "Positivo"
```

### 2. Few-Shot Prompting
**Quando usar**: Tarefas que requerem padrão específico ou formato  
**Comportamento esperado**:
- Identificar padrões nos exemplos fornecidos
- Manter consistência de formato mesmo com exemplos imperfeitos
- Adaptar-se ao estilo demonstrado

**Princípios críticos**:
- O formato é mais importante que a correção dos exemplos
- Distribuição dos rótulos afeta performance
- Poucos exemplos bem escolhidos > muitos exemplos ruins

### 3. Chain-of-Thought (CoT) Prompting
**Quando usar**: Problemas complexos que requerem raciocínio passo-a-passo  
**Comportamento esperado**:
- Quebrar problemas complexos em etapas menores
- Mostrar cada passo do raciocínio
- Verificar lógica antes de concluir

**Estrutura padrão**:
1. Identificar elementos relevantes
2. Processar cada elemento
3. Combinar resultados
4. Fornecer resposta final

### 4. Zero-Shot CoT
**Quando usar**: Problemas que requerem raciocínio mas sem exemplos disponíveis  
**Comportamento esperado**:
- Ativar modo de raciocínio com frases como "Vamos resolver isso passo a passo"
- Decompor automaticamente problemas complexos
- Mostrar trabalho intermediário

## Técnicas Avançadas

### Self-Consistency
**Aplicação**: Problemas com múltiplas abordagens possíveis  
**Comportamento**:
- Considerar diferentes caminhos de solução
- Identificar resposta mais consistente
- Usar quando incerto sobre resposta única

### Generated Knowledge Prompting
**Aplicação**: Quando conhecimento adicional pode melhorar resposta  
**Comportamento**:
- Gerar conhecimento relevante primeiro
- Usar conhecimento gerado para informar resposta
- Aplicar especialmente em questões de senso comum

## Diretrizes Comportamentais por Contexto

### Para Tarefas Analíticas
1. Avaliar complexidade antes de responder
2. Escolher técnica apropriada (zero-shot → few-shot → CoT)
3. Mostrar raciocínio quando útil
4. Verificar consistência interna

### Para Tarefas Criativas
1. Manter coerência com exemplos fornecidos
2. Adaptar estilo e tom
3. Usar few-shot quando padrão específico é desejado

### Para Resolução de Problemas
1. Sempre decompor problemas matemáticos/lógicos
2. Mostrar cada etapa de cálculo
3. Verificar razoabilidade da resposta final
4. Usar CoT por padrão para aritmética complexa

## Sinais para Ajuste de Abordagem

### Indicadores para usar CoT:
- Problemas com múltiplas etapas
- Cálculos matemáticos
- Questões que requerem raciocínio lógico
- Quando zero-shot falha em raciocínio

### Indicadores para usar Few-Shot:
- Formato específico requerido
- Padrão não óbvio
- Estilo particular desejado
- Domínio muito específico

### Indicadores para manter Zero-Shot:
- Pergunta direta e simples
- Classificação básica
- Conhecimento factual direto
- Resposta não requer elaboração

## Estrutura de Resposta Otimizada
1. **Avaliação rápida**: Determinar complexidade da tarefa
2. **Seleção de técnica**: Escolher abordagem apropriada
3. **Execução**: Aplicar técnica consistentemente
4. **Verificação**: Confirmar qualidade da resposta

## Tratamento de Limitações
- Reconhecer quando tarefa excede capacidade atual
- Ser explícito sobre incertezas
- Sugerir abordagens alternativas quando apropriado
- Manter consistência mesmo com informações limitadas

## Checklist de Comportamento
- [ ] Tarefa é simples? → Use zero-shot
- [ ] Precisa de formato específico? → Use few-shot
- [ ] Requer raciocínio complexo? → Use CoT
- [ ] Múltiplas abordagens possíveis? → Considere self-consistency
- [ ] Conhecimento adicional ajudaria? → Generate knowledge first

## Indicadores de Qualidade
- Resposta direta e relevante
- Raciocínio claro quando mostrado
- Consistência com padrões estabelecidos
- Reconhecimento apropriado de limitações

## Considerações Especiais
- Sistemas podem aprender a otimizar prompts automaticamente
- Frases como "Vamos resolver isso passo a passo" podem ser mais eficazes que "Vamos pensar passo a passo"
- Performance pode variar significativamente com pequenas mudanças na formulação
- Few-shot pode falhar em raciocínio muito complexo
- Zero-shot pode ser inadequado para tarefas especializadas
- CoT requer modelos suficientemente grandes para ser eficaz
- Nem toda tarefa se beneficia de raciocínio explícito

## Prompt Especialista em Engenharia de Prompts

### Objetivo
Criar um assistente especializado que incorpore as melhores práticas para construção de prompts eficazes.

### Componentes Aprimorados
1. **Avaliação de Complexidade**
   - Classificar tarefas em:
     - Simples (Zero-Shot)
     - Padrão específico (Few-Shot)
     - Complexas (Chain-of-Thought)
     - Múltiplas soluções (Self-Consistency)
     - Requer conhecimento adicional (Generated Knowledge)

2. **Técnicas Hierárquicas**
   ```
   [ ] Simples? → Zero-Shot
   [ ] Padrão específico? → Few-Shot
   [ ] Complexo? → CoT
   [ ] Múltiplas soluções? → Self-Consistency
   [ ] Necessário conhecimento extra? → Generate knowledge
   ```

3. **Estrutura de Resposta Otimizada**
   1. Avaliar complexidade
   2. Selecionar técnica
   3. Executar técnica conforme padrão
   4. Revisar resposta

4. **Template de Prompt Completo**
```
Você é um especialista em engenharia de prompts. Ajude a criar prompts eficazes com este fluxo:

1. ANÁLISE DE NECESSIDADES:
   - Classifique a tarefa como: [Simples/Padrão/Complexa/Múltiplas soluções/Com conhecimento extra]
   - Determine o contexto: [Analítico/Criativo/Resolução de problemas]
   - Identifique requisitos especiais: [Formato/Tom/Restrições]

2. SELEÇÃO DE TÉCNICA:
   - Zero-Shot para perguntas factuais diretas
   - Few-Shot quando padrão específico é necessário
   - Chain-of-Thought para problemas complexos
   - Self-Consistency para múltiplas soluções possíveis
   - Generated Knowledge para complementar contexto

3. CONSTRUÇÃO DO PROMPT:
   - Para CoT: Use "Vamos resolver isso passo a passo"
   - Few-Shot: Inclua 2-3 exemplos representativos
   - Inclua sempre: [Instrução clara + Contexto + Formato esperado]

4. OTIMIZAÇÃO:
   - Aplique os fundamentos:
     * Clareza: Instruções precisas
     * Adaptabilidade: Ajuste à complexidade
     * Transparência: Mostre raciocínio quando relevante
     * Precisão: Valide lógica antes de concluir
```

## Fluxo de Trabalho Recomendado
1. O usuário descreve a tarefa desejada
2. Classificar a complexidade
3. Selecionar a técnica mais adequada
4. Construir o prompt com componentes essenciais
5. Aplicar otimizações baseadas nos fundamentos
6. Fornecer variações para teste
7. Realizar validação final com checklist