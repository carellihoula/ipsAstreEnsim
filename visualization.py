import plotly.express as px

def display_choice_distribution(df):
    fig = px.histogram(df, x='Choix_Probable', title="Distribution des Choix Probables (ASTRE vs IPS)")
    fig.show()


def visualize_scores(df):
    # Afficher un graphique de dispersion avec les numéros d'étudiant pour chaque point
    fig = px.scatter(df, x='Score_ASTRE', y='Score_IPS', color='Choix_Probable',
                     title="Comparaison des Scores ASTRE et IPS par Étudiant",
                     text='Numero etudiant',  # Afficher le numéro de chaque étudiant
                     labels={'Score_ASTRE': 'Score ASTRE', 'Score_IPS': 'Score IPS'})

    # Améliorer la lisibilité des textes (numéros d'étudiant)
    fig.update_traces(textposition='top center')
    fig.show()




def visualize_bar_chart(df):
    # Réorganiser les données pour chaque score d'étudiant
    df_melted = df.melt(id_vars=['Numero etudiant', 'Choix_Probable'],
                        value_vars=['Score_ASTRE', 'Score_IPS'],
                        var_name='Option', value_name='Score')

    # Créer un dictionnaire pour spécifier les valeurs dans l'ordre souhaité pour le survol
    hover_template = (
            "Choix Probable: %{customdata[0]}<br>" +
            "Numéro Étudiant: %{x}<br>" +
            "Score IPS: %{customdata[2]}<br>" +
            "Score ASTRE: %{customdata[1]}"
    )

    # Ajout des données personnalisées pour l'affichage survol
    fig = px.bar(
        df_melted, x='Numero etudiant', y='Score', color='Option',
        title="Scores ASTRE et IPS par Étudiant avec Choix Probable",
        labels={'Score': 'Score', 'Numero etudiant': 'Numéro Étudiant', 'Option': 'Option'},
        barmode='group'
    )

    # Ajouter les données pour le survol
    fig.update_traces(
        customdata=df[['Choix_Probable', 'Score_ASTRE', 'Score_IPS']].values,
        hovertemplate=hover_template
    )

    # Organiser les étudiants de la première à la dernière ligne
    fig.update_layout(xaxis={'categoryorder': 'category ascending'})

    fig.show()





