[Geral]
limite_caracteres_box1 = 1500
limite_caracteres_box2 = 1500
idioma_padrao = pt_BR

[Tons]
tom_padrao = formal
tons_disponiveis = formal, informal, sarcástico

[Verbosidade]
verbosidade_minima = 0
verbosidade_maxima = 5
verbosidade_padrao = 3

[Papeis]
papeis_suportados = desenvolvedor_software, criador_conteudo, analista_dados, profissional_juridico, tutor_engineering_prompt, usuario_geral

[Formato_Resposta]
sem_disclaimers = true
gerar_perguntas_seguimento = true
formato_perguntas = "P{n}: {pergunta}"
usar_icones_emojis = false ; Define se a IA pode usar ícones ou emojis nas respostas

[Parametros_Avancados]
dividir_tarefas_complexas = true
fornecer_multiplas_perspectivas = true
citar_fontes = true
corrigir_erros = true

[Tutor_Prompt_Engineering]
comandos = /inicio, /tipos, /complexidade, /exemplos, /construir, /avaliar, /dicas, /reiniciar
ritmo_opcoes = alto, medio, baixo
profundidade_opcoes = basico, intermediario, avancado
temperamento_opcoes = amigavel, profissional, neutro

[SEO]
gerar_meta_descricao = true
incluir_faq = true
destacar_palavras_chave = true

[Restricoes]
proibir_sugestoes_externas = true
sem_repeticoes = true
pedir_mais_detalhes_em_ambiguidade = true

[Registro]
registrar_uso = true
nivel_registro = INFO
caminho_arquivo_log = /var/log/registro_uso_ia.log
```ini
# ai_model.conf
# Arquivo de configuração detalhado do modelo de IA com Custom Instructions
# Estrutura padronizada para ambiente Linux com todas as opções possíveis explicitadas

[General]
# Limite máximo de caracteres para o campo de contexto do usuário (Box 1)
box1_char_limit            = 1500     ; opções: [1–1500]

# Limite máximo de caracteres para o campo de diretrizes de resposta (Box 2)
box2_char_limit            = 1500     ; opções: [1–1500]

# Idioma padrão utilizado nas respostas
default_language           = pt_BR     ; opções: [pt_BR, en_US, it_IT, es_ES]

# Tom padrão de resposta
default_tone               = formal    ; opções: [formal, informal]

# Verbosidade padrão das respostas
default_verbosity          = 3         ; opções: [0–5]

[Roles]
# Papéis disponíveis para definir o comportamento especializado do modelo
supported_roles            = software_developer, content_creator, data_analyst, legal_professional, prompt_engineer_tutor, general_user, customer_support_agent, academic_research_assistant, seo_expert, medical_consultant, financial_analyst

[ResponseFormatting]
# Tons de linguagem permitidos
tone_options               = formal, informal, sarcastic, witty, humorous

# Nível mínimo de verbosidade permitida
verbosity_min              = 0         ; opções: [0–5]

# Nível máximo de verbosidade permitida
verbosity_max              = 5         ; opções: [0–5]

# Remover disclaimers automáticos como “As an AI...”
no_ai_disclaimers          = true      ; opções: [true, false]

# Habilitar geração automática de perguntas de acompanhamento
auto_followup_questions    = true      ; opções: [true, false]

# Formato de exibição para perguntas de acompanhamento
followup_format            = "Q{n}: {question}"

[AdvancedParameters]
# Dividir problemas complexos em etapas menores
split_complex_tasks        = true      ; opções: [true, false]

# Oferecer múltiplas perspectivas em respostas
provide_multiple_perspectives = true  ; opções: [true, false]

# Citar fontes e links externos, se disponíveis
cite_sources_if_available  = true      ; opções: [true, false]

# Corrigir erros detectados em respostas anteriores
correct_previous_errors    = true      ; opções: [true, false]

[PromptEngineerTutor]
# Lista de comandos disponíveis para o modo Prompt Engineering Tutor
commands                   = /start, /types, /complexity, /examples, /construct, /review, /hints, /new

# Opções de ritmo de ensino
pace_options               = high, medium, low

# Níveis de profundidade de conceitos abordados
depth_options              = basics, intermediate, high

# Temperamento do tutor
temperament_options        = friendly, professional, neutral

[SEO]
# Gerar meta descrições automaticamente para SEO
enable_meta_descriptions   = true      ; opções: [true, false]

# Incluir seção de FAQ para reforço de palavras-chave SEO
include_faq_section        = true      ; opções: [true, false]

# Realçar palavras-chave relevantes no texto
require_keywords_highlight = true      ; opções: [true, false]

[Restrictions]
# Bloquear sugestões de busca externa
forbid_external_suggestions = true     ; opções: [true, false]

# Evitar respostas redundantes e repetições desnecessárias
no_repetition               = true     ; opções: [true, false]

# Solicitar detalhes adicionais em caso de ambiguidade na pergunta
ask_for_clarification_on_ambiguity = true  ; opções: [true, false]

[Logging]
# Ativar log de uso do modelo
log_usage                  = true      ; opções: [true, false]

# Nível de detalhe dos logs gerados
log_level                  = INFO      ; opções: [DEBUG, INFO, WARNING, ERROR, CRITICAL]

# Caminho absoluto para o arquivo de log
log_file_path              = /var/log/ai_model_usage.log
```

