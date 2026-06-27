# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Estilos globais — Paleta Teal Profissional
# ==================================================================

DARK_THEME_CSS = """
<style>

/* ==============================================================
   REMOVE PADDING E HEADER PADRÃO DO STREAMLIT
   ============================================================== */

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0 !important;
}

.block-container {
    padding-top: 2.5rem !important;
    padding-bottom: 2.5rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    max-width: 100% !important;
}

/* ==============================================================
   BASE
   ============================================================== */

html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.stApp {
    background-color: #0a0e14;
    color: #e0f0ea;
}

/* ==============================================================
   SIDEBAR
   ============================================================== */

[data-testid="stSidebar"] {
    background-color: #080c11;
    border-right: 0.5px solid #1a2030;
}

[data-testid="stSidebarNavItems"] a {
    color: #3a5a50 !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 8px 14px !important;
}

[data-testid="stSidebarNavItems"] a:hover {
    color: #2dd4a0 !important;
    background-color: #0f2a22 !important;
}

[data-testid="stSidebarNavItems"] [aria-current="page"] {
    color: #2dd4a0 !important;
    background-color: #0f2a22 !important;
    border-left: 2px solid #2dd4a0 !important;
}

/* ==============================================================
   CABEÇALHOS — FONTES GRANDES E NÍTIDAS
   ============================================================== */

h1 {
    color: #f0fff8 !important;
    font-size: 32px !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
    line-height: 1.2 !important;
}

h2 {
    color: #e0f8f0 !important;
    font-size: 24px !important;
    font-weight: 600 !important;
    line-height: 1.3 !important;
}

h3 {
    color: #c0e8d8 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

p {
    color: #90c0b0 !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
}

/* ==============================================================
   MÉTRICAS
   ============================================================== */

[data-testid="stMetric"] {
    background-color: #0f1a16;
    border: 1px solid #1a3028;
    border-radius: 12px;
    padding: 22px 26px;
}

[data-testid="stMetricLabel"] p {
    color: #3a6a58 !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    letter-spacing: 0.10em;
    text-transform: uppercase;
}

[data-testid="stMetricValue"] {
    color: #f0fff8 !important;
    font-size: 34px !important;
    font-weight: 700 !important;
}

[data-testid="stMetricDelta"] svg { display: none; }

[data-testid="stMetricDelta"] > div {
    color: #3a6a58 !important;
    font-size: 13px !important;
}

/* ==============================================================
   TABS
   ============================================================== */

.stTabs [data-baseweb="tab-list"] {
    background-color: transparent;
    border-bottom: 1px solid #1a3028;
    gap: 4px;
}

.stTabs [data-baseweb="tab"] {
    background-color: transparent;
    border-radius: 8px 8px 0 0;
    color: #3a5a50 !important;
    font-size: 14px !important;
    font-weight: 600;
    padding: 10px 24px;
    border: none;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #2dd4a0 !important;
    background-color: #0f2a22;
}

.stTabs [aria-selected="true"] {
    background-color: #0f2a22 !important;
    color: #2dd4a0 !important;
    border-bottom: 2px solid #2dd4a0;
}

/* ==============================================================
   SELECTBOX E FILTROS
   ============================================================== */

.stSelectbox label p,
.stMultiSelect label p,
[data-testid="stWidgetLabel"] p {
    color: #4a8a70 !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.stSelectbox > div > div,
.stMultiSelect > div > div {
    background-color: #0f1a16 !important;
    border: 1px solid #1a3028 !important;
    border-radius: 8px !important;
    color: #c0e8d8 !important;
    font-size: 14px !important;
}

[data-baseweb="select"] > div {
    background-color: #0f1a16 !important;
    border-color: #1a3028 !important;
}

[data-baseweb="tag"] {
    background-color: #0f2a22 !important;
    color: #2dd4a0 !important;
}

[data-baseweb="menu"] {
    background-color: #0f1a16 !important;
    border: 1px solid #1a3028 !important;
}

[data-baseweb="menu"] li {
    color: #c0e8d8 !important;
    font-size: 14px !important;
}

[data-baseweb="menu"] li:hover {
    background-color: #0f2a22 !important;
}

/* ==============================================================
   SLIDER
   ============================================================== */

[data-testid="stSlider"] [data-baseweb="slider"] div {
    background-color: #2dd4a0 !important;
}

/* Texto dos valores do slider */
[data-testid="stSlider"] [data-testid="stTickBarMin"],
[data-testid="stSlider"] [data-testid="stTickBarMax"],
[data-testid="stSlider"] div[data-baseweb="slider"] [role="slider"] {
    color: #0a0e14 !important;
    font-weight: 700 !important;
}

/* Valor selecionado exibido acima do thumb */
[data-testid="stSlider"] p {
    color: #0a0e14 !important;
    font-weight: 700 !important;
    font-size: 13px !important;
}

/* ==============================================================
   DATAFRAME
   ============================================================== */

[data-testid="stDataFrame"] {
    border: 1px solid #1a3028;
    border-radius: 12px;
    overflow: hidden;
}

/* ==============================================================
   DIVIDER
   ============================================================== */

hr {
    border-color: #1a3028 !important;
    margin: 2rem 0 !important;
}

/* ==============================================================
   COMPONENTES CUSTOMIZADOS
   ============================================================== */

.ans-eyebrow {
    font-size: 12px;
    color: #2dd4a0;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.ans-insight {
    background-color: #0a1f18;
    border-left: 3px solid #2dd4a0;
    border-radius: 0 10px 10px 0;
    padding: 18px 22px;
    margin: 22px 0;
    font-size: 15px;
    color: #90c0b0;
    line-height: 1.75;
}

.ans-insight strong {
    color: #f0fff8;
    font-weight: 600;
}

.ans-badge-danger {
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 6px;
    background-color: #2a1020;
    color: #ff8080;
    border: 1px solid #4a2030;
}

.ans-badge-warning {
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 6px;
    background-color: #2a1e10;
    color: #ffb878;
    border: 1px solid #4a3020;
}

.ans-badge-success {
    display: inline-block;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 6px;
    background-color: #0a2818;
    color: #2dd4a0;
    border: 1px solid #1a4030;
}

.ans-footnote {
    font-size: 13px;
    color: #3a6a58;
    margin-top: 10px;
}

</style>
"""


