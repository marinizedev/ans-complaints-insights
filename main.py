# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Arquivo principal — configuração da página e home
# ==================================================================

import streamlit as st
from app.styles import inject_css
from app.data_loader import carregar_dados

st.set_page_config(
    page_title="ANS Complaints Insights",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_css()

# ==================================================================
# CARREGAMENTO DOS DADOS
# ==================================================================

df = carregar_dados()

if "df" not in st.session_state:
    st.session_state["df"] = df

# ==================================================================
# HOME
# ==================================================================

st.markdown(
    """
    <div class="ans-eyebrow">SAÚDE SUPLEMENTAR BRASILEIRA · 2015–2026</div>
    """,
    unsafe_allow_html=True
)

st.markdown("# Mais de 2,1 milhões de reclamações registradas na ANS")

st.markdown(
    """
    <p style="font-size:15px; color:#8080a8; max-width:680px;
    line-height:1.8; margin-bottom:32px;">
    Uma década de dados sobre conflitos entre beneficiários e operadoras
    de planos de saúde. A pandemia de 2020 marcou uma virada estrutural
    que ainda não se reverteu.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="font-size:13px; color:#6060888; line-height:2.2;">
        <span style="color:#7c6af7; font-size:15px;">📊</span>
        <a href="/Visão_Geral" style="color:#a89df5;
        text-decoration:none; font-weight:500;">Visão Geral</a>
        <span style="color:#404060"> — métricas e panorama do período</span><br>

        <span style="color:#7c6af7; font-size:15px;">📈</span>
        <a href="/Temporal" style="color:#a89df5;
        text-decoration:none; font-weight:500;">Temporal</a>
        <span style="color:#404060"> — evolução das reclamações e o marco da pandemia</span><br>

        <span style="color:#7c6af7; font-size:15px;">🏢</span>
        <a href="/Porte" style="color:#a89df5;
        text-decoration:none; font-weight:500;">Porte</a>
        <span style="color:#404060"> — comparativo entre grande, médio e pequeno</span><br>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="font-size:13px; color:#606088; line-height:2.2;">
        <span style="color:#7c6af7; font-size:15px;">🔍</span>
        <a href="/Operadoras" style="color:#a89df5;
        text-decoration:none; font-weight:500;">Operadoras</a>
        <span style="color:#404060"> — rankings, outliers e falências</span><br>

        <span style="color:#7c6af7; font-size:15px;">🎛️</span>
        <a href="/Explorar" style="color:#a89df5;
        text-decoration:none; font-weight:500;">Explorar</a>
        <span style="color:#404060"> — filtros livres para sua própria análise</span><br>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
    """
    <div style="font-size:12px; color:#303050; line-height:1.8;">
    Fonte: ANS — Agência Nacional de Saúde Suplementar &nbsp;·&nbsp;
    IGR = reclamações por mil beneficiários &nbsp;·&nbsp;
    Método: ponderado pela carteira &nbsp;·&nbsp;
    2026 = ano parcial
    </div>
    """,
    unsafe_allow_html=True
)