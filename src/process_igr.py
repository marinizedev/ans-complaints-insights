# ========================================================
# ANS COMPLAINTS INSIGHTS
# ETAPA 2 — PROCESSAMENTO DOS DADOS
# Objetivo: Padronizar e preparar o dataset para análise.
# ========================================================

import pandas as pd
from pathlib import Path

# =======================================================
# 1. LOCALIZAR DIRETÓRIOS
# =======================================================
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw" / "igr.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_FILE = PROCESSED_DIR / "igr_processed.csv"


# =======================================================
# 2. FUNÇÃO CORE DE PROCESSAMENTO (Para uso do Streamlit e Testes)
# =======================================================
def processar_dataframe_igr(df_bruto: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe um DataFrame bruto do IGR da ANS e aplica todas as regras 
    de padronização, limpeza e conversão de tipos de dados.
    """
    # Cria uma cópia para evitar warnings de cópia oculta (SettingWithCopyWarning)
    df = df_bruto.copy()

    # Padronizar nomes das colunas
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    # Converter IGR (Corrige vírgulas decimais para o padrão do Python)
    if "igr" in df.columns:
        df["igr"] = (
            df["igr"]
            .astype(str)
            .str.replace(",", ".", regex=False)
        )
        df["igr"] = pd.to_numeric(
            df["igr"],
            errors="coerce"
        )

    # Converter campos numéricos
    colunas_numericas = [
        "qtd_reclamacoes",
        "qtd_beneficiarios",
        "competencia",
        "competencia_beneficiario"
    ]
    for coluna in colunas_numericas:
        if coluna in df.columns:
            df[coluna] = pd.to_numeric(
                df[coluna],
                errors="coerce"
            )

    # Tratar DT_ATUALIZACAO
    if "dt_atualizacao" in df.columns:
        df["dt_atualizacao"] = pd.to_datetime(
            df["dt_atualizacao"],
            errors="coerce"
        )

    return df


# =======================================================
# 3. EXECUÇÃO SCRIPT LOCAL 
# =======================================================
if __name__ == "__main__":
    print("\n[Execução Local] Carregando arquivo bruto...")

    # Se rodar o script diretamente no terminal, ele lê o arquivo local data/raw/
    if not RAW_FILE.exists():
        print(f"Erro: Arquivo bruto não encontrado em: {RAW_FILE}")
    else:
        # Lendo com iso-8859-1 que é o padrão original dos arquivos da ANS
        df_raw = pd.read_csv(
            RAW_FILE,
            sep=";",
            encoding="iso-8859-1",
            low_memory=False
        )
        print("Arquivo bruto carregado com sucesso!")

        print("\nProcessando os dados através da função...")
        df_processed = processar_dataframe_igr(df_raw)

        print("\nResumo após processamento:")
        print(df_processed.info())

        # Salvar o arquivo processado localmente
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        df_processed.to_csv(PROCESSED_FILE, index=False, encoding="utf-8")

        print("\nArquivo salvo localmente com sucesso em UTF-8!")
        print(PROCESSED_FILE)
