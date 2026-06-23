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
