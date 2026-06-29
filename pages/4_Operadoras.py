# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Página 4 — Operadoras
# ==================================================================

import streamlit as st
import plotly.graph_objects as go
from app.styles import inject_css, eyebrow, insight_box, footnote, apply_layout
from app.data_loader import (
    carregar_dados, ranking_operadoras, top_por_volume,
    operadoras_falidas, falidas_por_ano, CORES, IGR_MERCADO, ANO_PANDEMIA
)

st.set_page_config(
    page_title="Operadoras · ANS Insights", page_icon="🔍", layout="wide"
)
inject_css()

df_base = st.session_state.get("df", carregar_dados())

st.markdown(eyebrow("OPERADORAS"), unsafe_allow_html=True)
st.markdown("## Rankings, outliers e operadoras em situação crítica")
st.markdown("---")

# ==================================================================
# FILTRO
# ==================================================================

col_f1, col_f2 = st.columns([2, 2])
with col_f1:
    anos = sorted(df_base["competencia"].unique())
    ano_range = st.select_slider(
        "Período de análise",
        options=anos, value=(anos[0], anos[-1])
    )
with col_f2:
    min_benef = st.selectbox(
        "Mínimo de beneficiários (filtro de relevância)",
        options=[1_000, 10_000, 50_000, 100_000],
        index=1,
        format_func=lambda x: f"{x:,.0f}".replace(",", ".")
    )

df = df_base[
    (df_base["competencia"] >= ano_range[0]) &
    (df_base["competencia"] <= ano_range[1])
]

ranking  = ranking_operadoras(df, min_beneficiarios=min_benef)
volume   = top_por_volume(df)
falidas  = operadoras_falidas(df)
falidas_t = falidas_por_ano(df)

st.markdown("---")

# ==================================================================
# ABAS
# ==================================================================

aba1, aba2, aba3 = st.tabs([
    "🏆  Maiores IGRs",
    "📊  Maior volume",
    "⚠️  Falências e liquidações"
])

# ------------------------------------------------------------------
# ABA 1 — MAIORES IGRs
# ------------------------------------------------------------------

