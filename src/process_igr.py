# ========================================================
# ANS COMPLAINTS INSIGHTS

# ETAPA 2 — PROCESSAMENTO DOS DADOS

# Objetivo: Padronizar e preparar o dataset para análise.

# Entrada: data/raw/igr.csv

# Saída: data/processed/igr_processed.csv
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
# 2. CARREGAR ARQUIVO
# =======================================================

print("\nCarregando arquivo...")

df = pd.read_csv(
    RAW_FILE,
    sep=";",
    encoding="utf-8",
    low_memory=False
)

print("Arquivo carregado com sucesso!")

# =======================================================
# 3. PADRONIZAR NOMES DAS COLUNAS
# =======================================================

print("\nPadronizando nomes das colunas...")

df.columns = (
    df.columns
    .str.lower()
    .str.strip()
)

# =======================================================
# 4. CONVERTER IGR
# =======================================================

print("Convertendo coluna igr...")

df["igr"] = (
    df["igr"]
    .astype(str)
    .str.replace(",", ".", regex=False)
)

df["igr"] = pd.to_numeric(
    df["igr"],
    errors="coerce"
)

# =======================================================
# 5. CONVERTER CAMPOS NUMÉRICOS
# =======================================================

colunas_numericas = [
    "qtd_reclamacoes",
    "qtd_beneficiarios",
    "competencia",
    "competencia_beneficiario"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

# =======================================================
# 6. TRATAR DT_ATUALIZACAO
# =======================================================

print("Convertendo datas...")

df["dt_atualizacao"] = pd.to_datetime(
    df["dt_atualizacao"],
    errors="coerce"
)

# =======================================================
# 7. VALIDAR RESULTADO
# =======================================================

print("\nResumo após processamento:")

print(df.info())

# =======================================================
# 8. SALVAR ARQUIVO PROCESSSADO
# =======================================================

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_FILE, index=False)

print("\nArquivo salvo com sucesso!")

print(PROCESSED_FILE)

# =======================================================
# FIM 
# =======================================================