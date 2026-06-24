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

## Descobertas Importantes

### Competência

O dicionário da ANS informa que:

- `COMPETENCIA`
- `COMPETENCIA_BENEFICIARIO`

representam mês e ano de referência.

Entretanto, os dados disponibilizados apresentam apenas o ano.

Exemplo:

```
2015, 2016, 2017...
```

Essa inconsistência foi registrada para futuras validações.

Durante a EDA complementar, a investigação do campo
`COMPETENCIA_BENEFICIARIO` em 2026 confirmou que o valor também aparece
apenas como `2026`, sem granularidade mensal. Isso reforça que a base está
agregada por ano, não por mês como o dicionário sugere.

---

### DT_ATUALIZACAO

O dicionário da ANS informa que registros sem data podem indicar bases
congeladas.

A ausência de valores nessa coluna (62.119 registros) é, portanto,
esperada e não representa problema de qualidade dos dados.

---

### IGR — Descoberta Crítica

> ⚠️ Esta foi a descoberta mais importante da fase de investigação.

Durante a carga inicial, a coluna IGR foi identificada como texto e
convertida para numérico com sucesso.

Entretanto, ao realizar a EDA principal, o cálculo de IGR médio por ano
através de `df.groupby("competencia")["igr"].mean()` produziu valores
completamente fora de escala:

| Ano  | IGR médio simples |
|------|-------------------|
| 2018 | 25,54             |
| 2019 | 130,75            |
| 2021 | 175,12            |
| 2022 | **357,12**        |

Esses números não fazem sentido para um índice calculado sobre proporções
de reclamações por beneficiário.

**Causa identificada:**

A coluna `IGR` do dataset já contém o índice calculado pela ANS para cada
operadora individualmente. Não é um campo bruto — é um campo derivado.

A fórmula do IGR é:

```
IGR = (QTD_RECLAMACOES / QTD_BENEFICIARIOS) × 1.000
```

Ao calcular a média aritmética do IGR entre operadoras, ignoramos
completamente o tamanho de cada carteira. Uma operadora com 10
beneficiários e 1 reclamação (IGR = 100) recebe o mesmo peso que uma
operadora com 10 milhões de beneficiários e 50 mil reclamações (IGR = 5).
O resultado é matematicamente inválido.

**Exemplo do problema:**

```
Operadora A: 1 reclamação / 10 beneficiários       → IGR = 100,0
Operadora B: 2 reclamações / 10.000 beneficiários  → IGR = 0,2

Média simples:  (100,0 + 0,2) / 2 = 50,1  ← número distorcido
IGR correto:    3 / 10.010 × 1.000 = 0,3  ← número real
```

**Solução adotada:**

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
    * 1000
)
```

**Comparativo após correção:**

| Ano  | IGR médio simples | IGR correto |
|------|-------------------|-------------|
| 2015 | 91,85             | 0,107       |
| 2018 | 25,54             | 0,107       |
| 2019 | 130,75            | 0,145       |
| 2021 | 175,12            | 0,195       |
| 2022 | 357,12            | 0,233       |
| 2024 | 141,53            | 0,352       |

A tendência real é de crescimento consistente e controlado — muito
diferente da oscilação caótica que os números incorretos sugeriam.

---

### 2026 — Ano Parcial

O ano de 2026 está presente na base com dados incompletos:

- Total de reclamações: 142.039 (vs 359.162 em 2024)
- Total de beneficiários: 443 milhões (vs 1,02 bilhão em 2024)
- Operadoras únicas: 897 (vs 935 em 2024)

Todas as análises e visualizações que incluem 2026 devem sinalizá-lo
como ano parcial para evitar interpretações incorretas de queda.

---

## Hipóteses Iniciais

Levantadas antes da EDA. Para hipóteses revisadas com dados reais,
consultar `hypotheses.md`.

- Operadoras de pequeno porte podem apresentar comportamento diferente
  das grandes operadoras.
- Assistência médica pode apresentar volume de reclamações superior à
  odontológica.
- O crescimento das reclamações pode não acompanhar o crescimento dos
  beneficiários.
- Existem operadoras que podem concentrar parte relevante das reclamações
  do setor.

---

## Próximos Passos

1. ~~Explorar comportamento temporal das reclamações.~~ ✅ Concluído
2. ~~Avaliar distribuição do IGR.~~ ✅ Concluído na EDA complementar
3. ~~Investigar operadoras com maiores índices.~~ ✅ Concluído
4. ~~Construir análises para responder às perguntas de negócio.~~ ✅ Em andamento
5. Construir visualizações no Streamlit com dados corrigidos.
6. Produzir narrativa de Data Storytelling.
