import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("Crypto Dashboard")
data = [
    {"name": "Bitcoin",  "symbol": "BTC", "prix": 58000, "variation_24h": 2.5},
    {"name": "Ethereum", "symbol": "ETH", "prix": 3100,  "variation_24h": -1.2},
    {"name": "Solana",   "symbol": "SOL", "prix": 140,   "variation_24h": 4.1},
    {"name": "BNB",      "symbol": "BNB", "prix": 520,   "variation_24h": 0.8},
    {"name": "XRP",      "symbol": "XRP", "prix": 0.52,  "variation_24h": -0.3},
]   
df = pd.DataFrame(data)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Bitcoin", "$58,000", "2.5%")
col2.metric("Ethereum", "$3,100", "-1.2%")
col3.metric("Solana", "$140", "4.1%")
col4.metric("BNB", "$520", "0.8%")
col5.metric("XRP", "$0.52", "-0.3%")

st.subheader("Prix des cryptos")

fig = px.bar(df, x="name", y="prix", title="Prix des cryptos en euros")
st.plotly_chart(fig, use_container_width=True)

gauche, droite = st.columns(2)

with gauche:
    fig2 = px.bar(df, x="name", y="variation_24h", title="Variation des cryptos sur 24h en %", color="variation_24h", color_continuous_scale=["red", "gray", "green"])
    st.plotly_chart(fig2, use_container_width=True)

with droite:    
    fig3 = px.pie(df, values="prix", names="name", title="Répartition du prix des cryptos")
    st.plotly_chart(fig3, use_container_width=True)

st.subheader("Données brutes")
st.dataframe(df, use_container_width=True)
