# critères pour ASTRE et IPS (à ajuster si nécessaire)
import pandas as pd

weights = {
    'frequence_code': 0.2,
    'langages_niveau_bas': 0.15,
    'interet_technique': 0.15,
    'profil_personnalite': 0.2,
    'type_de_films': 0.1,
    'formations_anterieures': 0.1,
    'associations': 0.1
}

def calculate_scores(row):
    score_astre = 0
    score_ips = 0

    # Critère de fréquence de codage
    frequence = row['19. À quelle fréquence codes-tu pour des projets personnels ?']
    if frequence in ['Quotidiennement', 'Plusieurs fois par semaine']:
        score_astre += weights['frequence_code'] * 1
    elif frequence == 'De temps en temps':
        score_astre += weights['frequence_code'] * 0.5

    # Critère de langages informatiques
    langages = row['12. Quels sont les langages informatiques que tu as pratiqué?']
    if any(l in langages for l in ['C', 'C++', 'Assembleur']):
        score_astre += weights['langages_niveau_bas']
    if any(l in langages for l in ['HTML', 'CSS', 'JavaScript']):
        score_ips += weights['langages_niveau_bas']

    # Critère d'intérêt technique
    if '24h du code' in row['5. Quelle(s) association(s) et/ou événement(s) t’intéressent ?']:
        score_astre += weights['interet_technique']
    if 'ENSIMersion' in row['5. Quelle(s) association(s) et/ou événement(s) t’intéressent ?']:
        score_ips += weights['interet_technique']

    # Critère de profil de personnalité
    traits = row['11. Es-tu plutôt : (3 choix maximum)']
    if 'Autonome' in traits or 'Pragmatique' in traits:
        score_astre += weights['profil_personnalite']
    if 'Créatif' in traits or 'Collaboratif' in traits:
        score_ips += weights['profil_personnalite']

    # Critère de type de films préférés
    films = row['2. Quel(s) type(s) de film aimes-tu ?']
    if 'Science-fiction' in films or 'Historique' in films:
        score_astre += weights['type_de_films']
    if 'Romancé' in films or 'Documentaire' in films:
        score_ips += weights['type_de_films']

    # Critère de formation antérieure
    formation = row['7. Quelle(s) est/sont ta/tes formation(s) antérieure(s) ?']
    if 'Informatique' in formation or 'Réseau & Telecom' in formation:
        score_astre += weights['formations_anterieures']
    if 'GEII' in formation:
        score_ips += weights['formations_anterieures']

    choix = 'ASTRE' if score_astre > score_ips else 'IPS'
    return pd.Series([score_astre, score_ips, choix])

def add_scores(df):
    df[['Score_ASTRE', 'Score_IPS', 'Choix_Probable']] = df.apply(calculate_scores, axis=1)
    return df
