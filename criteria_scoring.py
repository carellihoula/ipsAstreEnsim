import pandas as pd

# Dictionnaire des pondérations pour chaque critère et option
weights = {
    'frequence_code': 0.2,
    'langages_bas_niveau': 0.15,
    'langages_web': 0.1,
    'interet_technique': 0.1,
    'interet_culturel': 0.1,
    'formations_anterieures_technique': 0.1,
    'formations_anterieures_generaliste': 0.1,

    'profil_personnalite_technique': 0.15,
    'profil_personnalite_creatif': 0.15,
    'type_films_technique': 0.1,
    'type_films_culturel': 0.1,
    'plan_avant_ensim': 0.1,
    'motivation_technique': 0.1,
    'motivation_sociale': 0.1,
    'auto_entrepreneur': 0.05,
    'systeme_exploitation_technique': 0.05,
    'systeme_exploitation_grand_public': 0.05,
    # Ajout de pondérations pour des critères supplémentaires
    'preferences_metier': 0.05,
    'associations_interets': 0.1,
    'activites_personnelles': 0.05,
    'materiel_bureau_technique': 0.05,
    'palette_couleurs': 0.05,
    #hh
    'specialites_bac_technique': 0.1,
    'associations_kfet': 0.05,
    'entreprises_tech': 0.1,
    'reseaux_sociaux_tech': 0.05,
    'recherche_solution': 0.05,
    'travail_sans_code': 0.1,
    'interet_social':0.1,
    'interet_creativite':0.1,
    'entreprises_technique':0.1,
    'entreprises_creative':0.1
}

