# Revisão metodológica — setembro de 2026

Esta nota registra uma revisão posterior do projeto **ANS Complaints Insights**.

## O que foi confirmado

A comparação entre operadoras deve considerar o tamanho das carteiras. Para representar o IGR agregado, a abordagem utilizada na EDA Complementar — somar reclamações e beneficiários antes de aplicar a razão — é mais adequada do que calcular a média simples dos IGRs individuais:

```python
igr_agregado = (
    total_reclamacoes
    / total_beneficiarios
    * 100_000
)
```

A média simples entre operadoras não é matematicamente inválida como estatística descritiva. Porém, ela dá o mesmo peso a carteiras de tamanhos diferentes e não representa adequadamente o IGR agregado do mercado.

## Correção realizada

A coluna `igr` da base da ANS e a documentação oficial da Agência utilizam a referência de **100.000 beneficiários**. A versão anterior do projeto recalculava a razão usando `1.000` e apresentava os valores como “por mil beneficiários”.

A unidade foi corrigida para:

```
reclamações por 100.000 beneficiários
```

A troca de escala multiplica os valores absolutos por 100, mas não altera, por si só, razões relativas ou percentuais de crescimento.

Fontes consultadas:

- [Dados e Índices de Reclamações — ANS](https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/indice-de-reclamacoes-2)

- [Ficha técnica do IGR Anual — ANS](https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/3.3ndiceGeraldeReclamaoAnualIGRAnualPESO1.pdf)

## Investigação da granularidade

O dicionário oficial da ANS, datado de outubro de 2023, descreve `COMPETENCIA` e `COMPETENCIA_BENEFICIARIO` como campos numéricos de tamanho 6, correspondentes a ano e mês (`YYYYMM`).

Entretanto, a amostra efetivamente recebida da fonte contém apenas valores de quatro dígitos:

```
COMPETENCIA:             12 valores únicos, todos com 4 dígitos
COMPETENCIA_BENEFICIARIO: 12 valores únicos, todos com 4 dígitos
```

A verificação foi feita no arquivo bruto recebido da API, antes do processamento. Portanto, **não há evidência de que o ETL tenha removido o mês**. A limitação está presente no arquivo disponibilizado pela origem analisada, apesar da descrição do dicionário.

Mesmo sem o mês explícito, a base apresenta forte evidência de observações mensais implícitas:

- existem 151.501 registros;

- 11.754 combinações de operadora, cobertura e ano aparecem exatamente 12 vezes;

- essas combinações correspondem a 141.048 registros;

- os valores de `qtd_reclamacoes`, `qtd_beneficiarios` e `igr` variam entre as 12 linhas;

- para 2026, a maior parte dos grupos aparece cinco vezes, compatível com o caráter parcial do ano.

A interpretação correta é, portanto:

> A base contém múltiplas observações aparentemente mensais por operadora, cobertura e ano, mas a fonte não fornece o identificador explícito do mês. A periodicidade mensal é uma inferência baseada na estrutura dos registros; os meses exatos e sua completude não podem ser auditados diretamente.

Não foram removidas as linhas repetidas. Duas observações mensais diferentes podem ter exatamente os mesmos valores e parecer duplicatas quando o mês não está disponível.

## Implicação para o cálculo do IGR

Para anos completos, a agregação por soma permanece defensável:

```python
igr_agregado = (
    soma_reclamacoes
    / soma_beneficiarios
    * 100_000
)
```

A fórmula é equivalente à razão entre a média mensal de reclamações e a média mensal de beneficiários quando os mesmos 12 períodos estão representados, pois o fator 12 se cancela no numerador e no denominador.

Como a fonte não informa o mês, o projeto não afirma quais meses estão presentes nem cria artificialmente posições de janeiro a dezembro. Também não aplica `drop_duplicates()`, `mean()` ou `max()` para colapsar as observações.

O ano de 2026 continua sendo tratado como parcial. A estrutura observada indica cinco observações por grupo em grande parte da base, mas não permite afirmar quais meses elas representam.

## Validações adicionadas

A suíte de testes verifica:

- a constante de escala `100_000`;

- a fórmula do IGR contra uma linha conhecida da base;

- a agregação ponderada por reclamações e beneficiários;

- a concordância da coluna `igr` da fonte com a fórmula oficial;

- as regras existentes de qualidade e classificação temporal;

- a existência de múltiplas observações por grupo anual, sem tratá-las automaticamente como duplicações.

## O que permanece como limitação da fonte

A inconsistência entre o dicionário e o arquivo real impede auditar diretamente:

- quais meses estão presentes em cada ano;

- se existem meses ausentes ou repetidos;

- se `COMPETENCIA` e `COMPETENCIA_BENEFICIARIO` estão alinhadas mês a mês;

- quais meses correspondem às cinco observações de 2026.

Essa limitação deve ser atribuída à origem dos dados disponibilizados, não ao `src/process_igr.py`, que preserva numericamente os valores recebidos e não contém transformação que converta `YYYYMM` em `YYYY`.

## Princípio de transparência

Esta revisão não substitui a descoberta original; ela a torna mais precisa. O aprendizado principal permanece: resultados analíticos precisam ser confrontados com a definição oficial do indicador, a unidade de medida, a granularidade real da fonte e as limitações do arquivo efetivamente recebido.
