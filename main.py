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

# ==================================================================
# MENSAGENS-CHAVE
# ==================================================================

st.markdown(
    """
    <div style="margin-bottom: 8px;">
    <span style="font-size:12px; color:#2dd4a0; font-weight:700;
    letter-spacing:0.12em;">O QUE OS DADOS REVELAM</span>
    </div>
    """,
    unsafe_allow_html=True
)

col_k1, col_k2 = st.columns(2)

with col_k1:
    st.markdown(
        """
        <div style="background:#0f1a16; border:1px solid #1a3028;
        border-left: 3px solid #ff6b6b; border-radius:10px;
        padding:16px 20px; margin-bottom:12px;">
        <div style="font-size:11px; color:#ff6b6b; font-weight:700;
        letter-spacing:0.08em; margin-bottom:6px;">CRESCIMENTO DESPROPORCIONAL</div>
        <div style="font-size:15px; color:#f0fff8; font-weight:600;
        line-height:1.5;">Reclamações cresceram <span style="color:#ff6b6b">
        296%</span> entre 2015 e 2024, enquanto a base de beneficiários
        cresceu apenas <span style="color:#2dd4a0">21%</span>.</div>
        </div>

        <div style="background:#0f1a16; border:1px solid #1a3028;
        border-left: 3px solid #ff6b6b; border-radius:10px;
        padding:16px 20px; margin-bottom:12px;">
        <div style="font-size:11px; color:#ff6b6b; font-weight:700;
        letter-spacing:0.08em; margin-bottom:6px;">CONCENTRAÇÃO DESPROPORCIONAL</div>
        <div style="font-size:15px; color:#f0fff8; font-weight:600;
        line-height:1.5;">Operadoras de grande porte representam
        <span style="color:#ff6b6b">9,89%</span> dos registros, mas
        concentram <span style="color:#ff6b6b">82,54%</span>
        de todas as reclamações.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_k2:
    st.markdown(
        """
        <div style="background:#0f1a16; border:1px solid #1a3028;
        border-left: 3px solid #ffb060; border-radius:10px;
        padding:16px 20px; margin-bottom:12px;">
        <div style="font-size:11px; color:#ffb060; font-weight:700;
        letter-spacing:0.08em; margin-bottom:6px;">PONTO DE INFLEXÃO</div>
        <div style="font-size:15px; color:#f0fff8; font-weight:600;
        line-height:1.5;">A pandemia de 2020 marcou uma virada estrutural.
        O ritmo de crescimento das reclamações nunca voltou ao padrão
        anterior.</div>
        </div>

        <div style="background:#0f1a16; border:1px solid #1a3028;
        border-left: 3px solid #ffb060; border-radius:10px;
        padding:16px 20px; margin-bottom:12px;">
        <div style="font-size:11px; color:#ffb060; font-weight:700;
        letter-spacing:0.08em; margin-bottom:6px;">OUTLIER EXTREMO</div>
        <div style="font-size:15px; color:#f0fff8; font-weight:600;
        line-height:1.5;">A Prevent Senior apresenta IGR
        <span style="color:#ffb060">65×</span> acima do mercado —
        nenhuma outra operadora ativa chega perto desse número.</div>
        </div>
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