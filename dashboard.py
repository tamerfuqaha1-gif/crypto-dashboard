import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# ── BASE DE DONNÉES ──
# On crée la base automatiquement si elle n'existe pas
connexion = sqlite3.connect("crypto.db")
curseur = connexion.cursor()

curseur.execute("""
    CREATE TABLE IF NOT EXISTS cryptos (
        id       INTEGER PRIMARY KEY,
        name     TEXT,
        symbol   TEXT,
        prix     REAL,
        variation REAL
    )
""")

cryptos = [
    (1, "Bitcoin",  "BTC", 58000, 2.5),
    (2, "Ethereum", "ETH", 3100,  -1.2),
    (3, "Solana",   "SOL", 140,   4.1),
    (4, "BNB",      "BNB", 520,   0.8),
    (5, "XRP",      "XRP", 0.52,  -0.3),
]

curseur.executemany("INSERT OR IGNORE INTO cryptos VALUES (?,?,?,?,?)", cryptos)
connexion.commit()

df = pd.read_sql_query("SELECT * FROM cryptos", connexion)
connexion.close()

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

# ── KPI CARDS ──
col1, col2, col3, col4, col5 = st.columns(5)
colonnes = [col1, col2, col3, col4, col5]

for col, crypto in zip(colonnes, df.to_dict("records")):
    if crypto["variation"] >= 0:
        classe = "card-variation-pos"
        signe  = "▲"
    else:
        classe = "card-variation-neg"
        signe  = "▼"

    col.markdown(f"""
    <div class="card">
        <div class="card-name">{crypto["symbol"]}</div>
        <div class="card-prix">{crypto["prix"]:,} €</div>
        <div class="{classe}">{signe} {crypto["variation"]}%</div>
    </div>
    """, unsafe_allow_html=True)

# ── GRAPHIQUES ──
st.subheader("📊 Visualisations")

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
        df, x="name", y="variation",
        title="Variation 24h (%)",
        color="variation",
        color_continuous_scale=["#FF4B6E", "gray", "#00C896"],
    )
    fig2.update_layout(
        paper_bgcolor="#1A1D2E",
        plot_bgcolor="#1A1D2E",
        font=dict(color="#E8EAF6"),
    )
    st.plotly_chart(fig2, use_container_width=True)

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