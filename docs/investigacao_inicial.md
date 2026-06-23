# Investigação Inicial — IGR (Índice Geral de Reclamações)

## Objetivo

Realizar o entendimento inicial da base antes das análises exploratórias e identificar possíveis inconsistências, oportunidades analíticas e hipóteses de investigação.

---

## Contexto

O dataset disponibilizado pela ANS contém informações relacionadas ao Índice Geral de Reclamações (IGR) das operadoras de planos de saúde brasileiras.

A base reúne informações de reclamações, beneficiários, cobertura e porte das operadoras.

---

## Descobertas Importantes

### Competência

O dicionário da ANS informa que:

- COMPETENCIA
- COMPETENCIA_BENEFICIARIO

representa mês e ano de referência.

Entretanto, os dados disponibilizados apresentam apenas o ano.

Exemplo:

2015, 2016, 2017...

Essa inconsistência foi registrada para futuras validações.

---

### DT_ATUALIZACAO

O dicionário da ANS informa que registros sem data podem indicar bases congeladas.

Portanto, a existência de valores ausentes nessa coluna aparenta ser esperada.

---

### IGR

Durante a carga inicial dos dados, a coluna IGR foi identificada como texto.

Foi necessária investigação para investigar:

- separador decimal utilizado;
- formato dos valores;
- necessidade de conversão para tipo numérico.

---

## Hipóteses Iniciais

- Operadoras de pequeno porte podem apresentar comportamento diferente das grandes operadoras.
- Assistência médica pode apresentar volume de reclamações superior à odontológica.
- O crescimento das reclamações pode não acompanhar o crescimento dos beneficiários.
- Existem operadoras que podem concentrar parte relevante das reclamações do setor.

---

## Próximos Passos

1. Explorar comportamento temporal das reclamações.
2. Avaliar distribuição do IGR.
3. Investigar operadoras com maiores índices.
4. Construir análises para responder às perguntas de negócio.
