import streamlit as st
import pandas as pd
import plotly.express as px
from data_processing import load_and_preprocess_data
from criteria_scoring import add_scores

# Charger et préparer les données
data_file = 'config/data.csv'
df = load_and_preprocess_data(data_file)
df = add_scores(df)

# Titre de l'application
st.title("Visualisation des Scores ASTRE et IPS des Étudiants")

# Section de recherche d'un étudiant par numéro
st.sidebar.header("Rechercher un étudiant")
numero_etudiant = st.sidebar.text_input("Entrez le numéro de l'étudiant")

# Vérifier si le numéro d'étudiant existe
if numero_etudiant:
    etudiant_info = df[df['Numero etudiant'] == numero_etudiant]

    if not etudiant_info.empty:
        # Afficher les informations de l'étudiant
        st.write(f"### Résultats pour l'étudiant {numero_etudiant}")
        st.write(f"**Score IPS**: {etudiant_info['Score_IPS'].values[0]}")
        st.write(f"**Score ASTRE**: {etudiant_info['Score_ASTRE'].values[0]}")
        st.write(f"**Choix Probable**: {etudiant_info['Choix_Probable'].values[0]}")
    else:
        st.write("Cet étudiant n'existe pas dans nos données.")

# Créer un graphique de comparaison pour tous les étudiants avec un survol personnalisé
df_melted = df.melt(id_vars=['Numero etudiant', 'Choix_Probable'],
                    value_vars=['Score_ASTRE', 'Score_IPS'],
                    var_name='Option', value_name='Score')

# Configurer le graphique
fig = px.bar(
    df_melted, x='Numero etudiant', y='Score', color='Option',
    title="Scores ASTRE et IPS par Étudiant",
    labels={'Score': 'Score', 'Numero etudiant': 'Numéro Étudiant', 'Option': 'Option'},
    barmode='group'
)

# Ajouter les informations de survol personnalisées
df['Score_ASTRE'] = df['Score_ASTRE'].fillna(0)
df['Score_IPS'] = df['Score_IPS'].fillna(0)

fig.update_traces(
    customdata=df[['Numero etudiant', 'Choix_Probable', 'Score_IPS', 'Score_ASTRE']].values,
    hovertemplate="<br>".join([
        "Numéro Étudiant: %{customdata[0]}",
        "Choix Probable: %{customdata[1]}",
        "Score IPS: %{customdata[2]}",
        "Score ASTRE: %{customdata[3]}"
    ])
)

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

# Histogramme pour la répartition des choix probables
fig = px.histogram(df, x='Choix_Probable', title="Répartition des Choix Probables (ASTRE vs IPS)")
st.plotly_chart(fig)

# Créer une colonne 'Égalité' pour indiquer les égalités de scores
df['Égalité'] = df['Score_ASTRE'] == df['Score_IPS']
egalites = df['Égalité'].value_counts()

# Vérifier que les catégories sont bien définies
labels = ['Égalité', 'Pas d\'Égalité']
values = [egalites.get(True, 0), egalites.get(False, 0)]  # Utiliser 0 si la catégorie n'existe pas

# Graphique pour le nombre d'égalités
fig = px.bar(x=labels, y=values,
             title="Nombre d'Égalités de Score entre ASTRE et IPS",
             labels={'x': 'Égalité', 'y': 'Nombre d\'Étudiants'})
st.plotly_chart(fig)

# Graphique d'évolution des scores pour chaque étudiant
fig = px.line(df, x='Numero etudiant', y=['Score_ASTRE', 'Score_IPS'],
              title="Évolution des Scores pour ASTRE et IPS par Étudiant",
              labels={'variable': 'Option', 'value': 'Score'})
st.plotly_chart(fig)
