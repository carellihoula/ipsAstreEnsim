weights = {
    'frequence_code': {'ASTRE': 0.7, 'IPS': 0.3},  # Hypothèse : Les étudiants qui codent fréquemment s'orientent davantage vers ASTRE
    'langages_scripting': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Langages de script (Python, Bash) sont plus pertinents pour IPS
    'langages_applications': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Langages de développement d'applications (C#, Kotlin, SWIFT, etc) -> IPS
    'langages_data_management': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Langages de gestion de données (SQL, PHP) -> IPS
    'langages_generalistes': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Langages généralistes (Java) légèrement plus liés à IPS
    'interet_creativite': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Intérêts créatifs (arts, médias) sont plus en phase avec IPS
    'interet_social': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Intérêts sociaux (événements, interactions) -> IPS
    'travail_sans_code': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Rôle sans programmation -> IPS, mais aussi pertinent pour ASTRE
    'langages_bas_niveau': {'ASTRE': 0.8, 'IPS': 0.2},  # Hypothèse : Langages bas niveau (C, C++) pour ASTRE
    'langages_web': {'ASTRE': 0.2, 'IPS': 0.8},  # Hypothèse : Langages web (HTML, CSS, JavaScript) pour IPS
    'interet_technique': {'ASTRE': 0.7, 'IPS': 0.3},  # Hypothèse : Intérêt technique (technologie pure) plus fort vers ASTRE
    'interet_culturel': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Intérêt pour culture et interaction sociale -> IPS
    'formations_anterieures_technique': {'ASTRE': 0.7, 'IPS': 0.3},  # Hypothèse : Formation technique (informatique) pour ASTRE
    'formations_anterieures_generaliste': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Formation généraliste -> IPS
    'profil_personnalite_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Hypothèse : Profil pragmatique et autonome -> ASTRE
    'profil_personnalite_creatif': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Profil créatif et collaboratif -> IPS
    'plan_avant_ensim': {'ASTRE': 0.6, 'IPS': 0.4},  # Hypothèse : Plan de carrière clair avant l'ENSIM -> ASTRE
    'motivation_technique': {'ASTRE': 0.7, 'IPS': 0.3},  # Hypothèse : Motivation par TP/professeurs -> ASTRE
    'motivation_sociale': {'ASTRE': 0.3, 'IPS': 0.7},  # Hypothèse : Motivation par vie sociale et interactions -> IPS
    'auto_entrepreneur': {'ASTRE': 0.5, 'IPS': 0.5},  # Hypothèse : Intérêt pour l'entrepreneuriat partagé entre ASTRE et IPS
    'systeme_exploitation_technique': {'ASTRE': 0.6, 'IPS': 0.4},  # Hypothèse : Utilisation de Linux -> ASTRE
    'systeme_exploitation_grand_public': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Utilisation de macOS/Windows -> IPS
    'preferences_metier_tendance_astre': {'ASTRE': 0.7, 'IPS': 0.3},  # Métiers techniques orientés vers ASTRE
    'preferences_metier_tendance_ips': {'ASTRE': 0.3, 'IPS': 0.7},  # Métiers sociaux/créatifs orientés vers IPS
    'activites_personnelles': {'ASTRE': 0.4, 'IPS': 0.6},  # Hypothèse : Activités personnelles avec un léger penchant pour IPS
    'materiel_bureau_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Hypothèse : Matériel technique sur le bureau (arduino, esp32, autres pcb, etc) -> ASTRE
    'materiel_bureau_classique' : {'ASTRE': 0.3, 'IPS': 0.7}, # Hypothèse : Matériel classoque sur le bureau (crayon, stylo, feuilles,etc) -> IPS0
    'palette_couleurs_ips': {'ASTRE': 0.2, 'IPS': 0.8},  # Hypothèse : Couleurs sobres pour ASTRE
    'palette_couleurs_astre': {'ASTRE': 0.7, 'IPS': 0.3},  # Hypothèse : Couleurs vives pour IPS
    'entreprises_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Hypothèse : Intérêt pour entreprises techniques (ex., STMicroelectronics) -> ASTRE
    'entreprises_creative': {'ASTRE': 0.2, 'IPS': 0.8}  # Hypothèse : Intérêt pour entreprises créatives (ex., Ubisoft) -> IPS
}
