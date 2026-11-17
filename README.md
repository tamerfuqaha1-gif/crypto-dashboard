# 📈 CryptoDash

Dashboard interactif de visualisation de cryptomonnaies, construit avec **Streamlit** et **Plotly**, avec les données stockées dans une base **SQLite**.

> Projet personnel pour apprendre la chaîne complète : stockage SQL → traitement avec Pandas → visualisation web.

<!-- Ajoute une capture d'écran ici : lance le dashboard, fais une capture, glisse-la dans le dossier "docs/" puis décommente la ligne suivante -->
<!-- ![Aperçu du dashboard](docs/apercu.png) -->

## ✨ Fonctionnalités

- **Cartes KPI** : prix et variation sur 24 h pour chaque crypto (▲ vert / ▼ rouge)
- **Graphique des prix** par crypto
- **Graphique des variations 24 h** avec un dégradé rouge → vert
- **Donut** de répartition des prix
- **Tableau** des données brutes
- Thème sombre personnalisé (CSS)

> ℹ️ Les données sont pour l'instant des **valeurs d'exemple** stockées dans SQLite. Prochaine étape : les récupérer en direct depuis une API publique (CoinGecko).

## 🛠️ Stack technique

| Rôle | Outil |
|---|---|
| Langage | Python 3 |
| Interface web | Streamlit |
| Graphiques | Plotly Express |
| Données | Pandas, SQLite (`sqlite3`) |

## 📁 Structure du projet

```
crypto-dashboard/
├── dashboard.py      # Application Streamlit (point d'entrée)
├── database.py       # Crée la base crypto.db et insère les données
├── requetes.py       # Exemples de requêtes SQL sur la base
├── crypto.py         # Premiers essais Pandas + Plotly (hors Streamlit)
└── requirements.txt  # Dépendances
```

## 🚀 Lancer le projet

```bash
git clone https://github.com/tamerfuqaha1-gif/crypto-dashboard.git
cd crypto-dashboard
pip install -r requirements.txt
streamlit run dashboard.py
```

Le dashboard s'ouvre sur `http://localhost:8501`. La base `crypto.db` est créée automatiquement au premier lancement.

## 🗺️ Pistes d'amélioration

- [ ] Prix en temps réel via l'API CoinGecko
- [ ] Historique des prix et graphique d'évolution
- [ ] Choix des cryptos affichées depuis la barre latérale
- [ ] Déploiement sur Streamlit Community Cloud

## 👤 Auteur

**Tamer Fuqaha**, étudiant ingénieur en informatique à Polytech Nantes
[LinkedIn](https://www.linkedin.com/in/tamer-fuqaha-32934135b/)
