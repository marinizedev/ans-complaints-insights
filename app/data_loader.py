# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Carregamento e preparo dos dados
#
# Lê o CSV já processado (data/processed/igr_processed.csv) e
# adiciona as colunas auxiliares para as visualizações.
#
# O processamento bruto (limpeza, tipos, padronização) é
# responsabilidade do src/process_igr.py, que gera o CSV processado.
# Este módulo apenas consome o resultado já pronto.
# ==================================================================

import pandas as pd
from pathlib import Path
import streamlit as st

# ==================================================================
# CONSTANTES
# ==================================================================

BASE_DIR = Path(__file__).resolve().parents[1]

ARQUIVO_PROCESSADO = (
    BASE_DIR / "data" / "processed" / "igr_processed.csv"
)

ANOS_PARCIAIS = [2026]
IGR_MERCADO   = 0.201619
ANO_PANDEMIA  = 2020

CORES = {
    "primaria":    "#2dd4a0",   # teal — cor de identidade
    "perigo":      "#ff6b6b",   # vermelho coral — alertas
    "sucesso":     "#2dd4a0",   # teal — métricas positivas
    "atencao":     "#ffb060",   # âmbar — atenção
    "pre":         "#1a3028",   # barra pré-pandemia
    "pos":         "#25b088",   # barra pós-pandemia
    "neutro":      "#2a4a3a",   # elementos neutros
    "texto":       "#e0f0ea",
    "texto_muted": "#4a8a70",
    "fundo":       "#0a0e14",
    "card":        "#0f1a16",
    "borda":       "#1a3028",
}

# ==================================================================
# CARREGAMENTO PRINCIPAL
# ==================================================================

@st.cache_data(show_spinner="Carregando dados da ANS...")
def carregar_dados() -> pd.DataFrame:
    """
    Lê o CSV processado e adiciona colunas auxiliares para
    as visualizações do dashboard.

    Separação de responsabilidades:
    - src/process_igr.py  → gera o CSV processado a partir do bruto
    - app/data_loader.py  → consome o CSV processado e prepara o dashboard
    """
    df = pd.read_csv(
        ARQUIVO_PROCESSADO,
        sep=",",
        encoding="utf-8",
        low_memory=False
    )

    # Flag de ano parcial — 2026 ainda não tem dados completos
    df["ano_parcial"] = df["competencia"].isin(ANOS_PARCIAIS)

    # Classificação temporal em relação à pandemia de 2020
    df["periodo"] = df["competencia"].apply(
        lambda x: "pré-pandemia" if x < ANO_PANDEMIA
        else ("inflexão" if x == ANO_PANDEMIA else "pós-pandemia")
    )

    return df


# ==================================================================
# AGREGAÇÕES PRONTAS PARA AS PÁGINAS
# ==================================================================