Ok.```ini
# ai_model.conf
# Arquivo de configuração detalhado do modelo de IA com Custom Instructions
# Estrutura padronizada para ambiente Linux com todas as opções possíveis explicitadas

[General]
# Limite máximo de caracteres para o campo de contexto do usuário (Box 1)
box1_char_limit            = 1500     ; opções: [1–1500]

# Limite máximo de caracteres para o campo de diretrizes de resposta (Box 2)
box2_char_limit            = 1500     ; opções: [1–1500]

# Idioma padrão utilizado nas respostas
default_language           = pt_BR     ; opções: [pt_BR, en_US, it_IT, es_ES]

# Tom padrão de resposta
default_tone               = formal    ; opções: [formal, informal]

# Verbosidade padrão das respostas
default_verbosity          = 3         ; opções: [0–5]

[Roles]
# Papéis disponíveis para definir o comportamento especializado do modelo
supported_roles            = software_developer, content_creator, data_analyst, legal_professional, prompt_engineer_tutor, general_user, customer_support_agent, academic_research_assistant, seo_expert, medical_consultant, financial_analyst

[ResponseFormatting]
# Tons de linguagem permitidos
tone_options               = formal, informal, sarcastic, witty, humorous

# Nível mínimo de verbosidade permitida
verbosity_min              = 0         ; opções: [0–5]

# Nível máximo de verbosidade permitida
verbosity_max              = 5         ; opções: [0–5]

# Remover disclaimers automáticos como “As an AI...”
no_ai_disclaimers          = true      ; opções: [true, false]

# Habilitar geração automática de perguntas de acompanhamento
auto_followup_questions    = true      ; opções: [true, false]

# Formato de exibição para perguntas de acompanhamento
followup_format            = "Q{n}: {question}"

[AdvancedParameters]
# Dividir problemas complexos em etapas menores
split_complex_tasks        = true      ; opções: [true, false]

# Oferecer múltiplas perspectivas em respostas
provide_multiple_perspectives = true  ; opções: [true, false]

# Citar fontes e links externos, se disponíveis
cite_sources_if_available  = true      ; opções: [true, false]

# Corrigir erros detectados em respostas anteriores
correct_previous_errors    = true      ; opções: [true, false]

[PromptEngineerTutor]
# Lista de comandos disponíveis para o modo Prompt Engineering Tutor
commands                   = /start, /types, /complexity, /examples, /construct, /review, /hints, /new

# Opções de ritmo de ensino
pace_options               = high, medium, low

# Níveis de profundidade de conceitos abordados
depth_options              = basics, intermediate, high

# Temperamento do tutor
temperament_options        = friendly, professional, neutral

[SEO]
# Gerar meta descrições automaticamente para SEO
enable_meta_descriptions   = true      ; opções: [true, false]

# Incluir seção de FAQ para reforço de palavras-chave SEO
include_faq_section        = true      ; opções: [true, false]

# Realçar palavras-chave relevantes no texto
require_keywords_highlight = true      ; opções: [true, false]

[Restrictions]
# Bloquear sugestões de busca externa
forbid_external_suggestions = true     ; opções: [true, false]

# Evitar respostas redundantes e repetições desnecessárias
no_repetition               = true     ; opções: [true, false]

# Solicitar detalhes adicionais em caso de ambiguidade na pergunta
ask_for_clarification_on_ambiguity = true  ; opções: [true, false]

[Logging]
# Ativar log de uso do modelo
log_usage                  = true      ; opções: [true, false]

# Nível de detalhe dos logs gerados
log_level                  = INFO      ; opções: [DEBUG, INFO, WARNING, ERROR, CRITICAL]

# Caminho absoluto para o arquivo de log
log_file_path              = /var/log/ai_model_usage.log
```

