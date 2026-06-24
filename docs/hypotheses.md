# Hipóteses — ANS Complaints Insights

> Documento atualizado após EDA complementar.
> Hipóteses foram confrontadas com os dados reais.
> Status: Confirmada / Confirmada com ressalva / Refutada / Em investigação.

---

## H1 — Operadoras em falência ou liquidação apresentam taxas mais elevadas de reclamações

**Status: ✅ Confirmada**

### Evidências

Após aplicação do filtro mínimo de 10.000 beneficiários, todas as
posições do topo da lista de IGR correto são ocupadas por operadoras
em processo de falência, liquidação ou insolvência:

| Operadora                        | IGR correto |
|----------------------------------|-------------|
| Viva Planos (Massa Falida)       | 12,858      |
| Medical Brasil (Massa Falida)    | 10,549      |
| Minas Center Med (Massa Falida)  | 9,578       |
| Salutar (Massa Falida)           | 7,902       |
| SOSaúde (Massa Falida)           | 4,983       |

68 operadoras identificadas nessa situação. Mais de 3.000 registros
associados ao longo da série histórica.

---

## H2 — A Prevent Senior apresenta comportamento atípico em relação ao mercado

**Status: ✅ Confirmada e ampliada**

### Evidências

A Prevent Senior Corporate apresenta IGR correto de **13,213** —
o maior entre todas as operadoras ativas (não em processo de
falência ou liquidação).

Para contexto:

- IGR de mercado (2015–2025): **0,2016**
- IGR da Prevent Senior: **13,213**
- Relação: **65 vezes acima do mercado**

Nenhuma outra operadora ativa de porte relevante se aproxima
desse número. O comportamento é genuinamente atípico.

---

## H3 — O crescimento das reclamações não acompanha proporcionalmente o crescimento da base de beneficiários

**Status: ✅ Confirmada com números corrigidos**

### Evidências

| Métrica                         | 2015    | 2024      | Crescimento |
|---------------------------------|---------|-----------|-------------|
| Beneficiários                   | 845 mi  | 1,02 bi   | +21%        |
| Reclamações                     | 90.783  | 359.162   | +296%       |
| IGR correto (por mil benef.)    | 0,107   | 0,352     | +228%       |

O crescimento das reclamações foi **14 vezes maior** que o crescimento
da base de beneficiários no período.

> Nota: a versão anterior citava os mesmos percentuais. A correção do
> IGR reforça a hipótese com uma métrica agora matematicamente confiável.

---

## H4 — Operadoras de grande porte apresentam maior frequência relativa de reclamações

**Status: ✅ Confirmada com dados mais precisos**

### Evidências

IGR correto por porte (acumulado 2015–2026):

| Porte   | IGR correto |
|---------|-------------|
| Grande  | 0,223       |
| Médio   | 0,159       |
| Pequeno | 0,134       |

Razão de concentração (% reclamações / % registros na base):

| Porte   | Razão |
|---------|-------|
| Grande  | 8,35× |
| Médio   | 0,52× |
| Pequeno | 0,06× |

O grande porte representa menos de 10% dos registros da base,
mas concentra mais de 82% de todas as reclamações.

### Ressalva — 2026

Em 2026 (ano parcial), o porte médio registrou IGR de **0,358**,
superando o grande porte (**0,319**) pela primeira vez na série.
Esse comportamento merece acompanhamento.

---

## H5 — A maior parte dos conflitos está concentrada nos planos de assistência médica

**Status: ✅ Confirmada e ampliada com IGR correto**

### Evidências

| Cobertura          | Reclamações | Participação | IGR correto |
|--------------------|-------------|--------------|-------------|
| Assistência médica | 2.112.387   | 98,07%       | 0,313       |
| Odontológica       | 41.635      | 1,93%        | 0,011       |

A diferença de IGR entre os dois tipos de cobertura é de **27 vezes**.

A participação da assistência médica se manteve estável ao longo do
período, variando entre 96,5% e 98,7% ao ano — sem tendência de
mudança estrutural.

---

## H6 — O volume de reclamações está relacionado não apenas ao tamanho da carteira, mas à qualidade operacional

**Status: ✅ Confirmada com evidências mais fortes**

### Evidências

Correlação entre beneficiários e reclamações: **0,54** (moderada).

Entre as 10 maiores operadoras por beneficiários, o comportamento
frente ao mercado varia drasticamente:

| Operadora              | IGR correto | vs mercado |
|------------------------|-------------|------------|
| Odontoprev             | 0,013       | 0,07×      |
| Hapvida                | 0,184       | 0,91×      |
| Bradesco Saúde         | 0,437       | 2,17×      |
| Unimed Nacional        | 0,425       | 2,11×      |

Operadoras com carteiras comparáveis apresentam comportamentos
completamente distintos. O tamanho da carteira não explica sozinho
o resultado.

---

## H7 — Operadoras em situação financeira crítica continuam gerando impacto mesmo após liquidação

**Status: ✅ Confirmada**

### Evidências

- 68 operadoras identificadas em situação de falência ou liquidação.
- Presença recorrente ao longo de vários anos da série histórica.
- Reclamações de operadoras falidas: pico em 2015 (13.964) e 2019 (10.242),
  com queda gradual até 2026 (94 registros).

A redução ao longo do tempo é esperada — à medida que as operadoras
encerram suas atividades, os beneficiários migram para outros planos.
O impacto, entretanto, foi relevante especialmente entre 2015 e 2019.

---

## H8 — Em 2026, o porte médio ultrapassou o grande porte em frequência relativa de reclamações

**Status: 🔍 Em investigação (ano parcial)**

### Evidências iniciais

| Porte   | IGR 2024 | IGR 2025 | IGR 2026 |
|---------|----------|----------|----------|
| Grande  | 0,370    | 0,311    | 0,319    |
| Médio   | 0,293    | 0,271    | **0,358**|
| Pequeno | 0,240    | 0,221    | 0,234    |

Pela primeira vez na série histórica, o porte médio registrou IGR
superior ao grande porte.

> ⚠️ 2026 é ano parcial. A hipótese não pode ser confirmada ou refutada
> com os dados disponíveis até o momento. Requer acompanhamento ao
> longo do ano para validação.
