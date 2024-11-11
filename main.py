from data_processing import load_and_preprocess_data
from criteria_scoring import add_scores
from visualization import display_choice_distribution, visualize_scores, visualize_bar_chart
import os

# Chemin vers le fichier CSV dans le dossier 'config'
data_file = os.path.join('config', 'data.csv')

# Charger et traiter les données
df = load_and_preprocess_data(data_file)

# Ajouter les scores et déterminer les choix probables
df = add_scores(df)

# Afficher la distribution des choix
display_choice_distribution(df)

# Visualiser les scores comparatifs
visualize_scores(df)


# Visualiser les scores dans un graphique à barres
visualize_bar_chart(df)

# Sauvegarder les résultats dans le dossier 'resultats'
output_file = os.path.join('resultats', 'resultats_choix_probables.csv')
df.to_csv(output_file, index=False)
