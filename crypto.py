# On importe pandas et on lui donne le surnom "pd"
# Sans ce surnom on devrait écrire pandas.DataFrame() à chaque fois
import pandas as pd
import plotly.express as px
# Notre liste de dictionnaires (on la connaît déjà)
data = [
    {"name": "Bitcoin",  "symbol": "BTC", "prix": 58000, "variation_24h": 2.5},
    {"name": "Ethereum", "symbol": "ETH", "prix": 3100,  "variation_24h": -1.2},
    {"name": "Solana",   "symbol": "SOL", "prix": 140,   "variation_24h": 4.1},
    {"name": "BNB",      "symbol": "BNB", "prix": 520,   "variation_24h": 0.8},
    {"name": "XRP",      "symbol": "XRP", "prix": 0.52,  "variation_24h": -0.3},
]

# pd.DataFrame() transforme la liste en tableau (comme Excel)
# Les clés des dictionnaires ("name", "prix"...) deviennent les colonnes
# Chaque dictionnaire devient une ligne
df = pd.DataFrame(data)

# Affiche le tableau complet dans le terminal
print(df)

# df["prix"] isole uniquement la colonne "prix"
# .mean() calcule la moyenne de cette colonne
print("Prix moyen :", df["prix"].mean())

# df["variation_24h"] isole la colonne variation
# .max() renvoie la valeur la plus haute
print("Meilleure variation :", df["variation_24h"].max())
print("Nom de la crypto avec la meilleure variation :", df.loc[df["variation_24h"].idxmax(), "name"])

fig = px.bar(df, x="name", y="prix", title="Prix des cryptos")
fig.show()


fig2 = px.bar(
    df,
    x="name",
    y="variation_24h",
    title="Variation des cryptos sur 24h en %",
    color="variation_24h",
    color_continuous_scale=["red", "gray", "green"],
)
fig2.show()


fig3 = px.pie(
    df,
    values="prix",
    names="name",  
    title="Répartition du prix des cryptos"
)
fig3.show()