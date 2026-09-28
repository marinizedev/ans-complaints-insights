# Insights — ANS Complaints Insights

> Todos os valores de IGR foram calculados pelo método correto:
> ponderação pela carteira de beneficiários.
> Para entender a metodologia adotada, consultar `investigacao_inicial.md`.

---

## Estrutura do Dataset

- Total de registros: 151.501
- Total de colunas: 10
- Total de operadoras únicas: 1.411
- Período coberto: 2015 a 2026 (2026 parcial)

---

## Cobertura dos Planos

| Cobertura                   | Registros |
|-----------------------------|-----------|
| Assistência médica          | 100.352   |
| Exclusivamente odontológica | 51.149    |

A maior parte dos registros está relacionada à assistência médica.

---

## Porte das Operadoras

| Porte   | Registros |
|---------|-----------|
| Pequeno | 96.391    |
| Médio   | 40.120    |
| Grande  | 14.990    |

As operadoras de pequeno porte representam a maior parte dos registros
na base — mas não das reclamações (ver Insight 02).

---

## Período Coberto

2015 a 2026.

A base cobre mais de 10 anos de histórico.
O ano de 2026 é parcial e deve ser interpretado com cautela.

---

## Qualidade dos Dados

### Colunas sem valores nulos

- registro_ans
- razao_social
- cobertura
- igr
- qtd_reclamacoes
- qtd_beneficiarios
- porte_operadora
- competencia
- competencia_beneficiario

### Colunas com valores nulos

| Coluna         | Valores nulos |
|----------------|---------------|
| dt_atualizacao | 62.119        |

Segundo a documentação da ANS, valores ausentes indicam bases congeladas.
A ausência é esperada e não representa problema de qualidade.

---

## Processamento Realizado

Durante a etapa de preparação:

- padronização dos nomes das colunas para minúsculo;
- conversão da coluna igr para float;
- conversão da coluna dt_atualizacao para datetime;
- conversão das colunas numéricas com `pd.to_numeric`;
- geração do arquivo processado em `data/processed`.

### Impacto do processamento

| Etapa  | Memória  |
|--------|----------|
| Antes  | 24,16 MB |
| Depois | 23,70 MB |

O consumo em memória reflete a conversão da coluna
`dt_atualizacao` para `datetime64[us]`, preservando
a fidelidade do formato original da ANS (AAAAMMDD + hora).
O arquivo CSV em disco ocupa 18,7 MB.

---

## Insight 01 — Crescimento das reclamações supera o crescimento de beneficiários

Entre 2015 e 2024, a taxa de reclamações por 100.000 beneficiários
(IGR correto) aumentou de **10,739 para 35,211**.

Isso representa crescimento superior a **3 vezes** na frequência de
reclamações, enquanto a base de beneficiários cresceu aproximadamente
**21%** no mesmo período.

O crescimento das reclamações não pode ser explicado pelo aumento
da base de beneficiários — há deterioração real na relação entre
operadoras e beneficiários.

---

## Insight 02 — Grande porte concentra reclamações de forma desproporcional

O grande porte representa apenas **9,89% dos registros** na base,
mas concentra **82,54% de todas as reclamações**.

| Porte   | % dos registros | % das reclamações | Razão de concentração |
|---------|-----------------|-------------------|-----------------------|
| Grande  | 9,89%           | 82,54%            | **8,35×**             |
| Médio   | 26,48%          | 13,67%            | 0,52×                 |
| Pequeno | 63,62%          | 3,79%             | 0,06×                 |

O IGR correto por porte confirma:

| Porte   | IGR correto |
|---------|-------------|
| Grande  | 22,332       |
| Médio   | 15,887       |
| Pequeno | 13,441       |

Operadoras de grande porte apresentam maior frequência relativa de
reclamações mesmo após normalização pela carteira.

---

## Insight 03 — O tamanho da operadora não explica sozinho o volume de reclamações

Correlação entre quantidade de beneficiários e quantidade de reclamações:
**0,54** (moderada).

Entre as 10 maiores operadoras por beneficiários, o comportamento
frente ao mercado (IGR de mercado 2015–2025: **20,1619**) é bastante
heterogêneo:

| Operadora               | IGR correto | vs mercado           |
|-------------------------|-------------|----------------------|
| Odontoprev              | 1,300       | 0,07× — muito abaixo |
| Hapvida                 | 18,426       | 0,91× — abaixo       |
| Amil                    | 29,000       | 1,44× — acima        |
| Notre Dame Intermédica  | 33,400       | 1,66× — acima        |
| Bradesco Saúde          | 43,700       | **2,17× — acima**    |
| Sul América             | 34,200       | 1,70× — acima        |
| Unimed Nacional         | 42,500       | **2,11× — acima**    |
| Porto Seguro            | 14,100       | 0,70× — abaixo       |

Carteiras semelhantes, comportamentos completamente distintos.
Fatores operacionais e de atendimento exercem papel relevante.

