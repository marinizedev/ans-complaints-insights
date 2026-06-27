# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Página 2 — Temporal
# ==================================================================

import streamlit as st
import plotly.graph_objects as go
from app.styles import inject_css, eyebrow, insight_box, footnote, apply_layout
from app.data_loader import (
    carregar_dados, igr_por_ano, igr_porte_por_ano,
    cobertura_por_ano, CORES, ANO_PANDEMIA
)

st.set_page_config(page_title="Temporal · ANS Insights", page_icon="📈", layout="wide")
inject_css()

df       = st.session_state.get("df_filtrado", carregar_dados())
ano_df   = igr_por_ano(df)
porte_df = igr_porte_por_ano(df)
cob_df   = cobertura_por_ano(df)

st.markdown(eyebrow("ANÁLISE TEMPORAL"), unsafe_allow_html=True)
st.markdown("## Evolução das reclamações ao longo do tempo")
st.markdown("---")

# ==================================================================
# 1. IGR CORRETO POR ANO
# ==================================================================

st.markdown("### IGR correto — tendência histórica")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=ano_df["competencia"], y=ano_df["igr_correto"],
    mode="lines+markers", name="IGR correto",
    line=dict(color=CORES["primaria"], width=3),
    marker=dict(
        size=[10 if r["ano_parcial"] else 7 for _, r in ano_df.iterrows()],
        color=[CORES["atencao"] if r["ano_parcial"] else CORES["primaria"]
               for _, r in ano_df.iterrows()],
        symbol=["diamond" if r["ano_parcial"] else "circle"
                for _, r in ano_df.iterrows()]
    ),
    fill="tozeroy", fillcolor="rgba(124,106,247,0.10)",
    hovertemplate="<b>%{x}</b><br>IGR: %{y:.4f}<extra></extra>"
))
fig.add_vline(x=ANO_PANDEMIA, line_color="#e05c5c",
              line_width=1.5, line_dash="dash", opacity=0.6)
fig.add_annotation(
    x=ANO_PANDEMIA, y=ano_df["igr_correto"].max() * 0.90,
    text="  pandemia 2020", showarrow=False,
    font=dict(size=12, color="#ff7070"),
    bgcolor="#2a1020", bordercolor="#e05c5c",
    borderwidth=1, borderpad=5, xanchor="left"
)
apply_layout(fig, height=320,
             yaxis=dict(title=dict(text="IGR por mil beneficiários",
                                   font=dict(size=12, color="#7070a0")),
                        tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False),
             xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False, dtick=1))
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    insight_box(
        "O IGR cresceu <strong>+228%</strong> entre 2015 e 2024. "
        "O ponto de inflexão é 2020 — a partir daí, a curva muda de "
        "inclinação e não retorna ao ritmo anterior. "
        "O recuo de 2025 (0,301) é o primeiro desde 2016, "
        "mas o nível permanece <strong>3× acima</strong> do início da série."
    ),
    unsafe_allow_html=True
)
st.markdown("---")

# ==================================================================
# 2. RECLAMAÇÕES vs BENEFICIÁRIOS
# ==================================================================

st.markdown("### Reclamações vs beneficiários")

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=ano_df["competencia"],
    y=ano_df["total_reclamacoes"],
    name="Reclamações",
    marker_color=[
        "rgba(45,212,160,0.35)" if r["ano_parcial"] else CORES["primaria"]
        for _, r in ano_df.iterrows()
    ],
    yaxis="y1",
    hovertemplate="<b>%{x}</b><br>Reclamações: %{y:,.0f}<extra></extra>"
))
fig2.add_trace(go.Scatter(
    x=ano_df["competencia"], y=ano_df["total_beneficiarios"],
    name="Beneficiários", mode="lines+markers",
    line=dict(color=CORES["sucesso"], width=2.5),
    marker=dict(size=7, color=CORES["sucesso"]),
    yaxis="y2",
    hovertemplate="<b>%{x}</b><br>Beneficiários: %{y:,.0f}<extra></extra>"
))
fig2.add_vline(x=ANO_PANDEMIA, line_color="#e05c5c",
               line_width=1.5, line_dash="dash", opacity=0.4)
apply_layout(fig2, height=340,
             legend=dict(orientation="h", yanchor="bottom", y=1.02,
                         xanchor="left", x=0,
                         font=dict(size=12, color="#9090b8")),
             xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False, dtick=1),
             yaxis=dict(title=dict(text="Reclamações",
                                   font=dict(size=12, color="#7070a0")),
                        tickfont=dict(size=11, color="#9090b8"),
                        gridcolor="#252540", zeroline=False, tickformat=","),
             yaxis2=dict(title=dict(text="Beneficiários",
                                    font=dict(size=12, color="#50e8a0")),
                         tickfont=dict(size=11, color="#50e8a0"),
                         overlaying="y", side="right",
                         zeroline=False, showgrid=False, tickformat=","))
