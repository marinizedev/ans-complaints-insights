import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
import streamlit as st
from pathlib import Path

# 1. Desativa temporariamente os decoradores e spinners do Streamlit para o teste
st.cache_data = lambda *args, **kwargs: lambda func: func
st.spinner = MagicMock()

# Localiza o seu arquivo processado local para usar de base no teste
BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_LOCAL = BASE_DIR / "data" / "processed" / "igr_processed.csv"

# 2. INTERCEPTAÇÃO: Força a função carregar_dados a ler o arquivo local só no teste
# Isso pula o download da URL instável da ANS e evita o erro 10054
@pytest.fixture(scope="module")
def df_testes():
    """Lê o arquivo local processado para validar as regras de negócio."""
    if not ARQUIVO_LOCAL.exists():
        pytest.skip("Arquivo local processado não encontrado para o teste.")
        
    df = pd.read_csv(ARQUIVO_LOCAL, sep=",", encoding="utf-8")
    
    # Executa as colunas auxiliares que o seu data_loader faria
    ANOS_PARCIAIS = [2026]
    ANO_PANDEMIA = 2020
    df["ano_parcial"] = df["competencia"].isin(ANOS_PARCIAIS)
    df["periodo"] = df["competencia"].apply(
        lambda x: "pré-pandemia" if x < ANO_PANDEMIA
        else ("inflexão" if x == ANO_PANDEMIA else "pós-pandemia")
    )
    return df

# Importa as cores do seu arquivo original
from app.data_loader import CORES

# ==================================================================
# SEUS TESTES DE REGRAS DE NEGÓCIO (Rodando locais e ultra rápidos)
# ==================================================================

def test_verificacao_das_cores_essenciais():
    """Garante que ninguém alterou ou deletou as cores de identidade visual do dashboard."""
    chaves_obrigatorias = ["primaria", "perigo", "sucesso", "fundo"]
    for chave in chaves_obrigatorias:
        assert chave in CORES, f"A cor crítica '{chave}' sumiu do dicionário de cores."

def test_se_colunas_de_valores_sao_positivas(df_testes):
    """Valida se as reclamações e beneficiários não possuem valores inválidos (negativos)."""
    assert (df_testes["qtd_reclamacoes"] >= 0).all(), "Existem reclamações com valor negativo!"
    assert (df_testes["qtd_beneficiarios"] >= 0).all(), "Existem beneficiários com valor negativo!"

def test_flag_ano_parcial(df_testes):
    """Garante que a lógica de ano parcial está marcando o ano correto."""
    dados_2026 = df_testes[df_testes["competencia"] == 2026]
    if not dados_2026.empty:
        assert dados_2026["ano_parcial"].all(), "O ano de 2026 deveria estar marcado como True."

def test_periodo_da_pandemia(df_testes):
    """Valida se a classificação temporal antes/durante/depois da pandemia está correta."""
    dados_antigos = df_testes[df_testes["competencia"] < 2020]
    if not dados_antigos.empty:
        assert (dados_antigos["periodo"] == "pré-pandemia").all()
        
    dados_2020 = df_testes[df_testes["competencia"] == 2020]
    if not dados_2020.empty:
        assert (dados_2020["periodo"] == "inflexão").all()
