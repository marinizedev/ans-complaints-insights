# ==================================================================
# ANS COMPLAINTS INSIGHTS

# ETAPA 3 — EDA (EXPLORATORY DATA ANALYSIS)

# Objetivo: Explorar os dados para análises.

# ==================================================================

import pandas as pd
from pathlib import Path

# ==================================================================
# 1. CARREGAR BASE PROCESSADA
# ==================================================================

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminho do arquivo
arquivo = BASE_DIR / "data" / "processed" / "igr_processed.csv"

df = pd.read_csv(
    arquivo, 
    sep=",",
    encoding="utf-8")

print("\n=============================")
print("ARQUIVO CARREGADO COM SUCESSO")
print("=============================\n")

# =================================================================
# 2. RECLAMAÇÕES POR ANO
# =================================================================

print("\nRECLAMAÇÕES POR ANO")

reclamacoes_por_ano = (
    df.groupby("competencia")
    ["qtd_reclamacoes"]
    .sum()
    .reset_index()
    .sort_values("competencia")
)

print(reclamacoes_por_ano)

# =================================================================
# 3. BENEFICIÁRIOS POR ANO
# =================================================================

print("\nBENEFICIÁRIOS POR ANO")

beneficiarios_por_ano = (
    df.groupby("competencia")["qtd_beneficiarios"]
    .sum()
    .reset_index()
    .sort_values("competencia")
)

print(beneficiarios_por_ano)

# =================================================================
# 4. IGR MÉDIO POR ANO
# =================================================================

print("\nIGR MÉDIO POR ANO")

igr_medio_por_ano = (
    df.groupby("competencia")["igr"]
    .mean()
    .reset_index()
    .sort_values("competencia")
)

print(igr_medio_por_ano)

# =================================================================
# 5. COBERTURA
# =================================================================

print("\nRECLAMAÇÕES POR COBERTURA")

reclamacoes_por_cobertura = (
    df.groupby("cobertura")["qtd_reclamacoes"]
    .sum()
    .reset_index()
    .sort_values(
        "qtd_reclamacoes",
        ascending=False
    )
)

print(reclamacoes_por_cobertura)

# =================================================================
# 6. PORTE
# =================================================================

print("\nRECLAMAÇÕES POR PORTE")

reclamacoes_por_porte = (
    df.groupby("porte_operadora")["qtd_reclamacoes"]
    .sum()
    .reset_index()
    .sort_values(
        "qtd_reclamacoes",
        ascending=False
    )
)

print(reclamacoes_por_porte)

# ==========================================================
# 7. PARTICIPAÇÃO DAS COBERTURAS
# ==========================================================

print("\nPARTICIPAÇÃO DAS COBERTURAS")

participacao_cobertura = (
    df.groupby("cobertura")["qtd_reclamacoes"]
    .sum()
    .reset_index()
)

total_reclamacoes = (
    participacao_cobertura["qtd_reclamacoes"]
    .sum()
)

participacao_cobertura["percentual"] = (
    participacao_cobertura["qtd_reclamacoes"]
    / total_reclamacoes
    * 100
)

print(participacao_cobertura)

# ==========================================================
# 8. PARTICIPAÇÃO DOS PORTES
# ==========================================================

print("\nPARTICIPAÇÃO DOS PORTES")

participacao_porte = (
    df.groupby("porte_operadora")["qtd_reclamacoes"]
    .sum()
    .reset_index()
)

total_reclamacoes = (
    participacao_porte["qtd_reclamacoes"]
    .sum()
)

participacao_porte["percentual"] = (
    participacao_porte["qtd_reclamacoes"]
    / total_reclamacoes
    * 100
)

print(participacao_porte)

# ==========================================================
# 9. RECLAMAÇÕES POR BENEFICIÁRIO
# ==========================================================

print("\nRECLAMAÇÕES POR BENEFICIÁRIO")

reclamacoes_beneficiarios = (
    df.groupby("competencia")
    .agg(
        {
            "qtd_reclamacoes": "sum",
            "qtd_beneficiarios": "sum"
        }
    )
    .reset_index()
)

reclamacoes_beneficiarios["reclamacoes_por_mil_beneficiarios"] = (
    reclamacoes_beneficiarios["qtd_reclamacoes"]
    / reclamacoes_beneficiarios["qtd_beneficiarios"]
    * 1000
)

print(reclamacoes_beneficiarios)

# ==========================================================
# 10. RECLAMAÇÕES POR MIL BENEFICIÁRIOS POR PORTE
# ==========================================================

print("\nRECLAMAÇÕES POR MIL BENEFICIÁRIOS POR PORTE")

porte_normalizado = (
    df.groupby("porte_operadora")
    .agg(
        {
            "qtd_reclamacoes": "sum",
            "qtd_beneficiarios": "sum"
        }
    )
    .reset_index()
)

porte_normalizado["reclamacoes_por_mil_beneficiarios"] = (
    porte_normalizado["qtd_reclamacoes"]
    / porte_normalizado["qtd_beneficiarios"]
    * 1000
)

porte_normalizado = (
    porte_normalizado
    .sort_values(
        by="reclamacoes_por_mil_beneficiarios",
        ascending=False
    )
)