st.plotly_chart(fig2, use_container_width=True)
st.markdown(
    footnote("Beneficiários +21% · Reclamações +296% entre 2015 e 2024."),
    unsafe_allow_html=True
)
st.markdown("---")

# ==================================================================
# 3. IGR POR PORTE
# ==================================================================

st.markdown("### IGR por porte — evolução histórica")

cores_porte = {"Grande": CORES["perigo"], "Médio": CORES["atencao"],
               "Pequeno": CORES["sucesso"]}
fig3 = go.Figure()
for porte in ["Grande", "Médio", "Pequeno"]:
    sub = porte_df[porte_df["porte_operadora"] == porte]
    fig3.add_trace(go.Scatter(
        x=sub["competencia"], y=sub["igr_correto"],
        name=porte, mode="lines+markers",
        line=dict(color=cores_porte[porte], width=2.5),
        marker=dict(size=7, color=cores_porte[porte]),
        hovertemplate=f"<b>{porte} · %{{x}}</b><br>IGR: %{{y:.4f}}<extra></extra>"
    ))
fig3.add_vline(x=ANO_PANDEMIA, line_color="#e05c5c",
               line_width=1.5, line_dash="dash", opacity=0.4)

med_2026 = porte_df[(porte_df["competencia"] == 2026) &
                    (porte_df["porte_operadora"] == "Médio")]["igr_correto"]
if len(med_2026) > 0:
    fig3.add_annotation(
        x=2026, y=med_2026.values[0],
        text="inversão ⚠️", showarrow=True,
        arrowhead=2, arrowcolor="#ffb060",
        font=dict(size=11, color="#ffb060"),
        bgcolor="#2a1e10", bordercolor="#ffb060",
        borderwidth=1, borderpad=4, xanchor="right"
    )
apply_layout(fig3, height=340,
             legend=dict(orientation="h", yanchor="bottom", y=1.02,
                         xanchor="left", x=0,
                         font=dict(size=12, color="#9090b8")),
             xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False, dtick=1),
             yaxis=dict(title=dict(text="IGR correto",
                                   font=dict(size=12, color="#7070a0")),
                        tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False))
st.plotly_chart(fig3, use_container_width=True)
st.markdown(
    insight_box(
        "Em 2026, pela <strong>primeira vez na série histórica</strong>, "
        "o porte médio (IGR 0,358) superou o grande porte (IGR 0,319). "
        "⚠️ 2026 é ano parcial — requer acompanhamento."
    ),
    unsafe_allow_html=True
)
st.markdown("---")

# ==================================================================
# 4. IGR POR COBERTURA
# ==================================================================

st.markdown("### IGR por cobertura — evolução histórica")

medica = cob_df[cob_df["cobertura"] == "Assistência médica"]
odonto = cob_df[cob_df["cobertura"] == "Exclusivamente odontológica"]
fig4 = go.Figure()
fig4.add_trace(go.Scatter(
    x=medica["competencia"], y=medica["igr_correto"],
    name="Assistência médica", mode="lines+markers",
    line=dict(color=CORES["perigo"], width=2.5),
    marker=dict(size=7),
    hovertemplate="<b>Médica · %{x}</b><br>IGR: %{y:.4f}<extra></extra>"
))
fig4.add_trace(go.Scatter(
    x=odonto["competencia"], y=odonto["igr_correto"],
    name="Exclusivamente odontológica", mode="lines+markers",
    line=dict(color=CORES["sucesso"], width=2),
    marker=dict(size=7),
    hovertemplate="<b>Odontológica · %{x}</b><br>IGR: %{y:.4f}<extra></extra>"
))
fig4.add_vline(x=ANO_PANDEMIA, line_color="#e05c5c",
               line_width=1.5, line_dash="dash", opacity=0.4)
apply_layout(fig4, height=320,
             legend=dict(orientation="h", yanchor="bottom", y=1.02,
                         xanchor="left", x=0,
                         font=dict(size=12, color="#9090b8")),
             xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False, dtick=1),
             yaxis=dict(title=dict(text="IGR correto",
                                   font=dict(size=12, color="#7070a0")),
                        tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False))
st.plotly_chart(fig4, use_container_width=True)
st.markdown(
    footnote("IGR médica chegou a 0,573 em 2024 — 27× maior que odontológica."),
    unsafe_allow_html=True
)