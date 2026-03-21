import streamlit as st
import pandas as pd
import plotly.express as px

# ── CONFIG ──
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

# ── CSS ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=Space+Mono&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

.stApp { background-color: #0F1117; }

[data-testid="stSidebar"] {
    background-color: #1A1D2E;
    border-right: 1px solid #2A2D3E;
}

.header {
    background: linear-gradient(135deg, #1A1D2E, #0F1117);
    border: 1px solid #2A2D3E;
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
}
.header h1 { font-size: 2rem; font-weight: 700; color: #E8EAF6; margin: 0; }
.header h1 span { color: #6C63FF; }
.header p { color: #8B8FA8; font-size: 0.9rem; margin: 0.3rem 0 0 0; }

.card {
    background-color: #1A1D2E;
    border: 1px solid #2A2D3E;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
    margin-bottom: 1rem;
}
.card:hover { border-color: #6C63FF; }
.card-name {
    font-size: 0.78rem;
    color: #8B8FA8;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.card-prix {
    font-size: 1.5rem;
    font-weight: 700;
    color: #E8EAF6;
    font-family: 'Space Mono', monospace;
    margin: 0.3rem 0;
}
.card-variation-pos { color: #00C896; font-size: 0.9rem; }
.card-variation-neg { color: #FF4B6E; font-size: 0.9rem; }

.footer {
    text-align: center;
    color: #4A4D60;
    font-size: 0.8rem;
    padding: 2rem 0 1rem;
    border-top: 1px solid #1A1D2E;
    margin-top: 2rem;
    font-family: 'Space Mono', monospace;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ──
st.markdown("""
<div class="header">
    <h1>📈 Crypto<span>Dash</span></h1>
    <p>Dashboard de visualisation crypto · Projet personnel — Tamer Fuqaha</p>
</div>
""", unsafe_allow_html=True)

# ── DONNÉES ──
data = [
    {"name": "Bitcoin",  "symbol": "BTC", "prix": 58000, "variation_24h": 2.5},
    {"name": "Ethereum", "symbol": "ETH", "prix": 3100,  "variation_24h": -1.2},
    {"name": "Solana",   "symbol": "SOL", "prix": 140,   "variation_24h": 4.1},
    {"name": "BNB",      "symbol": "BNB", "prix": 520,   "variation_24h": 0.8},
    {"name": "XRP",      "symbol": "XRP", "prix": 0.52,  "variation_24h": -0.3},
]

df = pd.DataFrame(data)

# ── KPI CARDS ──
col1, col2, col3, col4, col5 = st.columns(5)
colonnes = [col1, col2, col3, col4, col5]

# zip() associe chaque colonne à une crypto en parallèle
for col, crypto in zip(colonnes, data):
    # Si variation positive → vert, sinon → rouge
    if crypto["variation_24h"] >= 0:
        classe = "card-variation-pos"
        signe  = "▲"
    else:
        classe = "card-variation-neg"
        signe  = "▼"

    col.markdown(f"""
    <div class="card">
        <div class="card-name">{crypto["symbol"]}</div>
        <div class="card-prix">{crypto["prix"]:,} €</div>
        <div class="{classe}">{signe} {crypto["variation_24h"]}%</div>
    </div>
    """, unsafe_allow_html=True)

# ── GRAPHIQUES ──
st.subheader("📊 Visualisations")

# Ligne 1 : deux graphiques côte à côte
gauche, droite = st.columns(2)

with gauche:
    fig1 = px.bar(
        df, x="name", y="prix",
        title="Prix en €",
        color="name",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig1.update_layout(
        paper_bgcolor="#1A1D2E",
        plot_bgcolor="#1A1D2E",
        font=dict(color="#E8EAF6"),
        showlegend=False,
    )
    st.plotly_chart(fig1, use_container_width=True)

with droite:
    fig2 = px.bar(
        df, x="name", y="variation_24h",
        title="Variation 24h (%)",
        color="variation_24h",
        color_continuous_scale=["#FF4B6E", "gray", "#00C896"],
    )
    fig2.update_layout(
        paper_bgcolor="#1A1D2E",
        plot_bgcolor="#1A1D2E",
        font=dict(color="#E8EAF6"),
    )
    st.plotly_chart(fig2, use_container_width=True)

# Ligne 2 : camembert centré
_, centre, _ = st.columns([1, 2, 1])
with centre:
    fig3 = px.pie(
        df, values="prix", names="name",
        title="Répartition des prix",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4,
    )
    fig3.update_layout(
        paper_bgcolor="#1A1D2E",
        font=dict(color="#E8EAF6"),
    )
    st.plotly_chart(fig3, use_container_width=True)

# ── TABLEAU ──
st.subheader("📋 Données brutes")
st.dataframe(df, use_container_width=True)

# ── FOOTER ──
st.markdown("""
<div class="footer">
    CryptoDash · Tamer Fuqaha · Polytech Nantes IDIA · 2026
</div>
""", unsafe_allow_html=True)