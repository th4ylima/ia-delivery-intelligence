# IA Delivery Intelligence

Projeto de análise de dados de delivery desenvolvido com Python e Inteligência Artificial, com dashboard interativo em Streamlit e integração com a API do Google Gemini.

🔗 **Demo online:** [Acessar dashboard](COLE_AQUI_O_LINK_DO_STREAMLIT_CLOUD)

## Objetivo

Desenvolver uma solução de análise de dados capaz de gerar pedidos fictícios, validar a qualidade das informações, calcular indicadores operacionais, apresentar os resultados em um dashboard interativo e utilizar Inteligência Artificial para produzir análises e recomendações baseadas nos dados.

## Tecnologias utilizadas

- **Python** — desenvolvimento e processamento dos dados.
- **Pandas** — manipulação e análise de dados.
- **Streamlit** — desenvolvimento do dashboard interativo.
- **Plotly** — criação de gráficos interativos.
- **Google Gemini API** — geração de análises com Inteligência Artificial.
- **SQL** — estudos e desenvolvimento da camada de consultas.
- **Git e GitHub** — versionamento e documentação do projeto.

## Funcionalidades

- Geração automatizada de dados fictícios de pedidos.
- Validação da qualidade dos dados.
- Identificação de valores ausentes, registros duplicados e valores inválidos.
- Cálculo de indicadores operacionais.
- Dashboard interativo com filtros por restaurante e status.
- Visualização de indicadores e gráficos dinâmicos.
- Insights automáticos com base nos dados selecionados.
- Integração com a API do Google Gemini.
- Análise automatizada com Inteligência Artificial.
- Geração e download de relatórios em Markdown.
- Exportação da base de pedidos em CSV.

## Dashboard

A aplicação possui quatro páginas principais:

**1. Dashboard**
- Indicadores operacionais.
- Insights inteligentes.
- Gráfico de pedidos por restaurante.
- Gráfico de distribuição por status.
- Filtros interativos.

**2. Analista IA**
- Integração com Google Gemini.
- Análise estruturada dos indicadores.
- Identificação de pontos de atenção.
- Recomendações e limitações da análise.
- Download do relatório em Markdown.

**3. Qualidade dos Dados**
- Verificação de valores ausentes.
- Identificação de IDs duplicados.
- Validação de valores e informações dos pedidos.

**4. Relatórios**
- Exportação da base de pedidos em CSV.
- Download do relatório gerado pela Inteligência Artificial.

## Indicadores analisados

- Quantidade total de pedidos.
- Pedidos entregues e cancelados.
- Receita dos pedidos entregues.
- Ticket médio.
- Tempo médio de entrega.
- Taxa de cancelamento.

## Inteligência Artificial

O projeto utiliza a API do Google Gemini para transformar indicadores calculados com Python em análises estruturadas.

A IA recebe informações consolidadas e gera:
- Resumo dos resultados.
- Pontos de atenção.
- Recomendações.
- Limitações da análise.

Foram definidos cuidados para evitar conclusões sem evidências, diferenciar fatos de hipóteses e considerar o tamanho da amostra durante a interpretação dos resultados.

## Estrutura do projeto

```text
ia-delivery-intelligence/
├── data/
│   └── pedidos.csv
├── frontend/
│   └── app.py
├── reports/
├── sql/
├── src/
│   ├── gerar_dados.py
│   ├── validar_dados.py
│   ├── analisar_dados.py
│   ├── analise_ia_gemini.py
│   └── analista_ia.py
├── tests/
├── .gitignore
└── README.md
```

## Base de dados

O projeto utiliza uma base com **305 pedidos fictícios**, distribuídos entre seis restaurantes.

Os registros foram gerados por script para simular um cenário operacional de delivery e permitir a aplicação de técnicas de análise e validação de dados.

**Importante:** os dados são inteiramente demonstrativos e não representam informações reais do iFood ou de qualquer outra empresa.

## Limitações

Por utilizar dados simulados, os resultados não representam tendências reais do mercado de delivery.

A base também não contempla informações como:
- Distância entre restaurante e cliente.
- Condições climáticas.
- Horários de pico.
- Motivos específicos de cancelamento.
- Formas de pagamento.

Essas informações poderiam ampliar as possibilidades de análise em versões futuras.

## Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/th4ylima/ia-delivery-intelligence.git
```

Acesse a pasta:

```bash
cd ia-delivery-intelligence
```

Crie e ative o ambiente virtual no Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências, caso o arquivo `requirements.txt` esteja disponível:

```bash
pip install -r requirements.txt
```

Configure sua chave da API do Google Gemini no arquivo `.env`, utilizando o nome de variável esperado pelo código. Não publique esse arquivo no GitHub.

Execute o dashboard:

```bash
streamlit run frontend/app.py
```

## Próximos passos

- Finalizar e ampliar a camada de SQL.
- Conectar o dashboard a fontes de dados reais.
- Adicionar análises por período, bairro e forma de pagamento.
- Ampliar a base de dados com novas variáveis.
- Desenvolver testes automatizados para as funções de cálculo.

## Autoria

Projeto desenvolvido como parte de um portfólio de estudos em Análise e Desenvolvimento de Sistemas, com foco em Dados, Business Intelligence, Automação e Inteligência Artificial.

**Thayna Rezende**

[LinkedIn](https://www.linkedin.com/in/thaynalimarezende) · [GitHub](https://github.com/th4ylima)