def inject_css():
    import streamlit as st
    st.markdown(DARK_THEME_CSS, unsafe_allow_html=True)


def eyebrow(text: str) -> str:
    return f'<div class="ans-eyebrow">{text}</div>'


def insight_box(text: str) -> str:
    return f'<div class="ans-insight">{text}</div>'


def badge_danger(text: str) -> str:
    return f'<span class="ans-badge-danger">{text}</span>'


def badge_warning(text: str) -> str:
    return f'<span class="ans-badge-warning">{text}</span>'


def badge_success(text: str) -> str:
    return f'<span class="ans-badge-success">{text}</span>'


def footnote(text: str) -> str:
    return f'<p class="ans-footnote">{text}</p>'


# ==================================================================
# LAYOUT PADRÃO PLOTLY — PALETA TEAL
# ==================================================================

PLOTLY_LAYOUT = dict(
    plot_bgcolor="#0f1a16",
    paper_bgcolor="#0f1a16",
    font=dict(
        family="Inter, Segoe UI, sans-serif",
        color="#c0e8d8",
        size=13
    ),
    xaxis=dict(
        tickfont=dict(size=13, color="#4a8a70"),
        gridcolor="#142818",
        zeroline=False,
        linecolor="#1a3028",
        tickcolor="#1a3028"
    ),
    yaxis=dict(
        tickfont=dict(size=13, color="#4a8a70"),
        gridcolor="#142818",
        zeroline=False,
        linecolor="#1a3028",
        tickcolor="#1a3028"
    ),
    legend=dict(
        font=dict(size=13, color="#4a8a70"),
        bgcolor="rgba(0,0,0,0)",
        bordercolor="rgba(0,0,0,0)"
    ),
    hoverlabel=dict(
        bgcolor="#0f2a22",
        bordercolor="#2dd4a0",
        font=dict(size=14, color="#f0fff8")
    ),
    margin=dict(l=10, r=20, t=30, b=10)
)


def apply_layout(fig, height: int = 320, **kwargs):
    layout = {**PLOTLY_LAYOUT, "height": height, **kwargs}
    fig.update_layout(**layout)
    return fig