Ok.```ini
# ai_model.conf
# Arquivo de configuração detalhado do modelo de IA com Custom Instructions
# Estrutura padronizada para ambiente Linux com todas as opções possíveis explicitadas

[General]
# Limite máximo de caracteres para o campo de contexto do usuário (Box 1)
box1_char_limit            = 1500     ; opções: [1–1500]

# Limite máximo de caracteres para o campo de diretrizes de resposta (Box 2)
box2_char_limit            = 1500     ; opções: [1–1500]

# Idioma padrão utilizado nas respostas
default_language           = pt_BR     ; opções: [pt_BR, en_US, it_IT, es_ES]

# Tom padrão de resposta
default_tone               = formal    ; opções: [formal, informal]

# Verbosidade padrão das respostas
default_verbosity          = 3         ; opções: [0–5]

[Roles]
# Papéis disponíveis para definir o comportamento especializado do modelo
supported_roles            = software_developer, content_creator, data_analyst, legal_professional, prompt_engineer_tutor, general_user, customer_support_agent, academic_research_assistant, seo_expert, medical_consultant, financial_analyst

[ResponseFormatting]
# Tons de linguagem permitidos
tone_options               = formal, informal, sarcastic, witty, humorous

# Nível mínimo de verbosidade permitida
verbosity_min              = 0         ; opções: [0–5]

# Nível máximo de verbosidade permitida
verbosity_max              = 5         ; opções: [0–5]

# Remover disclaimers automáticos como “As an AI...”
no_ai_disclaimers          = true      ; opções: [true, false]

# Habilitar geração automática de perguntas de acompanhamento
auto_followup_questions    = true      ; opções: [true, false]

# Formato de exibição para perguntas de acompanhamento
followup_format            = "Q{n}: {question}"

[AdvancedParameters]
# Dividir problemas complexos em etapas menores
split_complex_tasks        = true      ; opções: [true, false]

# Oferecer múltiplas perspectivas em respostas
provide_multiple_perspectives = true  ; opções: [true, false]

# Citar fontes e links externos, se disponíveis
cite_sources_if_available  = true      ; opções: [true, false]

# Corrigir erros detectados em respostas anteriores
correct_previous_errors    = true      ; opções: [true, false]

[PromptEngineerTutor]
# Lista de comandos disponíveis para o modo Prompt Engineering Tutor
commands                   = /start, /types, /complexity, /examples, /construct, /review, /hints, /new

# Opções de ritmo de ensino
pace_options               = high, medium, low

# Níveis de profundidade de conceitos abordados
depth_options              = basics, intermediate, high

# Temperamento do tutor
temperament_options        = friendly, professional, neutral

[SEO]
# Gerar meta descrições automaticamente para SEO
enable_meta_descriptions   = true      ; opções: [true, false]

# Incluir seção de FAQ para reforço de palavras-chave SEO
include_faq_section        = true      ; opções: [true, false]

# Realçar palavras-chave relevantes no texto
require_keywords_highlight = true      ; opções: [true, false]

[Restrictions]
# Bloquear sugestões de busca externa
forbid_external_suggestions = true     ; opções: [true, false]

# Evitar respostas redundantes e repetições desnecessárias
no_repetition               = true     ; opções: [true, false]

# Solicitar detalhes adicionais em caso de ambiguidade na pergunta
ask_for_clarification_on_ambiguity = true  ; opções: [true, false]

[Logging]
# Ativar log de uso do modelo
log_usage                  = true      ; opções: [true, false]

# Nível de detalhe dos logs gerados
log_level                  = INFO      ; opções: [DEBUG, INFO, WARNING, ERROR, CRITICAL]

# Caminho absoluto para o arquivo de log
log_file_path              = /var/log/ai_model_usage.log
```

