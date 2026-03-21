# sqlite3 est intégré dans Python, pas besoin de l'installer
import sqlite3

# On se connecte à la base de données
# Si le fichier n'existe pas, Python le crée automatiquement
connexion = sqlite3.connect("crypto.db")

# Le curseur est l'outil qui exécute les requêtes SQL
curseur = connexion.cursor()

# On crée la table avec nos colonnes
curseur.execute("""
    CREATE TABLE IF NOT EXISTS cryptos (
        id        INTEGER PRIMARY KEY,
        name      TEXT,
        symbol    TEXT,
        prix      REAL,
        variation REAL
    )
""")

# On insère nos données
cryptos = [
    (1, "Bitcoin",  "BTC", 58000, 2.5),
    (2, "Ethereum", "ETH", 3100,  -1.2),
    (3, "Solana",   "SOL", 140,   4.1),
    (4, "BNB",      "BNB", 520,   0.8),
    (5, "XRP",      "XRP", 0.52,  -0.3),
]

# executemany() insère plusieurs lignes en une seule fois
curseur.executemany("""
    INSERT OR IGNORE INTO cryptos VALUES (?, ?, ?, ?, ?)
""", cryptos)

# On sauvegarde les changements
connexion.commit()

# On ferme la connexion
connexion.close()

print("Base de données créée ✅")