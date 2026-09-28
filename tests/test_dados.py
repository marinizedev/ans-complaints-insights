# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Testes de regras de negócio e qualidade dos dados
# ==================================================================

from pathlib import Path
from unittest.mock import MagicMock

import pandas as pd
import pytest
import streamlit as st

# Desativa os decoradores do Streamlit fora do contexto da aplicação.
st.cache_data = lambda *args, **kwargs: lambda func: func
st.spinner = MagicMock()

BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_LOCAL = BASE_DIR / "data" / "processed" / "igr_processed.csv"

from app.data_loader import (  # noqa: E402
    CORES,
    IGR_MULTIPLICADOR,
    assegurar_arquivo_processado,
    calcular_igr,
    igr_por_ano,
)


@pytest.fixture(scope="module")
def df_testes():
    """Carrega o dataset processado e adiciona colunas auxiliares."""
    caminho_dados = assegurar_arquivo_processado()

    if not caminho_dados.exists():
        pytest.skip("Arquivo processado não encontrado.")

    df = pd.read_csv(
        caminho_dados,
        sep=",",
        encoding="utf-8",
        low_memory=False,
    )

    df["ano_parcial"] = df["competencia"].isin([2026])
    df["periodo"] = df["competencia"].apply(
        lambda x: "pré-pandemia"
        if x < 2020
        else ("inflexão" if x == 2020 else "pós-pandemia")
    )
    return df


def test_cores_essenciais_presentes():
    """Garante que as cores de identidade visual estão definidas."""
    for chave in ["primaria", "perigo", "sucesso", "fundo"]:
        assert chave in CORES, f"A cor '{chave}' não encontrada."


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
    """Valida a classificação dos períodos em relação a 2020."""
    pre = df_testes[df_testes["competencia"] < 2020]
    pandemia = df_testes[df_testes["competencia"] == 2020]
    pos = df_testes[df_testes["competencia"] > 2020]

    if not pre.empty:
        assert (pre["periodo"] == "pré-pandemia").all()
    if not pandemia.empty:
        assert (pandemia["periodo"] == "inflexão").all()
    if not pos.empty:
        assert (pos["periodo"] == "pós-pandemia").all()


def test_igr_usa_unidade_oficial_da_ans():
    """O IGR deve ser expresso por 100.000 beneficiários."""
    assert IGR_MULTIPLICADOR == 100_000
    assert calcular_igr(630, 822_883) == pytest.approx(76.560094)


def test_igr_agregado_eh_ponderado_pela_carteira():
    """A agregação usa soma de reclamações/soma de beneficiários."""
    df = pd.DataFrame(
        {
            "competencia": [2024, 2024],
            "ano_parcial": [False, False],
            "periodo": ["pós-pandemia", "pós-pandemia"],
            "qtd_reclamacoes": [1, 2],
            "qtd_beneficiarios": [10, 10_000],
        }
    )

    resultado = igr_por_ano(df).iloc[0]
    esperado = (1 + 2) / (10 + 10_000) * 100_000

    assert resultado["igr_correto"] == pytest.approx(esperado)
    assert resultado["igr_correto"] != pytest.approx((100_000 / 10 + 20) / 2)


def test_coluna_igr_da_base_confirma_escala_oficial(df_testes):
    """A coluna IGR da fonte deve coincidir com a fórmula por 100.000."""
    amostra = df_testes[df_testes["qtd_reclamacoes"] > 0].head(1000)
    esperado = (
        amostra["qtd_reclamacoes"]
        / amostra["qtd_beneficiarios"]
        * IGR_MULTIPLICADOR
    )
    pd.testing.assert_series_equal(
        amostra["igr"].reset_index(drop=True),
        esperado.round(2).reset_index(drop=True),
        check_names=False,
        check_exact=False,
        rtol=0,
        atol=0.01,
    )
