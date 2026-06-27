# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Página 1 — Visão Geral
# ==================================================================

import streamlit as st
import plotly.graph_objects as go
from app.styles import inject_css, eyebrow, insight_box, footnote, apply_layout
from app.data_loader import (
    carregar_dados, igr_por_ano, igr_por_porte,
    igr_por_cobertura, CORES, IGR_MERCADO, ANO_PANDEMIA
)

st.set_page_config(
    page_title="Visão Geral · ANS Insights",
    page_icon="📊",
    layout="wide"
)
inject_css()

# ==================================================================
# DADOS
# ==================================================================

df        = st.session_state.get("df_filtrado", carregar_dados())
ano_df    = igr_por_ano(df)
porte_df  = igr_por_porte(df)
cob_df    = igr_por_cobertura(df)

# ==================================================================
# CABEÇALHO
# ==================================================================

st.markdown(eyebrow("VISÃO GERAL"), unsafe_allow_html=True)
st.markdown("## Panorama do período analisado")
st.markdown("---")

# ==================================================================
# MÉTRICAS
# ==================================================================

total_rec   = df["qtd_reclamacoes"].sum()
total_ops   = df["registro_ans"].nunique()
igr_2024    = ano_df[ano_df["competencia"] == 2024]["igr_correto"].values
igr_2015    = ano_df[ano_df["competencia"] == 2015]["igr_correto"].values
igr_2024_v  = igr_2024[0] if len(igr_2024) > 0 else 0
igr_2015_v  = igr_2015[0] if len(igr_2015) > 0 else 0
cresc       = (igr_2024_v - igr_2015_v) / igr_2015_v * 100 if igr_2015_v > 0 else 0

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("TOTAL DE RECLAMAÇÕES",
              f"{total_rec:,.0f}".replace(",", "."),
              "2015 – 2026")
with col2:
    st.metric("CRESCIMENTO DO IGR", f"+{cresc:.0f}%", "2015 → 2024")
with col3:
    st.metric("OPERADORAS ANALISADAS",
              f"{total_ops:,}".replace(",", "."),
              "com histórico ativo")
with col4:
    st.metric("IGR DE MERCADO", f"{IGR_MERCADO:.3f}",
              "por mil beneficiários · 2015–2025")

st.markdown("---")

# ==================================================================
# GRÁFICO — RECLAMAÇÕES POR ANO
# ==================================================================

st.markdown("### Reclamações anuais")

fig = go.Figure()

for periodo, cor in [
    ("pré-pandemia", CORES["pre"]),
    ("inflexão",     CORES["primaria"]),
    ("pós-pandemia", CORES["pos"])
]:
    sub = ano_df[ano_df["periodo"] == periodo]
    fig.add_trace(go.Bar(
        x=sub["competencia"],
        y=sub["total_reclamacoes"],
        name=periodo,
        marker_color=[
            "rgba(45,212,160,0.35)" if r["ano_parcial"] else cor
            for _, r in sub.iterrows()
        ],
        hovertemplate="<b>%{x}</b><br>Reclamações: %{y:,.0f}<extra></extra>"
    ))

fig.add_vline(x=ANO_PANDEMIA - 0.5, line_color="#e05c5c",
              line_width=1.5, line_dash="dash", opacity=0.7)
fig.add_annotation(
    x=ANO_PANDEMIA, y=ano_df["total_reclamacoes"].max() * 0.93,
    text="  pandemia 2020", showarrow=False,
    font=dict(size=12, color="#ff7070"),
    bgcolor="#2a1020", bordercolor="#e05c5c",
    borderwidth=1, borderpad=5, xanchor="left"
)

apply_layout(fig, height=340,
             barmode="stack",
             legend=dict(orientation="h", yanchor="bottom",
                         y=1.02, xanchor="left", x=0,
                         font=dict(size=12, color="#9090b8")))
st.plotly_chart(fig, use_container_width=True)
st.markdown(
    footnote("⚠️ 2026 = ano parcial — barra com opacidade reduzida. Fonte: ANS."),
    unsafe_allow_html=True
)

# ==================================================================
# INSIGHT
# ==================================================================

st.markdown(
    insight_box(
        "A pandemia de 2020 não causou um pico isolado — ela foi o "
        "<strong>ponto de inflexão</strong>. Antes de 2020, o crescimento "
        "era lento e irregular. A partir de 2020, as reclamações crescem "
        "de forma consistente e acelerada, sem retorno ao ritmo anterior. "
        "Entre 2015 e 2024, o IGR cresceu <strong>+228%</strong> enquanto "
        "a base de beneficiários cresceu apenas <strong>+21%</strong>."
    ),
    unsafe_allow_html=True
)

st.markdown("---")

# ==================================================================
# PORTE E COBERTURA
# ==================================================================

col_e, col_d = st.columns(2)

with col_e:
    st.markdown("### Porte das operadoras")
    st.markdown(
        '<p style="font-size:13px;color:#7070a0;margin-bottom:12px;">'
        'Razão de concentração de reclamações</p>',
        unsafe_allow_html=True
    )
    fig_p = go.Figure(go.Bar(
        x=porte_df["razao_concentracao"],
        y=porte_df["porte_operadora"],
        orientation="h",
        marker_color=[
            CORES["perigo"] if x > 1 else CORES["sucesso"]
            for x in porte_df["razao_concentracao"]
        ],
        text=porte_df["razao_concentracao"].apply(lambda x: f"{x:.2f}×"),
        textposition="outside",
        textfont=dict(size=13, color="#d0d0f0"),
        hovertemplate="<b>%{y}</b><br>Razão: %{x:.2f}×<extra></extra>"
    ))
    fig_p.add_vline(x=1, line_color="#404060", line_dash="dot", line_width=1)
    apply_layout(fig_p, height=220,
                 xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False),
                 yaxis=dict(tickfont=dict(size=13, color="#c0c0e0"),
                            gridcolor="rgba(0,0,0,0)"),
                 margin=dict(l=10, r=70, t=10, b=10))
    st.plotly_chart(fig_p, use_container_width=True)
    st.markdown(
        footnote("Grande porte: 9,89% dos registros → 82,54% das reclamações."),
        unsafe_allow_html=True
    )

with col_d:
    st.markdown("### Cobertura")
    st.markdown(
        '<p style="font-size:13px;color:#7070a0;margin-bottom:12px;">'
        'IGR correto por tipo de cobertura</p>',
        unsafe_allow_html=True
    )
    fig_c = go.Figure(go.Bar(
        x=cob_df["igr_correto"],
        y=cob_df["cobertura"],
        orientation="h",
        marker_color=[CORES["perigo"], CORES["sucesso"]],
        text=cob_df["igr_correto"].apply(lambda x: f"{x:.3f}"),
        textposition="outside",
        textfont=dict(size=13, color="#d0d0f0"),
        hovertemplate="<b>%{y}</b><br>IGR: %{x:.4f}<extra></extra>"
    ))
    apply_layout(fig_c, height=220,
                 xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False),
                 yaxis=dict(tickfont=dict(size=12, color="#c0c0e0"),
                            gridcolor="rgba(0,0,0,0)"),
                 margin=dict(l=10, r=70, t=10, b=10))
    st.plotly_chart(fig_c, use_container_width=True)
    st.markdown(
        footnote("Assistência médica: IGR 27× maior que odontológica."),
        unsafe_allow_html=True
    )