# ==================================================================
# ANS COMPLAINTS INSIGHTS

# ETAPA 3B — EDA COMPLEMENTAR

# Objetivo: Aprofundar análises identificadas como lacunas na EDA
# principal e corrigir o cálculo do IGR médio anual.

# Por que este script existe?
# ----------------------------
# Durante a EDA principal (exploratory_analysis.py), o IGR foi
# calculado via média aritmética simples entre operadoras:
#
#   df.groupby("competencia")["igr"].mean()
#
# Esse cálculo produziu valores completamente fora de escala,
# chegando a 357 em 2022. A causa foi identificada na investigação
# inicial: a coluna IGR já contém o índice calculado pela ANS para
# cada operadora individualmente. Fazer média aritmética desse campo
# ignora o tamanho de cada carteira, distorcendo o resultado.
#
# A solução correta é recalcular o IGR agregando numerador e
# denominador separadamente antes de aplicar a fórmula:
#
#   IGR = (SOMA(qtd_reclamacoes) / SOMA(qtd_beneficiarios)) * 1.000
#
# Para documentação completa sobre essa descoberta, consultar:
#   docs/investigacao_inicial.md

# Lacunas investigadas neste script:
# ------------------------------------
#   1. IGR recalculado corretamente por ano (ponderado)
#   2. IGR por porte (recalculado)
#   3. IGR por cobertura (recalculado)
#   4. Evolução das coberturas ao longo do tempo
#   5. Tratamento e sinalização do ano parcial (2026)
#   6. Participação do porte: registros vs reclamações
#   7. Dispersão do IGR por operadora (identificação de outliers)
#   8. Comparação IGR: grandes operadoras vs mercado
#   9. Evolução do IGR por porte ao longo do tempo

# Entrada:  data/processed/igr_processed.csv
# Saída:    resultados impressos no terminal
# ==================================================================

import pandas as pd
from pathlib import Path

# ==================================================================
# 1. CARREGAR BASE PROCESSADA
# ==================================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = BASE_DIR / "data" / "processed" / "igr_processed.csv"

df = pd.read_csv(
    arquivo,
    sep=",",
    encoding="utf-8",
    low_memory=False
)

print("\n=============================")
print("ARQUIVO CARREGADO COM SUCESSO")
print("=============================\n")

# ==================================================================
# 2. IGR CORRETO POR ANO
# ==================================================================

# Recalcula o IGR ponderando pela carteira de beneficiários.
# Isso elimina a distorção causada pela média simples do campo IGR.
# 2026 é sinalizado como ano parcial para evitar interpretações
# incorretas de queda no índice.

print("IGR CORRETO POR ANO (ponderado pela carteira)")

