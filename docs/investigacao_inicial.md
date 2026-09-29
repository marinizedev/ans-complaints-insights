# Investigação Inicial — IGR (Índice Geral de Reclamações)

## Objetivo

Realizar o entendimento inicial da base antes das análises exploratórias,
identificar possíveis inconsistências, oportunidades analíticas e hipóteses
de investigação.

---

## Contexto

O dataset disponibilizado pela ANS contém informações relacionadas ao
Índice Geral de Reclamações (IGR) das operadoras de planos de saúde
brasileiras.

A base reúne informações de reclamações, beneficiários, cobertura e porte
das operadoras, cobrindo o período de 2015 a 2026.

---

## Descobertas importantes

### Competência e discrepância entre dicionário e arquivo recebido

O dicionário de dados da ANS, datado de outubro de 2023, descreve:

- `COMPETENCIA`;

- `COMPETENCIA_BENEFICIARIO`.

Ambos são definidos como campos numéricos de tamanho 6, referentes a ano e
mês de competência (`YYYYMM`).

Entretanto, a verificação feita no arquivo bruto recebido da fonte encontrou
somente valores com quatro dígitos:

```
COMPETENCIA:               12 valores únicos, todos com 4 dígitos
COMPETENCIA_BENEFICIARIO:  12 valores únicos, todos com 4 dígitos
```

Exemplos observados:

```
2015, 2016, 2017, ..., 2026
```

Essa redução já está presente no arquivo de origem analisado. Não há evidência
de que o ETL tenha removido o mês: o `src/process_igr.py` apenas converte os
campos para numérico e preserva os valores recebidos.

A base possui, porém, múltiplas observações para a mesma combinação de
operadora, cobertura e ano. A investigação encontrou:

- 151.501 registros;

- 13.666 combinações de operadora, cobertura e ano;

- 11.754 combinações com exatamente 12 linhas;

- 141.048 registros pertencentes a esses grupos de 12 linhas;

- grupos com cinco linhas predominantes em 2026.

Nas combinações com 12 linhas, `qtd_reclamacoes`, `qtd_beneficiarios` e `igr`
variam entre os registros. Isso é compatível com observações mensais, mas o
mês exato não pode ser identificado porque a fonte não o informa no arquivo.

A interpretação adotada é, portanto:

> A base contém múltiplas observações aparentemente mensais por operadora,
cobertura e ano, mas sem identificador explícito do mês. A periodicidade mensal
é inferida pela estrutura dos registros, não confirmada por uma coluna mensal.

Não foram removidas as linhas repetidas. Sem o mês, duas observações de meses
diferentes podem ter exatamente os mesmos valores e parecer duplicatas.

---

### DT_ATUALIZACAO

O dicionário da ANS informa que registros sem data podem indicar bases
congeladas.

A ausência de valores nessa coluna (62.119 registros) é, portanto, esperada e
não representa necessariamente problema de qualidade dos dados.

---

### IGR — descoberta crítica

> Esta foi a descoberta mais importante da fase de investigação.

Durante a carga inicial, a coluna IGR foi identificada como texto e convertida
para numérico com sucesso.

Entretanto, ao realizar a EDA principal, o cálculo de IGR médio por ano
através de `df.groupby("competencia")["igr"].mean()` produziu valores
inadequados para representar o índice agregado:

| Ano | IGR médio simples |
| --- | --- |
| 2018 | 25,54 |
| 2019 | 130,75 |
| 2021 | 175,12 |
| 2022 | **357,12** |

A coluna `IGR` do dataset já contém o índice calculado pela ANS para cada
observação individual. Não é um campo bruto — é um campo derivado.

A fórmula oficial usa a referência de 100.000 beneficiários:

```
IGR = (QTD_RECLAMACOES / QTD_BENEFICIARIOS) × 100.000
```

Ao calcular a média aritmética do IGR entre operadoras, cada observação recebe
o mesmo peso, independentemente do tamanho da carteira. O resultado pode ser
matematicamente válido como média entre observações, mas é inadequado como IGR
agregado do mercado.

#### Exemplo do problema

```
Operadora A: 1 reclamação / 10 beneficiários       → IGR = 10.000,0
Operadora B: 2 reclamações / 10.000 beneficiários  → IGR = 20

Média simples:  (10.000,0 + 20,0) / 2 = 5.010,0  ← número distorcido
IGR agregado:  3 / 10.010 × 100.000 = 29,97      ← número ponderado
```

#### Solução adotada

Recalcular o IGR agregando numerador e denominador separadamente antes de
aplicar a fórmula:

```python
igr_correto = (
    df.groupby("competencia")
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
)

igr_correto["igr"] = (
    igr_correto["total_reclamacoes"]
    / igr_correto["total_beneficiarios"]
    * 100_000
)
```

Para anos completos, essa razão equivale à razão entre as médias mensais
quando as observações mensais disponíveis representam o mesmo conjunto de
períodos no numerador e no denominador. Como os meses não são informados pela
fonte, o projeto não cria artificialmente uma sequência mensal.

#### Comparativo após correção

| Ano | IGR médio simples | IGR agregado |
| --- | --- | --- |
| 2015 | 91,85 | 10,739 |
| 2018 | 25,54 | 10,657 |
| 2019 | 130,75 | 14,511 |
| 2021 | 175,12 | 19,534 |
| 2022 | 357,12 | 23,325 |
| 2024 | 141,53 | 35,211 |

A tendência real é diferente da oscilação produzida pela média simples e deve
ser interpretada com a ressalva de granularidade descrita nesta investigação.

---

### 2026 — ano parcial

O ano de 2026 está presente na base com dados incompletos:

- total de reclamações: 142.039, contra 359.162 em 2024;

- total de beneficiários: aproximadamente 443 milhões, contra 1,02 bilhão em 2024;

- operadoras únicas: 897, contra 935 em 2024;

- cinco observações aparecem na maior parte dos grupos de operadora e cobertura.

Como o arquivo não informa o mês, não é possível afirmar quais cinco meses estão
representados. Todas as análises e visualizações que incluem 2026 devem
sinalizá-lo como ano parcial.

---

## Hipóteses iniciais

Levantadas antes da EDA. Para hipóteses revisadas com dados reais, consultar
`hypotheses.md`.

- Operadoras de pequeno porte podem apresentar comportamento diferente das
grandes operadoras.

- Assistência médica pode apresentar volume de reclamações superior à
odontológica.

- O crescimento das reclamações pode não acompanhar o crescimento dos
beneficiários.

- Existem operadoras que podem concentrar parte relevante das reclamações do
setor.

---

## Próximos passos

1. ~~Explorar comportamento temporal das reclamações.~~ ✅ Concluído

1. ~~Avaliar distribuição do IGR.~~ ✅ Concluído na EDA complementar

1. ~~Investigar operadoras com maiores índices.~~ ✅ Concluído

1. ~~Construir análises para responder às perguntas de negócio.~~ ✅ Concluído

1. ~~Construir visualizações no Streamlit com dados corrigidos.~~ ✅ Concluído

1. ~~Produzir narrativa de Data Storytelling.~~ ✅ Concluído

1. Obter, se possível, uma versão da fonte que preserve `YYYYMM` para auditar
a completude mensal e a correspondência entre competências de reclamações e
beneficiários.
