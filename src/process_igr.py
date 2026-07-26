# ========================================================
# ANS COMPLAINTS INSIGHTS
# ETAPA 2 — PROCESSAMENTO DOS DADOS
# Objetivo: Padronizar e preparar o dataset para análise.
# ========================================================

import pandas as pd
from pathlib import Path
import logging

# Configuração do Logger Profissional
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
logger = logging.getLogger("process_igr")

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
    logger.info("Iniciando o processamento do DataFrame bruto do IGR...")
    try:
        # Cria uma cópia para evitar warnings de cópia oculta (SettingWithCopyWarning)
        df = df_bruto.copy()

        # Padronizar nomes das colunas
        logger.info("Padronizando os nomes de colunas para minúsculo...")
        df.columns = (
            df.columns
            .str.lower()
            .str.strip()
        )

        # Converter IGR (Corrige vírgulas decimais para o padrão do Python)
        if "igr" in df.columns:
            logger.info("Convertendo coluna 'igr' de string/vírgula para numérico...")
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
        logger.info("Convertendo colunas de contagem e datas de competência para numérico...")
        for coluna in colunas_numericas:
            if coluna in df.columns:
                df[coluna] = pd.to_numeric(
                    df[coluna],
                    errors="coerce"
                )

        # Tratar DT_ATUALIZACAO
        if "dt_atualizacao" in df.columns:
            logger.info("Tratando e formatando coluna de data de atualização (dt_atualizacao)...")
            df["dt_atualizacao"] = pd.to_datetime(
                df["dt_atualizacao"],
                errors="coerce"
            )

        logger.info("Processamento do DataFrame bruto finalizado com sucesso!")
        return df

    except Exception as e:
        logger.error(f"Erro inesperado durante processamento do DataFrame do IGR: {e}", exc_info=True)
        raise e


# =======================================================
# 3. EXECUÇÃO SCRIPT LOCAL 
# =======================================================
if __name__ == "__main__":
    logger.info("[Execução Local] Carregando arquivo bruto...")

    # Se rodar o script diretamente no terminal, ele lê o arquivo local data/raw/
    if not RAW_FILE.exists():
        logger.error(f"Erro crítico: Arquivo bruto não encontrado em: {RAW_FILE}")
    else:
        try:
            df_raw = pd.read_csv(
                RAW_FILE,
                sep=";",
                encoding="utf-8",
                low_memory=False
            )
            logger.info("Arquivo bruto carregado com sucesso!")
        except Exception as e:
            logger.exception(f"Falha ao carregar o arquivo bruto em {RAW_FILE}: {e}")
            raise e

        try:
            logger.info("Processando os dados através da função de processamento...")
            df_processed = processar_dataframe_igr(df_raw)
        except Exception as e:
            logger.exception(f"Falha ao processar os dados do IGR: {e}")
            raise e

        logger.info("Resumo após processamento:")
        df_processed.info()

        # Salvar o arquivo processado localmente
        try:
            logger.info(f"Salvando o arquivo processado em: {PROCESSED_FILE}")
            PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
            df_processed.to_csv(PROCESSED_FILE, index=False, encoding="utf-8")
            logger.info("Arquivo salvo localmente com sucesso em UTF-8!")
        except Exception as e:
            logger.exception(f"Falha ao salvar o arquivo processado em {PROCESSED_FILE}: {e}")
            raise e
