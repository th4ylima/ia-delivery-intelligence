# IA Delivery Intelligence

Projeto de análise de dados de delivery desenvolvido com Python e Inteligência Artificial.

## Objetivo

Desenvolver uma solução capaz de gerar dados fictícios de pedidos, validar informações, calcular indicadores operacionais e utilizar Inteligência Artificial para produzir análises e recomendações.

## Tecnologias utilizadas

- Python
- Pandas
- Google Gemini API
- SQL (em desenvolvimento)
- Git e GitHub

## Funcionalidades

- Geração de dados fictícios de pedidos.
- Validação da qualidade dos dados.
- Cálculo de indicadores operacionais.
- Integração com a Gemini API.
- Análise automatizada com Inteligência Artificial.
- Geração de relatórios em Markdown.

## Indicadores analisados

- Quantidade de pedidos.
- Pedidos entregues e cancelados.
- Receita dos pedidos entregues.
- Tempo médio de entrega.
- Taxa de cancelamento.

##  Inteligência Artificial

A Gemini API recebe os indicadores calculados pelo Python e produz uma análise estruturada, com resumo, pontos de atenção, recomendações e limitações.

O projeto orienta a IA a diferenciar fatos de hipóteses e evitar conclusões sem evidências.

##  Limitações

Os dados utilizados são fictícios e a amostra inicial contém apenas cinco pedidos. Portanto, os resultados são demonstrativos e não representam tendências reais do mercado de delivery.

##  Execução

Com o ambiente virtual ativado e as dependências instaladas:

```bash
python src/gerar_dados.py
python src/validar_dados.py
python src/analisar_dados.py
python src/analise_ia_gemini.py
```

A chave da API deve ser configurada localmente no arquivo `.env`, que não deve ser publicado no GitHub.

##  Autoria

Projeto desenvolvido como parte de um portfólio de estudos em Análise e Desenvolvimento de Sistemas, com foco em Dados, Automação e Inteligência Artificial.