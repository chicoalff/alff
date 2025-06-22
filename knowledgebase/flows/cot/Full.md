{
  "versao": "2.0",
  "fonte_primaria": "guia-artigo-padrao.md",
  "fluxo_completo": {
    "coleta_inicial": {
      "etapa": 1,
      "detalhes": {
        "instrucoes": [
          "Solicitar descrição do tópico principal",
          "Coletar arquivos complementares (PDFs, imagens, links)",
          {
            "definir_tipo_artigo": {
              "introdutorio": {"palavras": "800-1.200"},
              "padrao": {"palavras": "1.200-1.800"},
              "guia_completo": {"palavras": "1.800-2.500"}
            }
          }
        ],
        "objetivos_qualidade": [
          "Consistência editorial",
          "Otimização SEO (1000+ palavras)",
          "Experiência fluida do leitor"
        ]
      }
    },
    "analise_semantica": {
      "etapa": 2,
      "detalhes": {
        "metricas_tipos": {
          "tabela_comparativa": [
            {
              "elemento": "Palavras",
              "introdutorio": "800-1.200",
              "padrao": "1.200-1.800",
              "guia_completo": "1.800-2.500"
            },
            {
              "elemento": "H2",
              "introdutorio": "3-5",
              "padrao": "4-7",
              "guia_completo": "5-8"
            }
          ]
        },
        "processos": [
          {
            "identificacao_palavras_chave": {
              "quantidade": 10,
              "fontes": ["conteúdo fornecido", "SERP"]
            }
          }
        ]
      }
    },
    "pesquisa_titulos": {
      "etapa": 3,
      "detalhes": {
        "requisitos_titulos": {
          "h1": {
            "formato": "5-9 palavras (45-65 caracteres)",
            "exemplos": [
              "O que são Requisitos Não-Funcionais?",
              "Guia Completo de Especificação de Requisitos"
            ]
          },
          "subtitulo": {
            "formato": "8-12 palavras (opcional)"
          }
        }
      }
    },
    "estrutura_hierarquica": {
      "etapa": 4,
      "detalhes": {
        "regras": {
          "h2": {
            "quantidade": "4-7",
            "caracteristicas": [
              "3-5 palavras",
              "parágrafo introdutório (2-3 frases)"
            ]
          },
          "h3": {
            "quantidade_por_h2": "2-4",
            "caracteristicas": [
              "2-4 palavras",
              "parágrafo introdutório (1-2 frases)"
            ]
          }
        },
        "template_toc": {
          "exemplo": [
            "1. Introdução",
            "2. [H2 Principal]",
            "2.1 [H3 Secundário]",
            "6. Conclusão",
            "7. FAQ"
          ]
        }
      }
    },
    "desenvolvimento_blocos": {
      "etapa": 5,
      "detalhes": {
        "elementos_multimidia": {
          "imagens": {
            "diretrizes": {
              "legenda": "5-10 palavras com padrão 'Figura N: Descrição'",
              "alt_text": "3-8 palavras descritivas sem número",
              "dimensoes": "600-800px de largura"
            }
          }
        },
        "workflow": [
          "Escrever H2 + introdução",
          "Desenvolver H3 relacionados",
          "Validar com usuário"
        ]
      }
    },
    "otimizacao_tecnica": {
      "etapa": 6,
      "detalhes": {
        "elementos": [
          {
            "meta_tags": {
              "title": {
                "limite": "45-65 caracteres",
                "exemplo": "Requisitos Funcionais vs Não-Funcionais: Diferenças Chave"
              },
              "description": {
                "limite": "150 caracteres"
              }
            }
          },
          {
            "links": {
              "internos": "3-5",
              "externos": "4-8"
            }
          }
        ]
      }
    },
    "revisao_final": {
      "etapa": 7,
      "detalhes": {
        "checklist": {
          "estrutura": [
            "Todo H2 tem introdução (2-3 frases)",
            "H3 relevantes têm introdução (1-2 frases)"
          ],
          "conteudo": [
            "Listas precedidas por contexto",
            "Parágrafos com 40-70 palavras"
          ]
        }
      }
    }
  },
  "templates_globais": {
    "artigo_completo": "# [Título H1]\n[Subtítulo opcional]\n\n## [Seção H2]\n[Introdução de 2-3 frases]\n\n### [Subseção H3]\n[Introdução de 1-2 frases]",
    "elementos": {
      "lista": "[Contexto para lista]\n- Item 1\n- Item 2",
      "imagem": "![Descrição da imagem](imagem.jpg)\n*Legenda da imagem*"
    }
  }
}