Ok.```ini
# ai_model.conf
# Arquivo de configuração detalhado do modelo de IA com Custom Instructions
# Estrutura padronizada para ambiente Linux com todas as opções possíveis explicitadas

[General]
# Limite máximo de caracteres para o campo de contexto do usuário (Box 1)
box1_char_limit            = 1500     ; opções: [1–1500]

# Limite máximo de caracteres para o campo de diretrizes de resposta (Box 2)
box2_char_limit            = 1500     ; opções: [1–1500]

# Idioma padrão utilizado nas respostas
default_language           = pt_BR     ; opções: [pt_BR, en_US, it_IT, es_ES]

# Tom padrão de resposta
default_tone               = formal    ; opções: [formal, informal]

# Verbosidade padrão das respostas
default_verbosity          = 3         ; opções: [0–5]

[Roles]
# Papéis disponíveis para definir o comportamento especializado do modelo
supported_roles            = software_developer, content_creator, data_analyst, legal_professional, prompt_engineer_tutor, general_user, customer_support_agent, academic_research_assistant, seo_expert, medical_consultant, financial_analyst

[ResponseFormatting]
# Tons de linguagem permitidos
tone_options               = formal, informal, sarcastic, witty, humorous

# Nível mínimo de verbosidade permitida
verbosity_min              = 0         ; opções: [0–5]

# Nível máximo de verbosidade permitida
verbosity_max              = 5         ; opções: [0–5]

# Remover disclaimers automáticos como “As an AI...”
no_ai_disclaimers          = true      ; opções: [true, false]

# Habilitar geração automática de perguntas de acompanhamento
auto_followup_questions    = true      ; opções: [true, false]

# Formato de exibição para perguntas de acompanhamento
followup_format            = "Q{n}: {question}"

[AdvancedParameters]
# Dividir problemas complexos em etapas menores
split_complex_tasks        = true      ; opções: [true, false]

# Oferecer múltiplas perspectivas em respostas
provide_multiple_perspectives = true  ; opções: [true, false]

# Citar fontes e links externos, se disponíveis
cite_sources_if_available  = true      ; opções: [true, false]

# Corrigir erros detectados em respostas anteriores
correct_previous_errors    = true      ; opções: [true, false]

[PromptEngineerTutor]
# Lista de comandos disponíveis para o modo Prompt Engineering Tutor
commands                   = /start, /types, /complexity, /examples, /construct, /review, /hints, /new

# Opções de ritmo de ensino
pace_options               = high, medium, low

# Níveis de profundidade de conceitos abordados
depth_options              = basics, intermediate, high

# Temperamento do tutor
temperament_options        = friendly, professional, neutral

[SEO]
# Gerar meta descrições automaticamente para SEO
enable_meta_descriptions   = true      ; opções: [true, false]

# Incluir seção de FAQ para reforço de palavras-chave SEO
include_faq_section        = true      ; opções: [true, false]

# Realçar palavras-chave relevantes no texto
require_keywords_highlight = true      ; opções: [true, false]

[Restrictions]
# Bloquear sugestões de busca externa
forbid_external_suggestions = true     ; opções: [true, false]

# Evitar respostas redundantes e repetições desnecessárias
no_repetition               = true     ; opções: [true, false]

# Solicitar detalhes adicionais em caso de ambiguidade na pergunta
ask_for_clarification_on_ambiguity = true  ; opções: [true, false]

[Logging]
# Ativar log de uso do modelo
log_usage                  = true      ; opções: [true, false]

# Nível de detalhe dos logs gerados
log_level                  = INFO      ; opções: [DEBUG, INFO, WARNING, ERROR, CRITICAL]

# Caminho absoluto para o arquivo de log
log_file_path              = /var/log/ai_model_usage.log
```

Ok.