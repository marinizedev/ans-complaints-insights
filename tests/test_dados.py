# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Testes de regras de negócio e qualidade dos dados
# ==================================================================

import pytest
import pandas as pd
from unittest.mock import MagicMock
from pathlib import Path
import streamlit as st

# Desativa os decoradores do Streamlit fora do contexto da aplicação
st.cache_data = lambda *args, **kwargs: lambda func: func
st.spinner = MagicMock()

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_LOCAL = BASE_DIR / "data" / "processed" / "igr_processed.csv"

from app.data_loader import CORES


# ==================================================================
# FIXTURE — BASE DE DADOS PARA OS TESTES
# ==================================================================

@pytest.fixture(scope="module")
def df_testes():
    """
    Carrega o dataset processado localmente e adiciona as colunas
    auxiliares para validação das regras de negócio.
    """
    if not ARQUIVO_LOCAL.exists():
        pytest.skip("Arquivo processado não encontrado.")

    df = pd.read_csv(ARQUIVO_LOCAL, sep=",", encoding="utf-8")

    ANOS_PARCIAIS = [2026]
    ANO_PANDEMIA  = 2020

    df["ano_parcial"] = df["competencia"].isin(ANOS_PARCIAIS)
    df["periodo"] = df["competencia"].apply(
        lambda x: "pré-pandemia" if x < ANO_PANDEMIA
        else ("inflexão" if x == ANO_PANDEMIA else "pós-pandemia")
    )
    return df


# ==================================================================
# TESTES
# ==================================================================

def test_cores_essenciais_presentes():
    """Garante que as cores de identidade visual do dashboard estão definidas."""
    for chave in ["primaria", "perigo", "sucesso", "fundo"]:
        assert chave in CORES, f"A cor '{chave}' não encontrada no dicionário."


def test_valores_numericos_positivos(df_testes):
    """Valida que reclamações e beneficiários não possuem valores negativos."""
    assert (df_testes["qtd_reclamacoes"] >= 0).all()
    assert (df_testes["qtd_beneficiarios"] >= 0).all()


def test_flag_ano_parcial(df_testes):
    """Garante que 2026 está corretamente marcado como ano parcial."""
    dados_2026 = df_testes[df_testes["competencia"] == 2026]
    if not dados_2026.empty:
        assert dados_2026["ano_parcial"].all()


def test_classificacao_temporal_pandemia(df_testes):
    """Valida a classificação de períodos em relação à pandemia de 2020."""
    pre = df_testes[df_testes["competencia"] < 2020]
    if not pre.empty:
        assert (pre["periodo"] == "pré-pandemia").all()

    pandemia = df_testes[df_testes["competencia"] == 2020]
    if not pandemia.empty:
        assert (pandemia["periodo"] == "inflexão").all()

    pos = df_testes[df_testes["competencia"] > 2020]
    if not pos.empty:
        assert (pos["periodo"] == "pós-pandemia").all()