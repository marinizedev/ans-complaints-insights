---
title: ANS Complaints Insights
emoji: 🏥
colorFrom: green
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

<div align="center">

# 🏥 ANS Complaints Insights

### Data Storytelling sobre reclamações de planos de saúde no Brasil

![CI](https://github.com/marinizedev/ans-complaints-insights/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.24-3F4F75?logo=plotly&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97_Hugging_Face-Space-FFD21E)
![License](https://img.shields.io/badge/Licen%C3%A7a-MIT-2dd4a0)

[**🚀 Acessar o Dashboard ao Vivo**](https://huggingface.co/spaces/marinizeeng/ans-complaints-insights)

</div>

---

## 📖 Sobre o Projeto

Este projeto nasceu de uma pergunta simples:

> **As reclamações dos beneficiários de planos de saúde cresceram porque aumentou o número de pessoas com plano — ou há algo mais grave acontecendo?**

A resposta emerge da análise dos dados.

Entre 2015 e 2024, a base de beneficiários cresceu **21%**. As reclamações cresceram **296%**. Os dados mostram uma mudança de padrão a partir de 2020, período que coincide com a pandemia — sem retorno ao ritmo anterior. Essa associação é uma hipótese exploratória, não uma relação causal comprovada.

O projeto percorre todo o ciclo analítico: da coleta e processamento dos dados brutos da ANS até a construção de um dashboard interativo de Data Storytelling, passando por análise exploratória aprofundada, correção de metodologia de cálculo do IGR, descoberta de insights e documentação rigorosa de todas as hipóteses investigadas.

---

## 📌 O que este projeto entrega

Além da construção do dashboard, o projeto contempla todas as etapas de um fluxo analítico completo:

- entendimento da base de dados;

- limpeza e padronização dos dados;

- investigação metodológica;

- análise exploratória (EDA);

- validação de hipóteses;

- descoberta de insights;

- construção do Data Storytelling;

- desenvolvimento de dashboard interativo;

- testes automatizados;

- integração e deploy contínuos (CI/CD).

Durante o desenvolvimento foi identificada e corrigida uma inconsistência importante na forma de calcular o IGR agregado, garantindo que todas as análises utilizassem a metodologia adequada para a comparação entre carteiras de tamanhos diferentes.

---

## 🖥️ Demonstração

### Página Inicial

![Home](https://private-us-east-1.manuscdn.com/sessionFile/UBGsxQ0ggPDaW9JQtDLpfC/sandbox/X6fUXQSOKxokzWPx9Ge080-images_1790702876444_na1fn_L2hvbWUvdWJ1bnR1L2Fucy1jb21wbGFpbnRzLXJldmlldy9yZXBvL2ltYWdlcy9ob21l.png?Expires=1790875678&Signature=MEQCIFmJk5zc2hajS-uBwHBLjo1rV1ZQ-qdkGIWjbcVwausuAiB3ZrdnCZIXDVtEbt~VAtYqReVaWQCbD8WM5lAAIZ7r4w__&Key-Pair-Id=K1K5N5YNBUUMMN)

### Visão Geral — métricas e panorama do período

![Visão Geral](https://private-us-east-1.manuscdn.com/sessionFile/UBGsxQ0ggPDaW9JQtDLpfC/sandbox/X6fUXQSOKxokzWPx9Ge080-images_1790702876444_na1fn_L2hvbWUvdWJ1bnR1L2Fucy1jb21wbGFpbnRzLXJldmlldy9yZXBvL2ltYWdlcy92aXNhb19nZXJhbA.png?Expires=1790875678&Signature=MEYCIQC1TRfwQaKzPCxEdHfL9Q5ju12O5Fdss7tpV0cKe6YoWwIhAM7acxD2Macu4p6hwe9ehai-BePIPbL0ldrGZpnIb1AQ&Key-Pair-Id=K1K5N5YNBUUMMN)

### Temporal — o marco da pandemia de 2020

![Temporal](https://private-us-east-1.manuscdn.com/sessionFile/UBGsxQ0ggPDaW9JQtDLpfC/sandbox/X6fUXQSOKxokzWPx9Ge080-images_1790702876444_na1fn_L2hvbWUvdWJ1bnR1L2Fucy1jb21wbGFpbnRzLXJldmlldy9yZXBvL2ltYWdlcy90ZW1wb3JhbA.png?Expires=1790875678&Signature=MEUCIQDE1Hg34pHcPj8t43F3B1VO50FVS11Voad7y-4qQ7EPHgIgbxqXnYhUWgUH8QzzrZXYL4oLtyt3bLxO3F7og72~dSQ_&Key-Pair-Id=K1K5N5YNBUUMMN)

### Operadoras — rankings e outliers

![Operadoras](https://private-us-east-1.manuscdn.com/sessionFile/UBGsxQ0ggPDaW9JQtDLpfC/sandbox/X6fUXQSOKxokzWPx9Ge080-images_1790702876444_na1fn_L2hvbWUvdWJ1bnR1L2Fucy1jb21wbGFpbnRzLXJldmlldy9yZXBvL2ltYWdlcy9vcGVyYWRvcmFz.png?Expires=1790875678&Signature=MEUCIQCxpaVSK~E9e9as4MgbbOd14UE7P2tgFUNlzxyYkr9QywIgFrk0Dht6Y~RjLVnJDBlvOD04~jeFdE3jw~Nueuf2N7o_&Key-Pair-Id=K1K5N5YNBUUMMN)

---

## 🔍 Principais Descobertas

### 📌 Mudança de padrão a partir de 2020

Antes de 2020, o crescimento das reclamações era lento e irregular. A partir de 2020, a curva muda de inclinação e **não retorna ao ritmo anterior**. Os dados sugerem uma mudança de padrão, mas não permitem afirmar que a pandemia foi sua causa.

### 📌 Grande porte concentra desproporcionalmente

Operadoras de grande porte representam apenas **9,89%** dos registros na base, mas concentram **82,54%** de todas as reclamações — razão de concentração de **8,35×**.

### 📌 Tamanho da carteira não explica tudo

A correlação entre quantidade de beneficiários e reclamações é moderada (**0,54**). Operadoras com carteiras semelhantes apresentam comportamentos completamente distintos — fatores operacionais e de qualidade de atendimento exercem papel relevante.

### 📌 Assistência médica vs odontológica

O IGR da assistência médica é **27 vezes** maior que o da cobertura exclusivamente odontológica no recorte de 2024. A diferença observada é um padrão descritivo da base, não uma explicação causal.

### 📌 Prevent Senior — outlier entre operadoras ativas

IGR de **1.321,33** — **65 vezes** acima do IGR de mercado (20,162). Única operadora ativa nesse patamar, com comportamento completamente distinto das demais grandes operadoras.

### 📌 Operadoras em falência continuam impactando beneficiários

71 operadoras identificadas com indícios de falência ou liquidação. O padrão sugere que a deterioração do serviço começa **antes** da falência formal.

### 📌 Inversão histórica em 2026

Pela primeira vez na série, o porte médio (IGR 35,823) superou o grande porte (IGR 31,859). Comportamento monitorado — 2026 é ano parcial.

---

## 🔄 Fluxo Analítico

![fluxo](https://private-us-east-1.manuscdn.com/sessionFile/UBGsxQ0ggPDaW9JQtDLpfC/sandbox/X6fUXQSOKxokzWPx9Ge080-images_1790702876444_na1fn_L2hvbWUvdWJ1bnR1L2Fucy1jb21wbGFpbnRzLXJldmlldy9yZXBvL2ltYWdlcy9mbHV4b19hbmFsaXRpY28.png?Expires=1790875678&Signature=MEUCIEcENM6SdYhQNUXAdMGxz-m~i40bTG6Be~ESJs4ipcIMAiEAnMQPp6pZAnfuMEJ5t8lGTZo~-Z~Xo4oD-iS1AXYLu7g_&Key-Pair-Id=K1K5N5YNBUUMMN)

---

## ⚠️ Descoberta Metodológica Importante

Durante a EDA surgiu uma inconsistência nos resultados.

Os valores anuais do IGR estavam completamente fora da realidade.

> Esta foi a descoberta técnica mais relevante do projeto e impacta diretamente a confiabilidade de qualquer análise sobre o IGR.

A coluna `IGR` do dataset da ANS já contém o índice **calculado individualmente** para cada operadora. Calcular a média aritmética desse campo dá o mesmo peso a carteiras de tamanhos diferentes e não representa adequadamente o IGR agregado do mercado.

**❌ Método incorreto — média simples:**

```python
df.groupby("competencia")["igr"].mean()
# Média descritiva entre operadoras, não o IGR agregado do mercado
```

**✅ Método correto — adotado neste projeto:**

```python
igr_correto = (
    df.groupby("competencia")
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
)
igr_correto["igr"] = (
    igr_correto["total_reclamacoes"]
    / igr_correto["total_beneficiarios"]
    * 100000
)
```

**Fórmula do IGR:** `IGR = (QTD_RECLAMACOES / QTD_BENEFICIARIOS) × 100.000`

> **Revisão posterior:** a ponderação pela carteira foi mantida, mas o cálculo do projeto foi alinhado à unidade oficial de “por 100.000 beneficiários”, em vez da escala “por 1.000” usada anteriormente no projeto. O dicionário da ANS descreve `COMPETENCIA` e `COMPETENCIA_BENEFICIARIO` como ano-mês, mas o arquivo efetivamente recebido contém apenas o ano. A base apresenta múltiplas observações compatíveis com periodicidade mensal, sem o mês explícito; não há evidência de que essa informação tenha sido removida pelo ETL. Consulte a [nota metodológica da revisão](docs/revisao_metodologica_2026.md).

---

## 🗂️ Estrutura do Projeto

```
ans-complaints-insights/
│
├── .github/
│   └── workflows/
│       └── main.yml              # CI/CD: testes, build Docker e deploy
│
├── .dockerignore                 # Arquivos excluídos do contexto Docker
├── .gitattributes                # Regras de Git LFS para dados e imagens
├── .gitignore                    # Ambientes, caches e arquivos locais
├── Dockerfile                    # Imagem de produção do dashboard
├── docker-compose.yml            # Execução local reproduzível
├── pyproject.toml                # Metadados e faixa de Python suportada
│
├── app/                          # Módulo do dashboard
│   ├── __init__.py
│   ├── data_loader.py            # Carregamento, cache e agregações
│   └── styles.py                 # CSS global e layout Plotly (tema Teal)
│
├── data/
│   ├── raw/                      # Dados brutos da ANS
│   └── processed/
│       └── igr_processed.csv     # Base consolidada utilizada pelo dashboard
│
├── docs/                         # Documentação analítica completa
│   ├── data_understanding_report.md
│   ├── investigacao_inicial.md
│   ├── revisao_metodologica_2026.md
│   ├── insights_iniciais.md
│   ├── hypotheses.md
│   └── perguntas_negocio.md
│
├── images/                       # Screenshots do dashboard
│
├── pages/                        # Páginas do dashboard Streamlit
│   ├── 1_Visão_Geral.py
│   ├── 2_Temporal.py
│   ├── 3_Porte.py
│   ├── 4_Operadoras.py
│   └── 5_Explorar.py
│
├── src/                          # Scripts de análise
│   ├── data_understanding.py     # Etapa 1 — entendimento da base
│   ├── process_igr.py            # Etapa 2 — processamento e limpeza
│   ├── exploratory_analysis.py   # Etapa 3 — EDA principal
│   └── eda_complementar.py       # Etapa 3B — EDA com IGR correto
│
├── tests/
│   └── test_dados.py             # Testes de regras de negócio
│
├── main.py                       # Ponto de entrada do Streamlit
├── requirements.txt               # Dependências da aplicação e testes
├── README.md                      # Documentação, execução e arquitetura
└── LICENSE
```

---

## 🚀 Como Executar Localmente

**Pré-requisitos:** Python >=3.11 e <3.14

```bash
# Clone o repositório
git clone https://github.com/marinizedev/ans-complaints-insights.git
cd ans-complaints-insights

# Crie e ative o ambiente virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run main.py
```

> **Observação:** o projeto utiliza Git LFS para versionamento eficiente da base processada. Caso o repositório seja clonado sem suporte ao Git LFS, o mecanismo de fallback implementado no projeto realiza automaticamente a obtenção do dataset necessário para execução da aplicação e dos testes.

### Executar com Docker

Com Docker Desktop instalado, a aplicação pode ser executada em um ambiente
reprodutível, sem criar um ambiente virtual Python local:

```bash
docker build -t ans-complaints-insights .
docker run --rm -p 8501:7860 ans-complaints-insights
```

Acesse `http://localhost:8501` no navegador.

Também é possível usar Docker Compose:

```bash
docker compose up --build
```

Para encerrar:

```bash
docker compose down
```

O container escuta internamente na porta `7860`, compatível com o padrão de
aplicações Docker no Hugging Face Spaces.

---

## 🧪 Testes

```bash
pytest tests/
```

O pipeline de CI executa os testes de regras de negócio automaticamente a cada push ou pull request via **GitHub Actions**.

---

## 🔄 Integração e Deploy Contínuos (CI/CD )

Este projeto utiliza um pipeline automatizado de CI/CD com GitHub Actions e Hugging Face Spaces.

### Continuous Integration (CI)

A cada push ou pull request:

- configuração automática do ambiente Python 3.11;

- instalação das dependências;

- execução da suíte de testes com `pytest`;

- validação das regras de negócio da aplicação;

- construção da imagem Docker para validar a containerização.

### Continuous Deployment (CD)

Após a conclusão bem-sucedida do estágio de CI na branch `main`, o deploy é realizado automaticamente para o Hugging Face Spaces.

O pipeline utiliza autenticação segura via GitHub Secrets (`HF_TOKEN`) e sincroniza o código diretamente com o repositório remoto do Space por meio de um `git push` automatizado. O Hugging Face identifica `sdk: docker` no README, constrói o `Dockerfile` e executa o container na porta `7860`.

Essa estratégia simplifica o processo de deploy e reduz a dependência de Actions específicas do Hugging Face, tornando o pipeline mais transparente e fácil de manter.

Durante o pipeline, o GitHub Actions realiza normalmente o checkout do repositório com suporte ao Git LFS, garantindo que os arquivos versionados sejam disponibilizados corretamente durante a execução do workflow.

---

## 📊 Fonte dos Dados

| Item | Detalhe |
| --- | --- |
| **Origem** | Portal de Dados Abertos da ANS |
| **Dataset** | Índice Geral de Reclamações (IGR) |
| **Período analisado** | 2015–2026* |
| **Registros** | 151.501 |
| **Operadoras** | 1.411 |
| **Cobertura** | Assistência médica e odontológica |

* O ano de 2026 contém dados parciais.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
| --- | --- |
| Linguagem | Python 3.11 |
| Processamento de Dados | Pandas 2.2 |
| Dashboard | Streamlit 1.45 |
| Visualizações | Plotly 5.24 |
| Testes | pytest 8.3 |
| CI/CD | GitHub Actions |
| Deploy | Hugging Face Spaces |
| Containerização | Docker / Docker Compose |
| Controle de versão | Git |
| Armazenamento de arquivos grandes | Git LFS |

---

## 👩‍💻 Sobre

Projeto desenvolvido por **Marinize Santana** como parte do portfólio de Data Engineering e Analytics Engineering.

Estudante de Análise e Desenvolvimento de Sistemas na UniFECAF, com foco em construir soluções analíticas baseadas em problemas reais.

Este projeto foi desenvolvido com foco na aplicação de boas práticas de Engenharia de Dados, Analytics Engineering e Data Storytelling utilizando dados públicos da ANS.

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Marinize_Santana-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/marinize-santana-47bb2b372)
[![GitHub](https://img.shields.io/badge/GitHub-marinizedev-181717?logo=github&logoColor=white)](https://github.com/marinizedev)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97_Space-ans--complaints--insights-FFD21E)](https://huggingface.co/spaces/marinizeeng/ans-complaints-insights)

</div>
