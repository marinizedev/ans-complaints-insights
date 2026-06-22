# ==================================================================
# ANS COMPLAINTS INSIGHTS

# ETAPA 1 — DATA UNDERSTANDING

# Objetivo: Entender completamente a estrutura do arquivo antes
# de iniciar qualquer tratamento ou análise.

# ==================================================================

import pandas as pd
from pathlib import Path

# ==================================================================
# 1. CARREGAR O ARQUIVO
# ==================================================================

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[1]

# Caminho do arquivo
arquivo = BASE_DIR / "data" / "raw" / "igr.csv"

print("BASE_DIR:")
print(BASE_DIR)

print("\nARQUIVO:")
print(arquivo)

df = pd.read_csv(
    arquivo, 
    sep=";",
    encoding="utf-8")

print("\n=============================")
print("ARQUIVO CARREGADO COM SUCESSO")
print("=============================\n")

# ==================================================================
# 2. TAMANHO DO DATASET
# ==================================================================

linhas, colunas = df.shape

print("TAMANHO DO DATASET")
print(f"Linhas: {linhas:,}")
print(f"colunas: {colunas}")

# ==================================================================
# 3. NOMES DAS COLUNAS
# ==================================================================

print("COLUNAS DISPONÍVEIS")
print(df.columns.tolist())

# ==================================================================
# 4. TIPOS DE DADOS
# ==================================================================

print("TIPOS DAS COLUNAS")
print(df.dtypes)

# ==================================================================
# 5. VALORES NULOS
# ==================================================================

print("VALORES NULOS POR COLUNA")

nulos = df.isnull().sum()

print(nulos)

# ==================================================================
# 6. MEMÓRIA UTILIZADA
# ==================================================================

print("MEMÓRIA UTILIZADA")
memoria_mb = (df.memory_usage(deep=True).sum() / 1024**2)

print(f"{memoria_mb:.2f} MB")

# ==================================================================
# 7. QUANTIDADE DE OPERADORAS
# ==================================================================

print("OPERADORAS")

qtd_operadoras = df["REGISTRO_ANS"].nunique()

print(f"Operadoras únicas: {qtd_operadoras}")

# ==================================================================
# 8. COBERTURAS EXISTENTES
# ==================================================================

print("TIPOS DE COBERTURA")

print(df["COBERTURA"].value_counts(dropna=False))

# ==================================================================
# 9. PORTE DAS OPERADORAS
# ==================================================================

print("PORTE DAS OPERADORAS")

print(df["PORTE_OPERADORA"].value_counts(dropna=False))

# ==================================================================
# 10. COMPETÊNCIA
# ==================================================================

print("PERÍODO COBERTO")

print(
    sorted(
        df["COMPETENCIA"]
        .dropna()
        .unique()
    )
)

# ==================================================================
# 11. AMOSTRA DOS DADOS
# ==================================================================

print("PRIMEIROS REGISTROS")

print(df.head())

# ==================================================================
# 12. ESTATÍSTICAS BÁSICAS
# ==================================================================

print("ESTATÍSTICAS NUMÉRICAS")

print(df.describe())

print("\n==============================")
print("DATA UNDERSTANDING FINALIZADO")
print("==============================")