@st.cache_data(show_spinner=False)
def igr_por_ano(df: pd.DataFrame) -> pd.DataFrame:
    """IGR correto agregado por ano, com flag de ano parcial."""
    resultado = (
        df.groupby(["competencia", "ano_parcial", "periodo"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado["variacao_pct"] = (
        resultado["total_reclamacoes"].pct_change() * 100
    ).round(1)
    return resultado.sort_values("competencia")


@st.cache_data(show_spinner=False)
def igr_por_porte(df: pd.DataFrame) -> pd.DataFrame:
    """IGR correto por porte com razão de concentração."""
    total_registros   = len(df)
    total_reclamacoes = df["qtd_reclamacoes"].sum()

    resultado = (
        df.groupby("porte_operadora")
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum"),
            registros=("registro_ans", "count"),
            operadoras_unicas=("registro_ans", "nunique")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado["pct_registros"] = (
        resultado["registros"] / total_registros * 100
    ).round(2)
    resultado["pct_reclamacoes"] = (
        resultado["total_reclamacoes"] / total_reclamacoes * 100
    ).round(2)
    resultado["razao_concentracao"] = (
        resultado["pct_reclamacoes"] / resultado["pct_registros"]
    ).round(2)

    ordem = {"Grande": 0, "Médio": 1, "Pequeno": 2}
    resultado["ordem"] = resultado["porte_operadora"].map(ordem)
    return resultado.sort_values("ordem").drop(columns="ordem")


@st.cache_data(show_spinner=False)
def igr_porte_por_ano(df: pd.DataFrame) -> pd.DataFrame:
    """IGR correto por porte ao longo do tempo."""
    resultado = (
        df.groupby(["competencia", "porte_operadora"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    return resultado.sort_values(["competencia", "porte_operadora"])


@st.cache_data(show_spinner=False)
def igr_por_cobertura(df: pd.DataFrame) -> pd.DataFrame:
    """IGR correto por cobertura com participação percentual."""
    total = df["qtd_reclamacoes"].sum()
    resultado = (
        df.groupby("cobertura")
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado["percentual"] = (
        resultado["total_reclamacoes"] / total * 100
    ).round(2)
    return resultado


@st.cache_data(show_spinner=False)
def cobertura_por_ano(df: pd.DataFrame) -> pd.DataFrame:
    """Evolução das coberturas ao longo do tempo."""
    total_por_ano = (
        df.groupby("competencia")["qtd_reclamacoes"]
        .sum()
        .reset_index()
        .rename(columns={"qtd_reclamacoes": "total_ano"})
    )
    resultado = (
        df.groupby(["competencia", "cobertura"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado = resultado.merge(total_por_ano, on="competencia")
    resultado["percentual"] = (
        resultado["total_reclamacoes"] / resultado["total_ano"] * 100
    ).round(2)
    return resultado.sort_values(["competencia", "cobertura"])


@st.cache_data(show_spinner=False)
def ranking_operadoras(
    df: pd.DataFrame,
    min_beneficiarios: int = 10_000
) -> pd.DataFrame:
    """Ranking por IGR correto com filtro mínimo de beneficiários."""
    resultado = (
        df.groupby(["registro_ans", "razao_social"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado["vs_mercado"] = (
        resultado["igr_correto"] / IGR_MERCADO
    ).round(2)
    resultado["em_falencia"] = resultado["razao_social"].str.contains(
        "FALIDA|LIQUIDAÇÃO|INSOLVÊNCIA|RECUPERAÇÃO JUDICIAL",
        case=False, na=False
    )
    return resultado[
        resultado["total_beneficiarios"] >= min_beneficiarios
    ].sort_values("igr_correto", ascending=False).reset_index(drop=True)


@st.cache_data(show_spinner=False)
def top_por_volume(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Top N operadoras por volume absoluto de reclamações."""
    resultado = (
        df.groupby(["registro_ans", "razao_social"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    resultado["vs_mercado"] = (
        resultado["igr_correto"] / IGR_MERCADO
    ).round(2)
    return resultado.sort_values(
        "total_reclamacoes", ascending=False
    ).head(n).reset_index(drop=True)


@st.cache_data(show_spinner=False)
def operadoras_falidas(df: pd.DataFrame) -> pd.DataFrame:
    """Operadoras em falência, liquidação ou insolvência."""
    falidas = df[
        df["razao_social"].str.contains(
            "FALIDA|LIQUIDAÇÃO|INSOLVÊNCIA|RECUPERAÇÃO JUDICIAL",
            case=False, na=False
        )
    ]
    resultado = (
        falidas.groupby(["registro_ans", "razao_social"])
        .agg(
            total_reclamacoes=("qtd_reclamacoes", "sum"),
            total_beneficiarios=("qtd_beneficiarios", "sum")
        )
        .reset_index()
    )
    resultado["igr_correto"] = (
        resultado["total_reclamacoes"]
        / resultado["total_beneficiarios"]
        * 1000
    )
    return resultado.sort_values(
        "total_reclamacoes", ascending=False
    ).reset_index(drop=True)


@st.cache_data(show_spinner=False)
def falidas_por_ano(df: pd.DataFrame) -> pd.DataFrame:
    """Reclamações de operadoras falidas ao longo do tempo."""
    falidas = df[
        df["razao_social"].str.contains(
            "FALIDA|LIQUIDAÇÃO|INSOLVÊNCIA|RECUPERAÇÃO JUDICIAL",
            case=False, na=False
        )
    ]
    return (
        falidas.groupby("competencia")["qtd_reclamacoes"]
        .sum()
        .reset_index()
        .rename(columns={"qtd_reclamacoes": "total_reclamacoes"})
        .sort_values("competencia")
    )