# Fonction pour calculer les scores ASTRE et IPS pour chaque étudiant
def calculate_scores(row):
    score_astre = 0
    score_ips = 0

    # Hypothèse 1 : Fréquence de codage (Question 19)
    frequence = row['19. À quelle fréquence codes-tu pour des projets personnels ?']
    if frequence in ['Quotidiennement', 'Plusieurs fois par semaine']:
        score_astre += weights['frequence_code']
        score_ips += weights['frequence_code']
    elif frequence == 'De temps en temps':
        score_astre += weights['frequence_code'] * 0.5
        score_ips += weights['frequence_code'] * 0.5

    # Hypothèse 2 : Langages bas niveau vs. Langages web (Question 12)
    langages = row['12. Quels sont les langages informatiques que tu as pratiqué?']
    # Langages bas niveau pour ASTRE
    if any(l in langages for l in ['C', 'C++', 'Assembleur']):
        score_astre += weights['langages_bas_niveau']

    # Langages de script et développement système pour ASTRE
    if any(l in langages for l in ['Python', 'Shell / Bash']):
        score_astre += weights.get('langages_scripting',
                                   0.1)  # 0.1 est un poids par défaut si 'langages_scripting' n'existe pas

    # Langages web pour IPS (HTML / CSS / Javascript)
    if 'HTML / CSS / Javascript' in langages:
        score_ips += weights['langages_web']

    # Langages de développement d'applications pour IPS
    if any(l in langages for l in ['C#', 'Kotlin / Dart / Swift']):
        score_ips += weights.get('langages_applications',
                                 0.1)  # 0.1 est un poids par défaut si 'langages_applications' n'existe pas

    # Langages de gestion de données pour IPS (SQL et PHP)
    if any(l in langages for l in ['SQL', 'PHP']):
        score_ips += weights.get('langages_data_management',
                                 0.1)  # 0.1 est un poids par défaut si 'langages_data_management' n'existe pas

    # Langage généraliste pour les deux (Java)
    if 'Java' in langages:
        score_astre += weights.get('langages_generalistes', 0.05)
        score_ips += weights.get('langages_generalistes', 0.05)
    # Hypothèse 3 : Intérêts techniques vs. culturels (Question 5)
    associations = row['5. Quelle(s) association(s) et/ou événement(s) t’intéressent ?']
    # Associations techniques pour ASTRE
    if  'IEEE Xtreme' in associations or 'Fablab' in associations:
        score_astre += weights['interet_technique']

    # Associations de créativité et modélisation pour IPS
    if '24h du code' in associations or 'ENSIMersion' in associations or 'Nuit de l’info' in associations:
        score_ips += weights['interet_creativite']

    # Associations sociales pour IPS
    if any(event in associations for event in
           ['AgiLeMans', 'Gala', 'BDLC (Kfet, Trublions, Kartel, ...)', 'Journée des Ensimiens (ex JDA)',
            'Forum de l\'ENSIM', 'BDE']):
        score_ips += weights['interet_social']

    # Hypothèse 4 : Formations techniques vs. généralistes (Question 7)
    formation = row['7. Quelle(s) est/sont ta/tes formation(s) antérieure(s) ?']
    # Formations techniques pour ASTRE excepté le bts
    if any(f in formation for f in ['BUT', 'Prépa intégrée', 'CPGE']):
        score_astre += weights['formations_anterieures_technique']

    # Formations généralistes pour IPS
    if any(f in formation for f in ['BTS', 'Licence', 'Prépa BL']):
        score_ips += weights['formations_anterieures_generaliste']
    if any(f in formation for f in ['Étudiant international']):
        score_ips += weights['formations_anterieures_generaliste']
        score_astre += weights['formations_anterieures_generaliste'] * 0.5


    # Hypothèse 5 : Profil de personnalité (Question 11)
    traits = row['11. Es-tu plutôt : (3 choix maximum)']
    # Traits associés à ASTRE
    if any(trait in traits for trait in ['Autonome', 'Pragmatique', 'Solitaire']):
        score_astre += weights['profil_personnalite_technique']

    # Traits associés à IPS
    if any(trait in traits for trait in ['Collaboratif', 'Créatif', 'Artistique']):
        score_ips += weights['profil_personnalite_creatif']

    # Hypothèse 6 : Type de films préférés (Question 2)
    films = row['2. Quel(s) type(s) de film aimes-tu ?']
    if 'Science-fiction' in films or 'Historique' in films:
        score_astre += weights['type_films_technique']
    if 'Romancé' in films or 'Documentaire' in films:
        score_ips += weights['type_films_culturel']

    # Hypothèse 7 : Plan avant ENSIM (Question 3)
    plan_avant_ensim = row['3. Savais-tu déjà ce que tu voulais faire avant de venir à l’ENSIM ?']
    if plan_avant_ensim == 1:
        score_astre += weights['plan_avant_ensim']
        score_ips += weights['plan_avant_ensim'] * 0.5


    # Hypothèse 8 : Motivation technique vs. sociale (Question 4)
    motivation = row['4. Qu’est-ce qui te motive à venir en cours ?']
    if 'Les TP' in motivation or 'Les profs' in motivation:
        score_astre += weights['motivation_technique']
    if 'Les copains' in motivation or 'La Kfet' in motivation:
        score_ips += weights['motivation_sociale']

    # Hypothèse 9 : Auto-entrepreneuriat (Question 9)
    auto_entrepreneur = row['9. Envisages-tu l’auto-entreprenariat ?']
    if auto_entrepreneur == 1:
        score_astre += weights['auto_entrepreneur']
        score_ips += weights['auto_entrepreneur'] * 0.5

    # Hypothèse 10 : Systèmes d'exploitation techniques vs. grand public (Question 18)
    os = row['18. Quel(s) système(s) d’exploitation utilises-tu ?']
    if 'Linux' in os:
        score_astre += weights['systeme_exploitation_technique']
        score_ips += weights['systeme_exploitation_technique'] * 0.5
    if 'Windows' in os or 'macOS' in os:
        score_ips += weights['systeme_exploitation_grand_public']
        score_astre += weights['systeme_exploitation_technique'] * 0.5

    # Hypothèse : Préférence pour des entreprises spécifiques (Question 10)
    entreprises = row['10. Dans la liste d’entreprise ci-dessous, lesquelles pourraient t’intéresser ?']
    # Entreprises pour ASTRE
    if 'STMicroelectronics' in entreprises or 'Thales' in entreprises or 'ANSSI' in entreprises or 'Bouygues Télécom' in entreprises or 'Schneider Electric' in entreprises:
        score_astre += weights['entreprises_technique']
    # Entreprises pour IPS
    if 'Sopra Steria' in entreprises or 'Ubisoft' in entreprises or 'MMA' in entreprises:
        score_ips += weights['entreprises_creative']

    # Hypothèse 11 : Préférence pour le métier futur (Question 15)
    metier = row['15. Petit, quel était ton métier de rêve ?']
    if metier in ['Architecte', 'Informaticien', 'Inventeur', 'Electricien', 'Astronaute']:
        score_astre += weights['preferences_metier']
    if metier in ['Pompier', 'Policier', 'Chanteur', 'Postier', 'Aventurier']:
        score_ips += weights['preferences_metier']

    # Hypothèse 12 : Activités personnelles (Question 20)
    activites = row['20. Quelles activités te passionnent le plus? (3 choix maximum)']
    if 'Bricolage' in activites or 'Jouer aux jeux vidéos' in activites or 'Lire des bouquins' in activites:
        score_astre += weights['activites_personnelles']

    if 'Activités artistiques' in activites or 'Sorties activités culturelles' in activites or 'Sorties en ville' in activites or 'Sport' in activites:
        score_ips += weights['activites_personnelles']

    # Hypothèse 13 : Matériel sur le bureau (Question 17)
    bureau = row['17. Qu’est-ce que tu as sur ton bureau ?']
    if 'Arduino/Raspberry Pi' in bureau or 'Outils de bricolage' in bureau or 'Plusieurs écrans' in bureau:
        score_astre += weights['materiel_bureau_technique']
    if 'Crayons' in bureau or 'Pinceaux' in bureau or 'Aquarium' in bureau or 'Enceinte connectée' in bureau or 'Calendrier gribouillé' in bureau:
        score_ips += weights['materiel_bureau_technique']

    # Hypothèse 14 : Palette de couleurs préférées (Question 16)
    palette = row['16. Quelle palette de couleurs préfères-tu ?']
    if palette in ['Palette 2', 'Palette 2', 'Sans opinion']:
        score_astre += weights['palette_couleurs']
    if palette == ['Palette 1', 'Palette 3']:
        score_ips += weights['palette_couleurs']

    travail_sans_code = row['21. Envisagez vous un travail sans code/programmation plus tard ?']
    if travail_sans_code == 1:
        score_ips += weights['travail_sans_code']
    if travail_sans_code == 0:
        score_astre += weights['travail_sans_code']
        score_ips += weights['travail_sans_code'] * 0.5
    # Calcul du choix probable
    choix = 'ASTRE' if score_astre > score_ips else 'IPS'
    return pd.Series([score_astre, score_ips, choix])

# Fonction pour ajouter les scores au DataFrame
def add_scores(df):
    df[['Score_ASTRE', 'Score_IPS', 'Choix_Probable']] = df.apply(calculate_scores, axis=1)
    return df
