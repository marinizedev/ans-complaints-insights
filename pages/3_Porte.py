# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Página 3 — Porte das Operadoras
# ==================================================================

import streamlit as st
import plotly.graph_objects as go
from app.styles import inject_css, eyebrow, insight_box, footnote
from app.data_loader import (
    carregar_dados,
    igr_por_porte,
    igr_porte_por_ano,
    CORES
)

st.set_page_config(
    page_title="Porte · ANS Insights",
    page_icon="🏢",
    layout="wide"
)

inject_css()

# ==================================================================
# DADOS
# ==================================================================

df       = st.session_state.get("df_filtrado", carregar_dados())
porte_df = igr_por_porte(df)
tempo_df = igr_porte_por_ano(df)

# ==================================================================
# CABEÇALHO
# ==================================================================

st.markdown(eyebrow("PORTE DAS OPERADORAS"), unsafe_allow_html=True)
st.markdown("## Grande, médio e pequeno — quem reclama mais?")
st.markdown("---")

# ==================================================================
# MÉTRICAS DE PORTE
# ==================================================================

col1, col2, col3 = st.columns(3)

for col, row in zip(
    [col1, col2, col3],
    porte_df.itertuples()
):
    with col:
        st.metric(
            label=f"PORTE {row.porte_operadora.upper()}",
            value=f"{row.pct_reclamacoes:.1f}% das reclamações",
            delta=f"{row.pct_registros:.1f}% dos registros"
        )

st.markdown("---")

# ==================================================================
# GRÁFICO — RAZÃO DE CONCENTRAÇÃO
# ==================================================================

st.markdown("### Razão de concentração")
st.markdown(
    '<div style="font-size:13px; color:#555; margin-bottom:16px;">'
    'Quanto cada porte concentra de reclamações em relação '
    'à sua presença na base de dados</div>',
    unsafe_allow_html=True
)

fig_conc = go.Figure()

fig_conc.add_trace(go.Bar(
    x=porte_df["porte_operadora"],
    y=porte_df["razao_concentracao"],
    marker_color=[
        CORES["perigo"] if x > 1 else CORES["sucesso"]
        for x in porte_df["razao_concentracao"]
    ],
    text=porte_df["razao_concentracao"].apply(
        lambda x: f"{x:.2f}×"
    ),
    textposition="outside",
    textfont=dict(size=13, color="#888"),
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Razão: %{y:.2f}×<br>"
        "<extra></extra>"
    )
))

# Linha de referência = 1 (neutro)
fig_conc.add_hline(
    y=1,
    line_color="#444",
    line_dash="dot",
    line_width=1,
    annotation_text="linha de equilíbrio",
    annotation_font=dict(size=10, color="#444"),
    annotation_position="right"
)

fig_conc.update_layout(
    plot_bgcolor="#16192a",
    paper_bgcolor="#16192a",
    font_color="#888",
    showlegend=False,
    xaxis=dict(
        tickfont=dict(size=13, color="#999"),
        gridcolor="rgba(0,0,0,0)",
        zeroline=False
    ),
    yaxis=dict(
        tickfont=dict(size=11, color="#555"),
        gridcolor="#1e1e2e",
        zeroline=False
    ),
    margin=dict(l=0, r=80, t=20, b=0),
    height=280
)

st.plotly_chart(fig_conc, use_container_width=True)

st.markdown(
    insight_box(
        "O grande porte representa apenas <strong>9,89%</strong> dos "
        "registros na base, mas concentra <strong>82,54%</strong> de "
        "todas as reclamações — razão de concentração de "
        "<strong>8,35×</strong>. "
        "Pequenas operadoras, por sua vez, têm concentração de apenas "
        "0,06× — praticamente invisíveis no volume total."
    ),
    unsafe_allow_html=True
)

st.markdown("---")

# ==================================================================
# GRÁFICO — IGR POR PORTE
# ==================================================================

st.markdown("### IGR correto por porte")

fig_igr = go.Figure(go.Bar(
    x=porte_df["porte_operadora"],
    y=porte_df["igr_correto"],
    marker_color=[
        CORES["perigo"],
        CORES["atencao"],
        CORES["sucesso"]
    ],
    text=porte_df["igr_correto"].apply(lambda x: f"{x:.3f}"),
    textposition="outside",
    textfont=dict(size=13, color="#888"),
    hovertemplate=(
        "<b>%{x}</b><br>"
        "IGR: %{y:.4f}<br>"
        "<extra></extra>"
    )
))

fig_igr.update_layout(
    plot_bgcolor="#16192a",
    paper_bgcolor="#16192a",
    font_color="#888",
    showlegend=False,
    xaxis=dict(
        tickfont=dict(size=13, color="#999"),
        gridcolor="rgba(0,0,0,0)",
        zeroline=False
    ),
    yaxis=dict(
        tickfont=dict(size=11, color="#555"),
        gridcolor="#1e1e2e",
        zeroline=False,
        title=dict(
            text="reclamações por mil beneficiários",
            font=dict(size=11, color="#444")
        )
    ),
    margin=dict(l=0, r=0, t=20, b=0),
    height=280
)

st.plotly_chart(fig_igr, use_container_width=True)

st.markdown("---")

# ==================================================================
# TABELA DETALHADA DE PORTE
# ==================================================================

st.markdown("### Detalhamento por porte")

tabela = porte_df[[
    "porte_operadora",
    "operadoras_unicas",
    "total_reclamacoes",
    "total_beneficiarios",
    "igr_correto",
    "pct_registros",
    "pct_reclamacoes",
    "razao_concentracao"
]].copy()

tabela.columns = [
    "Porte",
    "Operadoras",
    "Reclamações",
    "Beneficiários",
    "IGR correto",
    "% registros",
    "% reclamações",
    "Razão conc."
]

tabela["Reclamações"] = tabela["Reclamações"].apply(
    lambda x: f"{x:,.0f}".replace(",", ".")
)
tabela["Beneficiários"] = tabela["Beneficiários"].apply(
    lambda x: f"{x:,.0f}".replace(",", ".")
)
tabela["IGR correto"] = tabela["IGR correto"].apply(
    lambda x: f"{x:.3f}"
)
tabela["% registros"] = tabela["% registros"].apply(
    lambda x: f"{x:.2f}%"
)
tabela["% reclamações"] = tabela["% reclamações"].apply(
    lambda x: f"{x:.2f}%"
)
tabela["Razão conc."] = tabela["Razão conc."].apply(
    lambda x: f"{x:.2f}×"
)

st.dataframe(
    tabela,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    footnote(
        "IGR calculado pelo método correto: "
        "soma(reclamações) / soma(beneficiários) × 1.000. "
        "Razão de concentração = % reclamações / % registros."
    ),
    unsafe_allow_html=True
)