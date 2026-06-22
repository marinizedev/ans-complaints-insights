# Investigação Inicial — IGR (Índice Geral de Reclamações)

## Objetivo

Realizar o entendimento inicial da base de dados antes de qualquer tratamento, transformação ou análise exploratória.

---

## Resumo da Base

- Linhas: 151.501
- Colunas: 10
- Operadoras únicas: 1.411
- Coberturas: 2 categorias
- Período coberto: 2015 a 2026

---

## Colunas Disponíveis

- REGISTRO_ANS
- RAZAO_SOCIAL
- COBERTURA
- IGR
- QTD_RECLAMACOES
- QTD_BENEFICIARIO
- PORTE_OPERADORA
- COMPETENCIA
- COMPETENCIA_BENEFICIARIO
- DT_ATUALIZACAO

---

## Qualidade dos Dados

### Valores Nulos

Apenas uma coluna apresenta valores nulos:

| Coluna          | Valores nulos |
|-----------------|---------------|
| DT_ATUALIZACAO  | 62.119        |

Observação:

O próprio dicionário da ANS informa que campos sem data indicam bases congeladas ou não atualizadas.

Portanto, os valores nulos aparentam ser esperados.

---

## Distribuição por Cobertura

| Cobertura                   | Quantidade |
|-----------------------------|------------|
| Assistência médica          | 100.352    |
| Exclusivamente odontológica | 51.149     |

---

## Distribuição por Porte

| Porte   | Quantidade |
|---------|------------|
| Pequeno | 96.391     |
| Médio   | 40.120     |
| Grande  | 14.990     |

Observação:

A maior parte dos registros pertence a operadoras de pequeno porte.

---

## Descobertas Importantes

### Competência

Apesar de o dicionário informar que COMPETENCIA e COMPETENCIA_BENEFICIARIO representam mês/ano, os dados disponíveis apresentam apenas o ano.

Valores encontrados:

2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 e 2026.

Essa inconsistência deve ser registrada para futuras análises.

---

## IGR

A coluna IGR foi carregada como texto.

Será necessário investigar:

- separador decimal utilizado;
- possibilidade de conversão para numérico;
- existência de valores inválidos.

---

## Próximos Passos

1. Investigar a coluna IGR.
2. Validar possíveis duplicidades.
3. Identificar evolução temporal das reclamações.
4. Construir perguntas de negócio.
5. Iniciar análise exploratória.
