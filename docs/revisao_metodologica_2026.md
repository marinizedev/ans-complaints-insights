# Revisão metodológica — setembro de 2026

Esta nota registra uma revisão posterior do projeto ANS Complaints Insights.

## O que foi confirmado

A comparação entre operadoras deve considerar o tamanho das carteiras. Para representar o IGR agregado, a abordagem utilizada no EDA Complementar — somar reclamações e beneficiários antes de aplicar a razão — é mais adequada do que calcular a média simples dos IGRs individuais:

```python
igr_agregado = (
    total_reclamacoes
    / total_beneficiarios
    * 100_000
)
```

A média simples entre operadoras não é matematicamente inválida como estatística descritiva, mas não representa adequadamente o índice agregado do mercado quando as carteiras têm tamanhos diferentes.

## Correção realizada

A coluna `igr` da base da ANS e a documentação oficial da Agência utilizam a referência de **100.000 beneficiários**. A versão anterior do projeto recalculava a mesma razão usando `1.000` e apresentava os valores como “por mil beneficiários”.

A unidade foi corrigida para:

```text
reclamações por 100.000 beneficiários
```

A troca de escala multiplica os valores absolutos por 100, mas não altera, por si só, razões relativas ou percentuais de crescimento.

Fontes consultadas:

- [Dados e Índices de Reclamações — ANS](https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/indice-de-reclamacoes-2)
- [Ficha técnica do IGR Anual — ANS](https://www.gov.br/ans/pt-br/assuntos/informacoes-e-avaliacoes-de-operadoras/3.3ndiceGeraldeReclamaoAnualIGRAnualPESO1.pdf)

## Validações adicionadas

A suíte de testes passou a verificar:

- a constante de escala `100_000`;
- a fórmula do IGR contra uma linha conhecida da base;
- a agregação ponderada por reclamações e beneficiários;
- a concordância da coluna `igr` da fonte com a fórmula oficial;
- as regras já existentes de qualidade e classificação temporal.

## Limitação em investigação

A base processada contém várias observações para uma mesma combinação de operadora, competência anual e cobertura. Muitas chaves aparecem 12 vezes com valores distintos, o que sugere origem mensal, embora o mês não esteja preservado explicitamente no arquivo processado.

Também existem linhas exatamente repetidas. Elas não foram removidas automaticamente: antes é necessário confirmar no arquivo original da ANS se representam duplicação, snapshots ou observações mensais sem identificador de mês.

Por isso, os resultados recalculados nesta etapa corrigem a **unidade do indicador**, mas a validação definitiva da granularidade e da regra de agregação ainda deve ser feita contra a fonte original e seu dicionário de dados.

## Princípio de transparência

Esta revisão não substitui a descoberta original; ela a torna mais precisa. O aprendizado principal permanece: resultados analíticos precisam ser confrontados com a definição oficial do indicador, com a unidade de medida e com a granularidade real da fonte.