---

## Insight 04 — Assistência médica concentra praticamente todas as reclamações

| Cobertura          | Reclamações | Participação | IGR correto |
|--------------------|-------------|--------------|-------------|
| Assistência médica | 2.112.387   | 98,07%       | 31,293       |
| Odontológica       | 41.635      | 1,93%        | 1,134       |

A diferença no IGR correto entre os dois tipos de cobertura é de
**27 vezes**.

A dominância da assistência médica se manteve estável ao longo de
todo o período analisado, variando entre 96,51% e 98,72%.

---

## Insight 05 — Operadoras em falência ou liquidação concentram volumes expressivos de reclamações

71 operadoras identificadas com indícios de falência, liquidação ou
insolvência na razão social.

Mesmo representando parcela pequena do mercado, acumulam mais de
3.000 registros e figuram consistentemente entre as maiores taxas
de reclamação após aplicação do filtro mínimo de beneficiários:

| Operadora               | IGR correto |
|-------------------------|-------------|
| Viva Planos (MF)        | 1.285,848      |
| Medical Brasil (MF)     | 1.054,907      |
| Minas Center Med (MF)   | 957,793       |
| Salutar (MF)            | 790,167       |
| SOSaúde (MF)            | 498,348       |

Dificuldades financeiras impactam diretamente a experiência dos
beneficiários.

---

## Insight 06 — Prevent Senior se destaca negativamente entre operadoras ativas

A Prevent Senior Corporate apresenta o maior IGR correto entre
operadoras ativas (não em processo de falência ou liquidação):
**1.321,330** — mais de **65 vezes** o IGR de mercado.

Comportamento completamente distinto das demais operadoras de
grande porte, que apresentam IGR entre 13 e 44.

---

## Insight 07 — Em 2026, o porte médio superou o grande pela primeira vez

Evolução do IGR correto por porte nos últimos anos:

| Ano  | Grande | Médio     | Pequeno |
|------|--------|-----------|---------|
| 2022 | 24,700  | 18,426     | 18,277   |
| 2023 | 36,412  | 26,483     | 18,426   |
| 2024 | 36,952  | 29,348     | 23,967   |
| 2025 | 31,108  | 27,143     | 22,116   |
| 2026 | 31,859  | **35,823** | 23,361   |

Em 2026, pela primeira vez na série histórica, o porte médio ultrapassou
o grande porte em frequência relativa de reclamações.

> ⚠️ 2026 é ano parcial. Essa inversão requer acompanhamento ao longo
> do ano para confirmação da tendência.

---

## Insight 08 — IGR apresenta tendência de crescimento consistente

| Ano  | IGR correto  |
|------|--------------|
| 2015 | 10,739        |
| 2016 | 9,582        |
| 2017 | 9,825        |
| 2018 | 10,739        |
| 2019 | 14,511        |
| 2020 | 16,003        |
| 2021 | 19,534        |
| 2022 | 23,325        |
| 2023 | 33,959        |
| 2024 | 35,211        |
| 2025 | 30,142        |
| 2026 | 32,034 ⚠️    |

O crescimento é consistente de 2016 a 2024, com leve recuo em 2025.

---

## Insight 09 — A pandemia de 2020 marca o ponto de inflexão das reclamações

Antes de 2020, o crescimento do IGR era lento e relativamente estável:

| Ano  | IGR correto | Reclamações | Variação anual |
|------|-------------|-------------|----------------|
| 2015 | 10,739       | 90.783      | —              |
| 2016 | 9,582       | 79.371      | -12,6%         |
| 2017 | 9,825       | 81.362      | +2,5%          |
| 2018 | 10,739       | 89.877      | +10,5%         |
| 2019 | 14,511       | 124.557     | +38,6%         |

A partir de 2020, o ritmo muda estruturalmente:

| Ano  | IGR correto | Reclamações | Variação anual |
|------|-------------|-------------|----------------|
| 2020 | 16,003       | 139.635     | +12,1%         |
| 2021 | 19,534       | 177.061     | +26,8%         |
| 2022 | 23,325       | 220.898     | +24,8%         |
| 2023 | 33,959       | 333.875     | +51,1%         |
| 2024 | 35,211       | 359.162     | +7,6%          |

O crescimento não volta ao ritmo anterior após a pandemia.
O sistema de saúde suplementar parece ter saído estruturalmente
fragilizado do período.

### Hipóteses associadas

- Operadoras reduziram coberturas durante a crise e os conflitos
  com beneficiários se intensificaram nos anos seguintes.
- A sobrecarga operacional do período pandêmico pode ter degradado
  a qualidade do atendimento de forma duradoura.
- O caso da Prevent Senior — maior IGR entre operadoras ativas —
  pode ter relação direta com condutas adotadas durante a pandemia.

> Este insight merece destaque visual no dashboard como marco
> narrativo da série histórica: um ponto de corte claro entre
> o comportamento anterior e posterior a 2020.
