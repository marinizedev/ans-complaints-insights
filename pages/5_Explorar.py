# ==================================================================
# ANS COMPLAINTS INSIGHTS
# Página 5 — Explorar
# ==================================================================

import streamlit as st
import plotly.graph_objects as go
from app.styles import inject_css, eyebrow, footnote, apply_layout
from app.data_loader import carregar_dados, CORES, IGR_MERCADO

st.set_page_config(
    page_title="Explorar · ANS Insights", page_icon="🎛️", layout="wide"
)
inject_css()

df_base = st.session_state.get("df", carregar_dados())

st.markdown(eyebrow("EXPLORAÇÃO LIVRE"), unsafe_allow_html=True)
st.markdown("## Faça suas próprias perguntas")
st.markdown(
    '<p style="font-size:14px; color:#7070a0; margin-bottom:20px;">'
    'Filtre, combine e explore os dados sem restrições.</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# ==================================================================
# FILTROS
# ==================================================================

col_f1, col_f2, col_f3, col_f4 = st.columns(4)

with col_f1:
    anos = sorted(df_base["competencia"].unique())
    ano_range = st.select_slider(
        "Período",
        options=anos, value=(anos[0], anos[-1])
    )

with col_f2:
    coberturas = df_base["cobertura"].unique().tolist()
    cob_sel = st.multiselect(
        "Cobertura", options=coberturas, default=coberturas
    )

with col_f3:
    portes = ["Grande", "Médio", "Pequeno"]
    porte_sel = st.multiselect(
        "Porte", options=portes, default=portes
    )

with col_f4:
    min_benef = st.selectbox(
        "Mínimo de beneficiários",
        options=[0, 1_000, 10_000, 50_000, 100_000],
        index=2,
        format_func=lambda x: (
            "Sem filtro" if x == 0
            else f"{x:,.0f}".replace(",", ".")
        )
    )

# ==================================================================
# APLICAR FILTROS
# ==================================================================

df = df_base[
    (df_base["competencia"] >= ano_range[0]) &
    (df_base["competencia"] <= ano_range[1]) &
    (df_base["cobertura"].isin(cob_sel if cob_sel else coberturas)) &
    (df_base["porte_operadora"].isin(porte_sel if porte_sel else portes))
]

if df.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
    st.stop()

st.markdown("---")

# ==================================================================
# MÉTRICAS DA SELEÇÃO
# ==================================================================

total_rec   = df["qtd_reclamacoes"].sum()
total_benef = df["qtd_beneficiarios"].sum()
igr_sel     = total_rec / total_benef * 1000 if total_benef > 0 else 0
ops_unicas  = df["registro_ans"].nunique()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("RECLAMAÇÕES",
              f"{total_rec:,.0f}".replace(",", "."))
with col2:
    st.metric("BENEFICIÁRIOS",
              f"{total_benef:,.0f}".replace(",", "."))
with col3:
    st.metric("IGR DA SELEÇÃO", f"{igr_sel:.4f}")
with col4:
    st.metric("OPERADORAS",
              f"{ops_unicas:,}".replace(",", "."))

st.markdown("---")

# ==================================================================
# RANKING DE OPERADORAS
# ==================================================================

st.markdown("### Operadoras na seleção")

operadoras_df = (
    df.groupby(["registro_ans", "razao_social"])
    .agg(
        total_reclamacoes=("qtd_reclamacoes", "sum"),
        total_beneficiarios=("qtd_beneficiarios", "sum")
    )
    .reset_index()
)
operadoras_df["igr_correto"] = (
    operadoras_df["total_reclamacoes"]
    / operadoras_df["total_beneficiarios"]
    * 1000
)
operadoras_df["vs_mercado"] = (
    operadoras_df["igr_correto"] / IGR_MERCADO
).round(2)

if min_benef > 0:
    operadoras_df = operadoras_df[
        operadoras_df["total_beneficiarios"] >= min_benef
    ]

col_ord1, col_ord2 = st.columns([3, 1])
with col_ord1:
    ordenar_por = st.selectbox(
        "Ordenar por",
        options=[
            "IGR correto",
            "Total de reclamações",
            "Total de beneficiários"
        ]
    )
with col_ord2:
    n_exibir = st.selectbox(
        "Exibir", options=[10, 20, 50], index=0
    )

mapa = {
    "IGR correto":            "igr_correto",
    "Total de reclamações":   "total_reclamacoes",
    "Total de beneficiários": "total_beneficiarios"
}

resultado = operadoras_df.sort_values(
    mapa[ordenar_por], ascending=False
).head(n_exibir).copy()

resultado["nome_curto"] = resultado["razao_social"].apply(
    lambda x: x[:45] + "..." if len(x) > 45 else x
)

fig = go.Figure(go.Bar(
    x=resultado[mapa[ordenar_por]],
    y=resultado["nome_curto"],
    orientation="h",
    marker_color=CORES["primaria"],
    hovertemplate=(
        "<b>%{y}</b><br>"
        f"{ordenar_por}: %{{x:,.2f}}<extra></extra>"
    )
))
apply_layout(fig, height=max(320, n_exibir * 30),
             xaxis=dict(tickfont=dict(size=12, color="#9090b8"),
                        gridcolor="#252540", zeroline=False),
             yaxis=dict(tickfont=dict(size=11, color="#c0c0e0"),
                        gridcolor="rgba(0,0,0,0)", autorange="reversed"),
             margin=dict(l=10, r=20, t=10, b=10))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==================================================================
# TABELA EXPORTÁVEL
# ==================================================================

st.markdown("### Tabela completa")

tabela = resultado[[
    "razao_social", "total_reclamacoes",
    "total_beneficiarios", "igr_correto", "vs_mercado"
]].copy()
tabela.columns = [
    "Operadora", "Reclamações", "Beneficiários", "IGR correto", "vs mercado"
]
tabela["Reclamações"] = tabela["Reclamações"].apply(
    lambda x: f"{x:,.0f}".replace(",", "."))
tabela["Beneficiários"] = tabela["Beneficiários"].apply(
    lambda x: f"{x:,.0f}".replace(",", "."))
tabela["IGR correto"] = tabela["IGR correto"].apply(lambda x: f"{x:.3f}")
tabela["vs mercado"] = tabela["vs mercado"].apply(lambda x: f"{x:.2f}×")

st.dataframe(tabela, use_container_width=True, hide_index=True)

st.markdown(
    footnote(
        f"Exibindo {len(resultado)} operadoras · "
        f"IGR de mercado de referência: {IGR_MERCADO:.4f} (2015–2025)."
    ),
    unsafe_allow_html=True
)