with aba1:
    st.markdown("### Top 15 — maior IGR correto")
    st.markdown(
        f'<p style="font-size:13px; color:#7070a0; margin-bottom:16px;">'
        f'Operadoras com mínimo de '
        f'{min_benef:,.0f} beneficiários</p>'.replace(",", "."),
        unsafe_allow_html=True
    )

    top15 = ranking.head(15).copy()
    top15["nome_curto"] = top15["razao_social"].apply(
        lambda x: x[:48] + "..." if len(x) > 48 else x
    )

    fig = go.Figure(go.Bar(
        x=top15["igr_correto"],
        y=top15["nome_curto"],
        orientation="h",
        marker_color=[
            CORES["perigo"] if r["em_falencia"]
            else (CORES["atencao"] if r["igr_correto"] > IGR_MERCADO * 5
                  else CORES["primaria"])
            for _, r in top15.iterrows()
        ],
        text=top15["igr_correto"].apply(lambda x: f"{x:.2f}"),
        textposition="outside",
        textfont=dict(size=12, color="#d0d0f0"),
        hovertemplate="<b>%{y}</b><br>IGR: %{x:.4f}<extra></extra>"
    ))
    fig.add_vline(
        x=IGR_MERCADO, line_color="#404060", line_dash="dot", line_width=1,
        annotation_text=f"mercado {IGR_MERCADO:.3f}",
        annotation_font=dict(size=11, color="#505070"),
        annotation_position="top right"
    )
    apply_layout(fig, height=520,
                 xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False),
                 yaxis=dict(tickfont=dict(size=11, color="#c0c0e0"),
                            gridcolor="rgba(0,0,0,0)", autorange="reversed"),
                 margin=dict(l=10, r=70, t=20, b=10))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        insight_box(
            "O IGR cresceu <strong>+228%</strong> entre 2015 e 2024. "
            "O ponto de inflexão observado nos dados é 2020 — a partir daí, "
            "a curva muda de inclinação e não retorna ao ritmo anterior. "
            "O recuo de 2025 (0,301) é o primeiro desde 2016, "
            "mas o nível permanece <strong>3× acima</strong> do início da série. "
            "<em>Os dados indicam uma mudança estrutural a partir de 2020, "
            "possivelmente associada à pandemia. Essa associação é uma hipótese "
            "analítica — não uma relação causal comprovada.</em>"
        ),
        unsafe_allow_html=True
    )
    st.markdown("---")

    tabela = ranking.head(20)[[
        "razao_social", "total_reclamacoes", "total_beneficiarios",
        "igr_correto", "vs_mercado", "em_falencia"
    ]].copy()
    tabela.columns = [
        "Operadora", "Reclamações", "Beneficiários",
        "IGR correto", "vs mercado", "Em falência"
    ]
    tabela["Reclamações"] = tabela["Reclamações"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela["Beneficiários"] = tabela["Beneficiários"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela["IGR correto"] = tabela["IGR correto"].apply(lambda x: f"{x:.3f}")
    tabela["vs mercado"] = tabela["vs mercado"].apply(lambda x: f"{x:.1f}×")
    tabela["Em falência"] = tabela["Em falência"].apply(
        lambda x: "⚠️ Sim" if x else "—")
    st.dataframe(tabela, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------
# ABA 2 — MAIOR VOLUME
# ------------------------------------------------------------------

with aba2:
    st.markdown("### Top 10 — maior volume absoluto de reclamações")

    vol = volume.copy()
    vol["nome_curto"] = vol["razao_social"].apply(
        lambda x: x[:42] + "..." if len(x) > 42 else x
    )

    fig2 = go.Figure(go.Bar(
        x=vol["total_reclamacoes"],
        y=vol["nome_curto"],
        orientation="h",
        marker_color=[
            CORES["perigo"] if v > 1 else CORES["sucesso"]
            for v in vol["vs_mercado"]
        ],
        text=vol["total_reclamacoes"].apply(
            lambda x: f"{x:,.0f}".replace(",", ".")),
        textposition="outside",
        textfont=dict(size=12, color="#d0d0f0"),
        hovertemplate="<b>%{y}</b><br>Reclamações: %{x:,.0f}<extra></extra>"
    ))
    apply_layout(fig2, height=400,
                 xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False, tickformat=","),
                 yaxis=dict(tickfont=dict(size=11, color="#c0c0e0"),
                            gridcolor="rgba(0,0,0,0)", autorange="reversed"),
                 margin=dict(l=10, r=90, t=20, b=10))
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown(
        insight_box(
            "Notre Dame Intermédica, Amil e Bradesco lideram em volume "
            "absoluto — mas a correlação entre tamanho e reclamações é "
            "apenas moderada (<strong>0,54</strong>). "
            "A Odontoprev, maior carteira do mercado, tem IGR "
            "<strong>15× menor</strong> que a média. "
            "<em>Esses contrastes sugerem que fatores operacionais e de "
            "qualidade de atendimento podem exercer papel relevante — "
            "hipótese que não pode ser confirmada apenas com este dataset.</em>"
        ),
        unsafe_allow_html=True
    )
    st.markdown("---")

    tabela2 = vol[[
        "razao_social", "total_reclamacoes",
        "total_beneficiarios", "igr_correto", "vs_mercado"
    ]].copy()
    tabela2.columns = [
        "Operadora", "Reclamações", "Beneficiários", "IGR correto", "vs mercado"
    ]
    tabela2["Reclamações"] = tabela2["Reclamações"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela2["Beneficiários"] = tabela2["Beneficiários"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela2["IGR correto"] = tabela2["IGR correto"].apply(lambda x: f"{x:.3f}")
    tabela2["vs mercado"] = tabela2["vs mercado"].apply(lambda x: f"{x:.2f}×")
    st.dataframe(tabela2, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------
# ABA 3 — FALÊNCIAS
# ------------------------------------------------------------------

with aba3:
    st.markdown("### Operadoras em falência, liquidação ou insolvência")

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("OPERADORAS IDENTIFICADAS", "68",
                  "com termos na razão social")
    with col_b:
        st.metric("TOTAL DE RECLAMAÇÕES",
                  f"{falidas['total_reclamacoes'].sum():,.0f}".replace(",", "."),
                  "acumulado no período")

    st.markdown("---")
    st.markdown("#### Reclamações de operadoras falidas por ano")

    fig3 = go.Figure(go.Bar(
        x=falidas_t["competencia"],
        y=falidas_t["total_reclamacoes"],
        marker_color=CORES["perigo"],
        opacity=0.85,
        hovertemplate="<b>%{x}</b><br>Reclamações: %{y:,.0f}<extra></extra>"
    ))
    fig3.add_vline(x=ANO_PANDEMIA, line_color="#e09a3e",
                   line_width=1.5, line_dash="dash", opacity=0.5)
    apply_layout(fig3, height=280,
                 xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False),
                 yaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                            gridcolor="#252540", zeroline=False,
                            tickformat=","))
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown(
        footnote("Pico em 2015 (13.964 reclamações). Redução gradual "
                 "à medida que os beneficiários migram após o encerramento."),
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("#### Ranking por volume de reclamações")

    tabela3 = falidas.head(20)[[
        "razao_social", "total_reclamacoes",
        "total_beneficiarios", "igr_correto"
    ]].copy()
    tabela3.columns = [
        "Operadora", "Reclamações", "Beneficiários", "IGR correto"
    ]
    tabela3["Reclamações"] = tabela3["Reclamações"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela3["Beneficiários"] = tabela3["Beneficiários"].apply(
        lambda x: f"{x:,.0f}".replace(",", "."))
    tabela3["IGR correto"] = tabela3["IGR correto"].apply(lambda x: f"{x:.3f}")
    st.dataframe(tabela3, use_container_width=True, hide_index=True)

    st.markdown(
        insight_box(
            "Vision Med, Agemed e Unimed Paulistana lideram em volume "
            "mesmo estando em processo de encerramento. "
            "O padrão observado nos dados sugere que o aumento de reclamações "
            "pode anteceder a falência formal — mas essa é uma hipótese "
            "analítica baseada na correlação temporal, "
            "<em>não uma relação de causa e efeito estabelecida.</em>"
        ),
        unsafe_allow_html=True
    )