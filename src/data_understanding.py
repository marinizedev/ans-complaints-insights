# ==================================================================
# ANS COMPLAINTS INSIGHTS

# ETAPA 1 — DATA UNDERSTANDING

# Objetivo: Entender completamente a estrutura do arquivo antes
# de iniciar qualquer tratamento ou análise.

# ==================================================================

import pandas as pd
from pathlib import Path
from datetime import datetime

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

print("\nVALORES NULOS POR COLUNA")

nulos = df.isnull().sum()

print(nulos)

# ==================================================================
# 6. MEMÓRIA UTILIZADA
# ==================================================================

print("\nMEMÓRIA UTILIZADA")

memoria_mb = (df.memory_usage(deep=True).sum() / 1024**2)

print(f"{memoria_mb:.2f} MB")

# ==================================================================
# 7. QUANTIDADE DE OPERADORAS
# ==================================================================

print("\nOPERADORAS")

qtd_operadoras = df["REGISTRO_ANS"].nunique()

print(f"Operadoras únicas: {qtd_operadoras}")

# =================================================================
# VARIÁVEIS REUTILIZÁVEIS
# =================================================================

coberturas = (
    df["COBERTURA"]
    .value_counts(dropna=False)
)

portes = (
    df["PORTE_OPERADORA"]
    .value_counts(dropna=False)
)

periodo = sorted(
    df["COMPETENCIA"]
    .dropna()
    .unique()
)

# ==================================================================
# 8. COBERTURAS EXISTENTES
# ==================================================================

print("\nTIPOS DE COBERTURA")

print(coberturas)

# ==================================================================
# 9. PORTE DAS OPERADORAS
# ==================================================================

print("\nPORTE DAS OPERADORAS")

print(portes)

# ==================================================================
# 10. COMPETÊNCIA
# ==================================================================

print("\nPERÍODO COBERTO")

print(periodo)

# ==================================================================
# 11. AMOSTRA DOS DADOS
# ==================================================================

print("\nPRIMEIROS REGISTROS")

print(df.head())

# ==================================================================
# 12. ESTATÍSTICAS BÁSICAS
# ==================================================================

print("\nESTATÍSTICAS NUMÉRICAS")

print(df.describe())

print("\n==============================")
print("DATA UNDERSTANDING FINALIZADO")
print("==============================")

# ==================================================================
# 13. GERAR RELATÓRIO AUTOMÁTICO
# ==================================================================

print("\nGerando relatório automático...")

data_execucao = datetime.now()

relatorio_path = (
    BASE_DIR
    / "docs"
    / "data_understanding_report.md"
)

relatorio = f"""
# Data Understanding Report

Gerado em: {data_execucao}

---

## Arquivo Analisado

{arquivo.name}

---

## Estrutura

- Registros: {linhas:,}
- Colunas: {colunas}
- Operadoras únicas: {qtd_operadoras}

---

## Memória

- Consumo: {memoria_mb:.2f} MB

---

## Coberturas

{coberturas.to_markdown()}

---

## Porte das Operadoras

{portes.to_markdown()}

---

## Valores Nulos

{nulos.to_frame(name="Quantidade").to_markdown()}

---

## Período Coberto

{periodo}
"""

with open(
    relatorio_path,
    "w",
    encoding="utf-8"
) as arquivo_md:
    arquivo_md.write(relatorio)

print(f"\nRelatório gerado com sucesso:\n{relatorio_path}")