print(porte_normalizado)

# ==========================================================
# 11. TOP 10 TAXAS BRUTAS (sem filtro de beneficiários)
# ==========================================================

print("\nTOP 10 TAXAS BRUTAS (sem filtro de beneficiários)")

operadoras_taxa = (
    df.groupby(
        ["registro_ans", "razao_social"]
    )
    .agg(
        {
            "qtd_reclamacoes": "sum",
            "qtd_beneficiarios": "sum"
        }
    )
    .reset_index()
)

operadoras_taxa["reclamacoes_por_mil_beneficiarios"] = (
    operadoras_taxa["qtd_reclamacoes"]
    / operadoras_taxa["qtd_beneficiarios"]
    * 1000
)

operadoras_taxa = (
    operadoras_taxa
    .sort_values(
        by="reclamacoes_por_mil_beneficiarios",
        ascending=False
    )
)

top10_taxa = operadoras_taxa.head(10)

print(top10_taxa)

# ==========================================================
# 12. TOP 10 OPERADORAS COM MAIOR TAXA DE RECLAMAÇÃO
#       (filtro mínimo de 10 mil beneficiários)
# ==========================================================

print("\nTOP OPERADORAS (FILTRO MÍNIMO DE BENEFICIÁRIOS)")

operadoras_filtradas = (
    operadoras_taxa[
        operadoras_taxa["qtd_beneficiarios"] >= 10000
    ]
)

top10_filtrado = (
    operadoras_filtradas
    .sort_values(
        by="reclamacoes_por_mil_beneficiarios",
        ascending=False
    )
    .head(10)
)

print(top10_filtrado.to_string())

# ==========================================================
# 13. COMPARAÇÃO ENTRE QUANTIDADE E TAXA
# ==========================================================

print("\nTOP 10 POR QUANTIDADE DE RECLAMAÇÕES")

top_qtd = (
    operadoras_taxa
    .sort_values(
        by="qtd_reclamacoes",
        ascending=False
    )
    .head(10)
)

print(
    top_qtd[
        [
            "registro_ans",
            "razao_social",
            "qtd_reclamacoes",
            "qtd_beneficiarios",
            "reclamacoes_por_mil_beneficiarios"
        ]
    ].to_string(index=False)
)

# ==========================================================
# 14. CORRELAÇÃO ENTRE BENEFICIÁRIOS E RECLAMAÇÕES
# ==========================================================

print("\nCORRELAÇÃO ENTRE BENEFICIÁRIOS E RECLAMAÇÕES")

correlacao = (
    df[
        [
            "qtd_beneficiarios",
            "qtd_reclamacoes"
        ]
    ]
    .corr()
)

print(correlacao)

print("\nTOP 10 OPERADORAS POR BENEFICIÁRIOS")

top_beneficiarios = (
    df.groupby(
        [
            "registro_ans",
            "razao_social"
        ],
        as_index=False
    )
    .agg(
        {
            "qtd_beneficiarios": "sum",
            "qtd_reclamacoes": "sum"
        }
    )
    .sort_values(
        by="qtd_beneficiarios",
        ascending=False
    )
    .head(10)
)

print(top_beneficiarios.to_string())

# ==========================================================
# 15. OPERADORAS EM FALÊNCIA E LIQUIDAÇÃO
# ==========================================================

print("\nOPERADORAS EM FALÊNCIA E LIQUIDAÇÃO")

falidas = df[
    df["razao_social"]
    .str.contains(
        "FALIDA|LIQUIDAÇÃO",
        case=False,
        na=False
    )
]

print(
    falidas[
        [
            "registro_ans",
            "razao_social",
            "qtd_reclamacoes",
            "qtd_beneficiarios"
        ]
    ]
    .groupby("razao_social")
    .sum()
    .sort_values(
        by="qtd_reclamacoes",
        ascending=False
    )
    .head(20)
)

print(
    f"\nTotal de registros encontrados: {len(falidas):,}"
)

print(
    f"Total de operadoras únicas: "
    f"{falidas['razao_social'].nunique()}"
)

print(
    "\nPrimeiras operadoras encontradas:\n"
)

print(
    falidas[
        [
            "registro_ans",
            "razao_social"
        ]
    ]
    .drop_duplicates()
    .head(20)
    .to_string(index=False)
)

falidas_resumo = (
    falidas
    .groupby(
        "razao_social",
        as_index=False
    )
    .agg(
        {
            "qtd_reclamacoes": "sum",
            "qtd_beneficiarios": "sum"
        }
    )
    .sort_values(
        by="qtd_reclamacoes",
        ascending=False
    )
)

print(
    falidas_resumo
    .head(20)
    .to_string(index=False)
)

# ==========================================================
# 16. RECLAMAÇÕES DE OPERADORAS FALIDAS POR ANO
# ==========================================================

print("\nRECLAMAÇÕES DE OPERADORAS FALIDAS POR ANO")

falidas_por_ano = (
    falidas
    .groupby("competencia")
    ["qtd_reclamacoes"]
    .sum()
    .reset_index()
    .sort_values("competencia")
)

print(falidas_por_ano)