# Insights Iniciais

## Estrutura do Dataset

- Total de registros: 151.501
- Total de colunas: 10
- Total de operadoras únicas: 1.411

---

## Cobertura dos Planos

| Cobertura                   | Registros |
| --------------------------- | --------- |
| Assistência médica          | 100.352   |
| Exclusivamente odontológica | 51.149    |

Observação:

A maior parte dos registros está relacionada à assistência médica.

---

## Porte das Operadoras

| Porte   | Registros |
| ------- | --------- |
| Pequeno | 96.391    |
| Médio   | 40.120    |
| Grande  | 14.990    |

Observação:

As operadoras de Pequeno Porte representam a maior parte da base.

---

## Período Coberto

2015 até 2026

Observação:

A base cobre mais de 10 anos de histórico.

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
| -------------- | ------------- |
| dt_atualizacao | 62.119        |

Observação:

Segundo a documentação da ANS, valores ausentes podem indicar bases congeladas.

---

## Processamento Realizado

Durante a etapa de preparação:

- padronização dos nomes das colunas para minúsculo;
- conversão da coluna igr para float;
- conversão da coluna dt_atualizacao para datetime;
- geração do arquivo processado em data/processed.

---

### Impacto do processamento

Consumo de memória:

| Etapa  | Memória  |
|--------|----------|
| Antes  | 24,16 MB |
| Depois | 11,60 MB |

Observação:

A padronização dos tipos reduziu significativamente o consumo de memória do dataset.

---

## Insight 1 — Crescimento proporcional das reclamações

Entre 2015 e 2024 a taxa de reclamações por mil beneficiários aumentou de 0,107 para 0,352.

Isso representa um crescimento superior a 3 vezes na frequência de reclamações.

O aumento das reclamações não pode ser explicado apenas pelo crescimento da quantidade de beneficiários.

---

## Insight 02 — Operadoras de grande porte concentram a maior taxa de reclamações

Após normalização pela quantidade de beneficiários:

| Porte   | Reclamações por mil beneficiários |
| ------- | --------------------------------- |
| Grande  | 0,223                             |
| Médio   | 0,159                             |
| Pequeno | 0,134                             |

Mesmo considerando o tamanho das carteiras, operadoras de grande porte apresentam maior frequência de reclamações.

Isso sugere que fatores operacionais e de experiência do cliente podem exercer influência relevante sobre o volume de reclamações registradas.

Observação:

Durante a análise foi identificado que algumas operadoras apresentavam taxas extremamente elevadas de reclamação.

Ao investigar os dados, verificou-se que essas operadoras possuíam bases muito pequenas de beneficiários (menos de 1.000 usuários), o que distorcia os resultados.

Por esse motivo foi aplicado um filtro mínimo de beneficiários para identificar operadoras com relevância estatística.

---

## Insight 03 — O tamanho da operadora não explica sozinho o volume de reclamações

A análise revelou correlação moderada (0,54) entre quantidade de beneficiários e quantidade de reclamações.

Isso indica que operadoras maiores tendem a receber mais reclamações, porém o tamanho da carteira não é suficiente para explicar completamente o comportamento observado.

Casos como a Odontoprev demonstram que é possível possuir uma das maiores bases de beneficiários do mercado e, ainda assim, apresentar volume relativamente reduzido de reclamações.

O resultado sugere que fatores relacionados à qualidade operacional, atendimento ao cliente, gestão de processos e experiência do beneficiário podem exercer influência relevante sobre o número de reclamações registradas.

-- Correlação observada: 0,54

---

## Insight 04 — Operadoras em falência ou liquidação concentram volumes expressivos de reclamações

A análise identificou 68 operadoras com indícios de falência, liquidação ou insolvência presentes na razão social.

Mesmo representando uma parcela pequena do mercado, essas operadoras acumulam milhares de reclamações ao longo do período analisado.

Casos como Vision Med, Agemed, Unimed Paulistana e Viva Planos demonstram que operadoras em situação financeira crítica continuam registrando volumes relevantes de reclamações mesmo após processos de liquidação ou encerramento das atividades.

O resultado sugere que dificuldades financeiras podem impactar diretamente a experiência dos beneficiários, aumentando conflitos relacionados a atendimento, cobertura e continuidade dos serviços.

Esse comportamento merece investigação específica ao longo do projeto.

---

## Insight 05 — Reclamações cresceram mais rápido que a base de beneficiários

Entre 2015 e 2024:

- Beneficiários cresceram de aproximadamente 845 milhões para mais de 1 bilhão.
- Reclamações cresceram de 90 mil para mais de 359 mil.

O crescimento das reclamações ocorreu em ritmo significativamente superior ao crescimento da quantidade de beneficiários.

Isso sugere deterioração relativa da experiência dos usuários ou aumento da propensão de registrar reclamações junto à ANS.

---

## Insight 06 — Assistência médica concentra praticamente todas as reclamações

Participação das reclamações:

| Cobertura          | Participação |
| ------------------ | ------------ |
| Assistência médica | 98,07%       |
| Odontológica       | 1,93%        |

Quase todas as reclamações registradas na base estão relacionadas aos planos médicos.

Isso sugere que os principais problemas percebidos pelos beneficiários estão concentrados em serviços médicos e hospitalares.

---

## Insight 07 — Algumas operadoras em liquidação continuam acumulando reclamações relevantes

Mesmo após processos de falência, liquidação ou insolvência, diversas operadoras continuam apresentando volumes expressivos de reclamações.

Exemplos:

- Vision Med
- Agemed
- Unimed Paulistana
- Viva Planos
- Saúde Sim

O comportamento sugere que dificuldades financeiras podem impactar diretamente a qualidade do atendimento e a continuidade dos serviços prestados.