igr_por_ano = (
    df.groupby("competencia")
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

igr_por_ano["igr_correto"] = (
    igr_por_ano["total_reclamacoes"]
    / igr_por_ano["total_beneficiarios"]
    * 1000
)

igr_por_ano["ano_parcial"] = igr_por_ano["competencia"] == 2026

print(igr_por_ano.to_string(index=False))

# ------------------------------------------------------------------
# Comparativo: média simples vs IGR correto
# Evidencia o tamanho do erro no cálculo anterior.
# ------------------------------------------------------------------

print("\nCOMPARATIVO — MÉDIA SIMPLES vs IGR CORRETO")

igr_media_simples = (
    df.groupby("competencia")["igr"]
    .mean()
    .reset_index()
    .rename(columns={"igr": "igr_media_simples"})
)

comparativo = igr_por_ano.merge(
    igr_media_simples,
    on="competencia"
)

print(
    comparativo[
        [
            "competencia",
            "igr_media_simples",
            "igr_correto",
            "ano_parcial"
        ]
    ].to_string(index=False)
)

# ==================================================================
# 3. IGR CORRETO POR PORTE
# ==================================================================

# Recalcula o IGR por porte usando a mesma lógica de ponderação.
# O resultado anterior (exploratory_analysis.py, seção 10) já
# usava qtd_reclamacoes / qtd_beneficiarios diretamente, portanto
# estava correto. Este bloco reconfirma os valores com a notação
# padronizada.

print("\nIGR CORRETO POR PORTE")

igr_por_porte = (
    df.groupby("porte_operadora")
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

igr_por_porte["igr_correto"] = (
    igr_por_porte["total_reclamacoes"]
    / igr_por_porte["total_beneficiarios"]
    * 1000
)

igr_por_porte = igr_por_porte.sort_values(
    "igr_correto",
    ascending=False
)

print(igr_por_porte.to_string(index=False))

# ==================================================================
# 4. IGR CORRETO POR COBERTURA
# ==================================================================

# Lacuna da EDA principal: o IGR por cobertura não havia sido
# calculado. Este bloco revela a diferença real entre assistência
# médica e exclusivamente odontológica.

print("\nIGR CORRETO POR COBERTURA")

igr_por_cobertura = (
    df.groupby("cobertura")
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

igr_por_cobertura["igr_correto"] = (
    igr_por_cobertura["total_reclamacoes"]
    / igr_por_cobertura["total_beneficiarios"]
    * 1000
)

print(igr_por_cobertura.to_string(index=False))

# ==================================================================
# 5. EVOLUÇÃO DAS COBERTURAS AO LONGO DO TEMPO
# ==================================================================

# Lacuna da EDA principal: a cobertura havia sido analisada de forma
# estática (total acumulado). Este bloco investiga se a participação
# de cada cobertura mudou ao longo dos anos e como o IGR evoluiu
# separadamente para médica e odontológica.

print("\nEVOLUÇÃO DAS COBERTURAS POR ANO")

cobertura_por_ano = (
    df.groupby(["competencia", "cobertura"])
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

cobertura_por_ano["igr_correto"] = (
    cobertura_por_ano["total_reclamacoes"]
    / cobertura_por_ano["total_beneficiarios"]
    * 1000
)

print(cobertura_por_ano.to_string(index=False))

# ------------------------------------------------------------------
# Participação percentual de cada cobertura por ano
# ------------------------------------------------------------------

print("\nPARTICIPAÇÃO PERCENTUAL DAS COBERTURAS POR ANO")

total_por_ano = (
    df.groupby("competencia")["qtd_reclamacoes"]
    .sum()
    .reset_index()
    .rename(columns={"qtd_reclamacoes": "total_ano"})
)

cobertura_pct = cobertura_por_ano.merge(
    total_por_ano,
    on="competencia"
)

cobertura_pct["percentual"] = (
    cobertura_pct["total_reclamacoes"]
    / cobertura_pct["total_ano"]
    * 100
).round(2)

print(
    cobertura_pct[
        [
            "competencia",
            "cobertura",
            "total_reclamacoes",
            "percentual",
            "igr_correto"
        ]
    ].to_string(index=False)
)

# ==================================================================
# 6. ANÁLISE DO ANO PARCIAL — 2026
# ==================================================================

# 2026 está presente na base com dados incompletos.
# Este bloco investiga a granularidade disponível e compara
# as métricas com 2024 como referência de ano completo recente.
# O objetivo é documentar o caráter parcial de 2026 para que
# as visualizações possam sinalizá-lo adequadamente.

print("\nANÁLISE DO ANO PARCIAL — 2026")

competencias_2026 = (
    df[df["competencia"] == 2026]["competencia_beneficiario"]
    .dropna()
    .unique()
)

print("Valores únicos de competencia_beneficiario em 2026:")
print(sorted(competencias_2026))

ano_2026 = df[df["competencia"] == 2026]

resumo_2026 = pd.DataFrame({
    "métrica": [
        "Total reclamações",
        "Total beneficiários",
        "IGR correto",
        "Operadoras únicas"
    ],
    "2026 (parcial)": [
        ano_2026["qtd_reclamacoes"].sum(),
        ano_2026["qtd_beneficiarios"].sum(),
        round(
            ano_2026["qtd_reclamacoes"].sum()
            / ano_2026["qtd_beneficiarios"].sum()
            * 1000, 6
        ),
        ano_2026["registro_ans"].nunique()
    ],
    "2024 (referência)": [
        df[df["competencia"] == 2024]["qtd_reclamacoes"].sum(),
        df[df["competencia"] == 2024]["qtd_beneficiarios"].sum(),
        round(
            df[df["competencia"] == 2024]["qtd_reclamacoes"].sum()
            / df[df["competencia"] == 2024]["qtd_beneficiarios"].sum()
            * 1000, 6
        ),
        df[df["competencia"] == 2024]["registro_ans"].nunique()
    ]
})

print(resumo_2026.to_string(index=False))

# ==================================================================
# 7. PORTE — REGISTROS NA BASE vs PARTICIPAÇÃO NAS RECLAMAÇÕES
# ==================================================================

# Lacuna da EDA principal: o porte havia sido analisado apenas por
# volume absoluto de reclamações. Este bloco calcula a razão de
# concentração, que revela o descompasso entre representatividade
# na base e impacto nas reclamações.

print("\nPORTE — REGISTROS NA BASE vs PARTICIPAÇÃO NAS RECLAMAÇÕES")

total_registros = len(df)
total_reclamacoes_geral = df["qtd_reclamacoes"].sum()

porte_dupla = (
    df.groupby("porte_operadora")
    .agg(
        registros=("registro_ans", "count"),
        reclamacoes=("qtd_reclamacoes", "sum"),
        operadoras_unicas=("registro_ans", "nunique")
    )
    .reset_index()
)

porte_dupla["pct_registros"] = (
    porte_dupla["registros"] / total_registros * 100
).round(2)

porte_dupla["pct_reclamacoes"] = (
    porte_dupla["reclamacoes"] / total_reclamacoes_geral * 100
).round(2)

# razao_concentracao: quanto o porte concentra de reclamações
# em relação à sua representatividade na base.
# > 1: concentra proporcionalmente mais reclamações
# < 1: concentra proporcionalmente menos reclamações
porte_dupla["razao_concentracao"] = (
    porte_dupla["pct_reclamacoes"]
    / porte_dupla["pct_registros"]
).round(2)

print(porte_dupla.to_string(index=False))

print(
    "\nNota: razao_concentracao > 1 indica que o porte concentra "
    "proporcionalmente mais reclamações do que registros na base."
)

# ==================================================================
# 8. DISPERSÃO DO IGR POR OPERADORA (IDENTIFICAÇÃO DE OUTLIERS)
# ==================================================================

# Investiga a distribuição do IGR correto entre todas as operadoras.
# O objetivo é identificar outliers relevantes — operadoras com
# comportamento muito acima do mercado — e estabelecer os percentis
# de referência para classificação nas visualizações.

print("\nDISPERSÃO DO IGR POR OPERADORA")

igr_por_operadora = (
    df.groupby(["registro_ans", "razao_social"])
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

igr_por_operadora["igr_correto"] = (
    igr_por_operadora["total_reclamacoes"]
    / igr_por_operadora["total_beneficiarios"]
    * 1000
)

print("\nEstatísticas descritivas do IGR por operadora:")
print(igr_por_operadora["igr_correto"].describe())

percentis = igr_por_operadora["igr_correto"].quantile(
    [0.75, 0.90, 0.95, 0.99]
)
print("\nPercentis:")
print(percentis)

# Filtro de 10.000 beneficiários: elimina operadoras com base
# muito pequena, cujos índices são matematicamente instáveis
# (1 reclamação em 100 beneficiários → IGR = 10).
p95 = igr_por_operadora["igr_correto"].quantile(0.95)

outliers = (
    igr_por_operadora[
        (igr_por_operadora["igr_correto"] >= p95)
        & (igr_por_operadora["total_beneficiarios"] >= 10000)
    ]
    .sort_values("igr_correto", ascending=False)
)

print(
    f"\nOperadoras acima do P95 (IGR ≥ {p95:.4f}) "
    f"com mínimo de 10k beneficiários:"
)
print(outliers.to_string(index=False))

# ==================================================================
# 9. GRANDES OPERADORAS — IGR vs MERCADO
# ==================================================================

# Compara o IGR correto das maiores operadoras por beneficiários
# contra o IGR médio ponderado do mercado.
# 2026 é excluído do cálculo do mercado por ser ano parcial.

print("\nGRANDES OPERADORAS — IGR vs MERCADO")

df_sem_2026 = df[df["competencia"] < 2026]

igr_mercado = (
    df_sem_2026["qtd_reclamacoes"].sum()
    / df_sem_2026["qtd_beneficiarios"].sum()
    * 1000
)

print(f"\nIGR do mercado (2015–2025): {igr_mercado:.6f}")

top_grandes = (
    igr_por_operadora[
        igr_por_operadora["total_beneficiarios"] >= 100_000_000
    ]
    .sort_values("total_beneficiarios", ascending=False)
    .head(10)
    .copy()
)

top_grandes["vs_mercado"] = (
    top_grandes["igr_correto"] / igr_mercado
).round(2)

top_grandes["classificacao"] = top_grandes["vs_mercado"].apply(
    lambda x: "acima do mercado" if x > 1 else "abaixo do mercado"
)

print("\nTop operadoras por beneficiários vs IGR de mercado:")
print(
    top_grandes[
        [
            "razao_social",
            "total_beneficiarios",
            "total_reclamacoes",
            "igr_correto",
            "vs_mercado",
            "classificacao"
        ]
    ].to_string(index=False)
)

# ==================================================================
# 10. EVOLUÇÃO DO IGR CORRETO POR PORTE AO LONGO DO TEMPO
# ==================================================================

# Investiga se o padrão de maior IGR no grande porte se manteve
# consistente ao longo de toda a série, ou se há variações
# relevantes. Em 2026 o porte médio superou o grande — esse
# comportamento é registrado aqui para acompanhamento.

print("\nEVOLUÇÃO DO IGR CORRETO POR PORTE AO LONGO DO TEMPO")

igr_porte_ano = (
    df.groupby(["competencia", "porte_operadora"])
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)

igr_porte_ano["igr_correto"] = (
    igr_porte_ano["total_reclamacoes"]
    / igr_porte_ano["total_beneficiarios"]
    * 1000
)

igr_porte_ano = igr_porte_ano.sort_values(
    ["competencia", "porte_operadora"]
)

print(igr_porte_ano.to_string(index=False))

# ==================================================================
# FIM
# ==================================================================

print("\n=====================================")
print("EDA COMPLEMENTAR FINALIZADA")
print("=====================================")