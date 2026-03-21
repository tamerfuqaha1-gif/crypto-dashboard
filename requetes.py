import sqlite3

# On se reconnecte à la base
connexion = sqlite3.connect("crypto.db")
curseur = connexion.cursor()

# Requête 1 : toutes les cryptos
print("--- Toutes les cryptos ---")
curseur.execute("SELECT * FROM cryptos")

# fetchall() récupère tous les résultats
resultats = curseur.fetchall()

# On affiche ligne par ligne
for ligne in resultats:
    print(ligne)

# Requête 2 : uniquement les cryptos avec variation positive
print("\n--- Variation positive ---")
curseur.execute("SELECT name, variation FROM cryptos WHERE variation > 0")
resultats = curseur.fetchall()
for ligne in resultats:
    print(ligne)

# Requête 3 : prix moyen
print("\n--- Prix moyen ---")
curseur.execute("SELECT AVG(prix) FROM cryptos")

# fetchone() récupère un seul résultat
moyenne = curseur.fetchone()
print(f"Prix moyen : {moyenne[0]:,.2f} €")

connexion.close()