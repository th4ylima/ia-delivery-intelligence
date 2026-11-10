from pathlib import Path
import sys
from html import escape

import pandas as pd
import plotly.express as px
import streamlit as st


# =========================================================
# CONFIGURAÇÕES INICIAIS
# =========================================================

st.set_page_config(
    page_title="IA Delivery Intelligence",
    page_icon="🚀",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = BASE_DIR / "data" / "pedidos.csv"
PASTA_RELATORIOS = BASE_DIR / "reports"

sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / "src"))


# =========================================================
# ESTILO VISUAL
# =========================================================

st.markdown("""
<style>
    .stApp {
        background-color: #0b1120;
        color: #e2e8f0;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    h1, h2, h3 {
        color: #f8fafc;
    }

    .metric-card {
        background: #172033;
        border: 1px solid #29364d;
        border-radius: 12px;
        padding: 18px;
        min-height: 115px;
        margin-bottom: 12px;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 14px;
    }

    .metric-value {
        color: #f8fafc;
        font-size: 27px;
        font-weight: bold;
        margin-top: 8px;
    }

    .insight-card {
        border-radius: 12px;
        padding: 20px;
        min-height: 175px;
        height: 100%;
        margin-bottom: 14px;
        box-sizing: border-box;
    }

    .insight-titulo {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 13px;
    }

    .insight-mensagem {
        color: #e2e8f0;
        font-size: 14px;
        line-height: 1.6;
    }

    .page-subtitle {
        color: #94a3b8;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# CARREGAMENTO DOS DADOS
# =========================================================

@st.cache_data
def carregar_dados():
    if not ARQUIVO_CSV.exists():
        return pd.DataFrame()

    return pd.read_csv(ARQUIVO_CSV)


df = carregar_dados()

if df.empty:
    st.error(
        "Não foi possível carregar os dados. "
        "Verifique o arquivo data/pedidos.csv."
    )
    st.stop()


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def formatar_moeda(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def gerar_insights(dados):

    total = len(dados)

    if total == 0:
        return []

    cancelados = int(
        (dados["status"].astype(str).str.lower() == "cancelado").sum()
    )

    entregues = dados[
        dados["status"].astype(str).str.lower() == "entregue"
    ]

    percentual_cancelamento = cancelados / total * 100
    percentual_amostra = 100 / total

    if not entregues.empty:
        tempo_medio = entregues["tempo_entrega_min"].mean()

        texto_tempo = (
            f"O tempo médio registrado foi de {tempo_medio:.1f} minutos, "
            f"considerando os {len(entregues)} pedidos entregues. "
            "Não há meta cadastrada para comparação."
        )
    else:
        texto_tempo = (
            "Não existem pedidos entregues na seleção "
            "para calcular o tempo médio."
        )

    volume = dados["restaurante"].value_counts()

    maior_quantidade = int(volume.max())

    restaurantes_destaque = volume[
        volume == maior_quantidade
    ].index.tolist()

    nomes = ", ".join(restaurantes_destaque)

    return [
        {
            "titulo": "ℹ️ Volume da amostra",
            "mensagem": (
                f"A seleção possui {total} pedidos. Cada pedido representa "
                f"aproximadamente {percentual_amostra:.1f}% do total "
                "selecionado. Percentuais podem variar bastante "
                "com poucos registros."
            ),
            "fundo": "#14243c",
            "borda": "#315d99",
            "cor": "#60a5fa"
        },
        {
            "titulo": "⚠️ Atenção aos cancelamentos",
            "mensagem": (
                f"Foram identificados {cancelados} cancelamento(s), "
                f"equivalentes a {percentual_cancelamento:.1f}% "
                "dos pedidos selecionados. O motivo do cancelamento "
                "não está disponível na base."
            ),
            "fundo": "#302d16",
            "borda": "#8b751d",
            "cor": "#facc15"
        },
        {
            "titulo": "ℹ️ Tempo médio de entrega",
            "mensagem": texto_tempo,
            "fundo": "#14243c",
            "borda": "#315d99",
            "cor": "#60a5fa"
        },
        {
            "titulo": "✓ Destaque por volume de pedidos",
            "mensagem": (
                f"{nomes} registraram o maior volume, com "
                f"{maior_quantidade} pedido(s) cada. "
                "O resultado considera somente os dados selecionados."
            ),
            "fundo": "#153329",
            "borda": "#237957",
            "cor": "#4ade80"
        }
    ]


# =========================================================
# COMPONENTES HTML
# =========================================================
# IMPORTANTE: o HTML é montado em linha única, sem indentação e sem
# linhas em branco. No Markdown do Streamlit, linhas com 4+ espaços
# no início são interpretadas como bloco de código.

def exibir_metrica(nome, valor):

    html = (
        f'<div class="metric-card">'
        f'<div class="metric-label">{escape(nome)}</div>'
        f'<div class="metric-value">{escape(valor)}</div>'
        f'</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def exibir_insight(insight):

    titulo = escape(insight["titulo"])
    mensagem = escape(insight["mensagem"])

    fundo = insight["fundo"]
    borda = insight["borda"]
    cor = insight["cor"]

    html = (
        f'<div class="insight-card" '
        f'style="background-color: {fundo}; border: 1px solid {borda};">'
        f'<div class="insight-titulo" style="color: {cor};">{titulo}</div>'
        f'<div class="insight-mensagem">{mensagem}</div>'
        f'</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# =========================================================
# MENU LATERAL
# =========================================================

st.sidebar.markdown("# 🚀 IA Delivery")
st.sidebar.caption("Delivery Intelligence")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Dashboard",
        "Analista IA",
        "Qualidade dos Dados",
        "Relatórios"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Projeto de portfólio | Inteligência de Dados"
)


# =========================================================
# PÁGINA: DASHBOARD
# =========================================================

if pagina == "Dashboard":

    st.title("📊 Dashboard")

    st.markdown(
        '<p class="page-subtitle">'
        'Visão geral dos indicadores de delivery'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # FILTROS

    coluna_filtro1, coluna_filtro2 = st.columns(2)

    with coluna_filtro1:

        restaurantes = sorted(
            df["restaurante"].dropna().unique().tolist()
        )

        restaurantes_selecionados = st.multiselect(
            "Filtrar por restaurante",
            options=restaurantes,
            default=restaurantes
        )

    with coluna_filtro2:

        status_disponiveis = ["Todos"] + sorted(
            df["status"].dropna().astype(str).unique().tolist()
        )

        status_selecionado = st.selectbox(
            "Filtrar por status",
            options=status_disponiveis
        )

    # APLICAÇÃO DOS FILTROS

    df_dashboard = df[
        df["restaurante"].isin(restaurantes_selecionados)
    ].copy()

    if status_selecionado != "Todos":

        df_dashboard = df_dashboard[
            df_dashboard["status"].astype(str) == status_selecionado
        ].copy()

    if df_dashboard.empty:
        st.warning(
            "Nenhum pedido encontrado para os filtros selecionados."
        )
        st.stop()

    # INDICADORES

    total_pedidos = len(df_dashboard)

    entregues = df_dashboard[
        df_dashboard["status"].astype(str).str.lower() == "entregue"
    ]

    cancelados = df_dashboard[
        df_dashboard["status"].astype(str).str.lower() == "cancelado"
    ]

    total_entregues = len(entregues)
    total_cancelados = len(cancelados)

    faturamento = entregues["valor_pedido"].sum()

    ticket_medio = (
        faturamento / total_entregues
        if total_entregues > 0 else 0
    )

    tempo_medio = (
        entregues["tempo_entrega_min"].mean()
        if total_entregues > 0 else 0
    )

    taxa_cancelamento = (
        total_cancelados / total_pedidos * 100
        if total_pedidos > 0 else 0
    )

    # CARDS DE INDICADORES

    st.subheader("Indicadores principais")

    metricas = [
        ("Total de pedidos", str(total_pedidos)),
        ("Faturamento entregue", formatar_moeda(faturamento)),
        ("Ticket médio", formatar_moeda(ticket_medio)),
        ("Tempo médio", f"{tempo_medio:.1f} min"),
        ("Pedidos entregues", str(total_entregues)),
        ("Taxa de cancelamento", f"{taxa_cancelamento:.1f}%")
    ]

    colunas_metricas = st.columns(3)

    for i, (nome, valor) in enumerate(metricas):

        with colunas_metricas[i % 3]:
            exibir_metrica(nome, valor)

    st.markdown("---")

    # INSIGHTS INTELIGENTES

    st.subheader("🧠 Insights Inteligentes")

    insights = gerar_insights(df_dashboard)

    coluna_insight1, coluna_insight2 = st.columns(
        2,
        gap="large"
    )

    with coluna_insight1:
        exibir_insight(insights[0])
        exibir_insight(insights[2])

    with coluna_insight2:
        exibir_insight(insights[1])
        exibir_insight(insights[3])

    st.markdown("---")

    # GRÁFICOS

    st.subheader("📈 Análise dos pedidos")

    grafico1, grafico2 = st.columns(2)

    with grafico1:

        pedidos_restaurante = (
            df_dashboard.groupby("restaurante")
            .size()
            .reset_index(name="quantidade")
        )

        fig_restaurantes = px.bar(
            pedidos_restaurante,
            x="restaurante",
            y="quantidade",
            title="Pedidos por restaurante",
            color="restaurante",
            template="plotly_dark"
        )

        fig_restaurantes.update_layout(
            paper_bgcolor="#0b1120",
            plot_bgcolor="#0b1120",
            showlegend=False
        )

        st.plotly_chart(
            fig_restaurantes,
            width="stretch"
        )

    with grafico2:

        pedidos_status = (
            df_dashboard["status"]
            .value_counts()
            .reset_index()
        )

        pedidos_status.columns = [
            "status",
            "quantidade"
        ]

        fig_status = px.pie(
            pedidos_status,
            names="status",
            values="quantidade",
            title="Distribuição por status",
            hole=0.55,
            template="plotly_dark"
        )

        fig_status.update_layout(
            paper_bgcolor="#0b1120"
        )

        st.plotly_chart(
            fig_status,
            width="stretch"
        )

    st.markdown("---")

    # TABELA DE PEDIDOS

    st.subheader("📋 Pedidos selecionados")

    st.dataframe(
        df_dashboard,
        width="stretch",
        hide_index=True
    )


# =========================================================
# PÁGINA: ANALISTA IA
# =========================================================

elif pagina == "Analista IA":

    st.title("🤖 Analista IA")

    st.markdown(
        '<p class="page-subtitle">'
        'Análise dos dados com inteligência artificial'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.write(
        "Utilize o Gemini para gerar uma análise dos pedidos, "
        "identificar padrões e apresentar observações sobre os dados."
    )

    if st.button(
        "✨ Gerar análise com IA",
        type="primary"
    ):

        with st.spinner(
            "O Gemini está analisando os dados..."
        ):

            try:

                from src.analise_ia_gemini import gerar_analise

                resultado = gerar_analise()

                if resultado:
                    st.session_state["analise_ia"] = resultado
                else:
                    st.warning(
                        "A análise não retornou conteúdo."
                    )

            except Exception as erro:

                st.error(
                    f"Não foi possível gerar a análise: {erro}"
                )

    if "analise_ia" in st.session_state:

        st.markdown("### Resultado da análise")

        st.markdown(
            st.session_state["analise_ia"]
        )

        st.download_button(
            "📥 Baixar análise em Markdown",
            data=st.session_state["analise_ia"],
            file_name="analise_gemini.md",
            mime="text/markdown",
            width="stretch"
        )

    st.caption(
        f"Análise baseada em {len(df)} registros da base atual."
    )


# =========================================================
# PÁGINA: QUALIDADE DOS DADOS
# =========================================================

elif pagina == "Qualidade dos Dados":

    st.title("🔍 Qualidade dos Dados")

    st.markdown(
        '<p class="page-subtitle">'
        'Verificação da consistência da base de pedidos'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    total_registros = len(df)

    valores_ausentes = int(
        df.isnull().sum().sum()
    )

    duplicados = (
        int(df["pedido_id"].duplicated().sum())
        if "pedido_id" in df.columns
        else 0
    )

    valores_invalidos = (
        int((df["valor_pedido"] <= 0).sum())
        if "valor_pedido" in df.columns
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Registros", total_registros)
    col2.metric("Valores ausentes", valores_ausentes)
    col3.metric("IDs duplicados", duplicados)
    col4.metric("Valores inválidos", valores_invalidos)

    st.markdown("---")

    if (
        valores_ausentes == 0
        and duplicados == 0
        and valores_invalidos == 0
    ):

        st.success(
            "Nenhum problema identificado nas verificações realizadas."
        )

    else:

        st.warning(
            "Foram encontrados pontos que precisam de atenção."
        )

    st.subheader("Detalhamento dos valores ausentes")

    ausentes = (
        df.isnull()
        .sum()
        .reset_index()
    )

    ausentes.columns = [
        "Coluna",
        "Valores ausentes"
    ]

    st.dataframe(
        ausentes,
        width="stretch",
        hide_index=True
    )

    st.subheader("Prévia da base de dados")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )


# =========================================================
# PÁGINA: RELATÓRIOS
# =========================================================

elif pagina == "Relatórios":

    st.title("📁 Relatórios")

    st.markdown(
        '<p class="page-subtitle">'
        'Exporte os dados e análises do projeto'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("Base de pedidos")

    csv = df.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        "📥 Baixar base de pedidos (CSV)",
        data=csv,
        file_name="pedidos.csv",
        mime="text/csv",
        width="stretch"
    )

    st.markdown("---")

    st.subheader("Análise gerada pelo Gemini")

    arquivo_analise = (
        PASTA_RELATORIOS / "analise_gemini.md"
    )

    if arquivo_analise.exists():

        conteudo_analise = arquivo_analise.read_text(
            encoding="utf-8"
        )

        st.download_button(
            "📥 Baixar relatório da IA",
            data=conteudo_analise,
            file_name="analise_gemini.md",
            mime="text/markdown",
            width="stretch"
        )

        with st.expander("Visualizar relatório"):
            st.markdown(conteudo_analise)

    else:

        st.info(
            "Nenhum relatório do Gemini foi encontrado. "
            "Acesse a página Analista IA para gerar uma análise."
        )


# =========================================================
# RODAPÉ
# =========================================================

st.markdown("---")

st.caption(
    "IA Delivery Intelligence | Projeto de portfólio"
)
