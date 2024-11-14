weights = {
    'frequence_code': {'ASTRE': 0.7, 'IPS': 0.3},  #  Les étudiants qui codent fréquemment s'orientent davantage vers ASTRE
    'langages_scripting': {'ASTRE': 0.4, 'IPS': 0.6},  # Langages de script (Python, Bash) sont plus pertinents pour IPS
    'langages_applications': {'ASTRE': 0.3, 'IPS': 0.7},  #  Langages de développement d'applications (C#, Kotlin, SWIFT, etc) ==> IPS
    'langages_data_management': {'ASTRE': 0.3, 'IPS': 0.7},  # Langages de gestion de données (SQL) ==> IPS
    'langages_generalistes': {'ASTRE': 0.5, 'IPS': 0.5},  # Langages généralistes (Java) sont liés à IPS et ASTRE
    'interet_creativite': {'ASTRE': 0.4, 'IPS': 0.6},  #Intérêts créatifs (arts, médias) sont plus en phase avec IPS
    'interet_social': {'ASTRE': 0.4, 'IPS': 0.6},  #  Intérêts sociaux (événements, interactions) ==> IPS
    'travail_sans_code': {'ASTRE': 0.3, 'IPS': 0.7},  # Rôle sans programmation ==> IPS
    'langages_bas_niveau': {'ASTRE': 0.8, 'IPS': 0.2},  # Langages bas niveau (C, C++) pour ASTRE
    'langages_web': {'ASTRE': 0.2, 'IPS': 0.8},  # Langages web (HTML, CSS, JavaScript) pour IPS
    'interet_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Intérêt technique (technologie pure) plus fort vers ASTRE
    'interet_culturel': {'ASTRE': 0.4, 'IPS': 0.6},  #  Intérêt pour culture et interaction sociale ==> IPS
    'formations_anterieures_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Formation technique orienté plus vers ASTRE
    'formations_anterieures_generaliste': {'ASTRE': 0.4, 'IPS': 0.6},  #  Formation généraliste ==> IPS
    'profil_personnalite_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Profil pragmatique et autonome ==> ASTRE
    'profil_personnalite_creatif': {'ASTRE': 0.3, 'IPS': 0.7},  #  Profil créatif et collaboratif ==> IPS
    'plan_avant_ensim': {'ASTRE': 0.6, 'IPS': 0.4},  # Plan de carrière clair avant l'ENSIM ==> ASTRE domine
    'motivation_technique': {'ASTRE': 0.7, 'IPS': 0.3},  # Motivation par TP/professeurs ==> ASTRE
    'motivation_sociale': {'ASTRE': 0.4, 'IPS': 0.6},  # Motivation par vie sociale et interactions ==> IPS
    'auto_entrepreneur': {'ASTRE': 0.6, 'IPS': 0.4},  #  Intérêt pour l'entrepreneuriat partagé entre ASTRE et IPS
    'systeme_exploitation_technique': {'ASTRE': 0.6, 'IPS': 0.4},  #  Utilisation de Linux ==> ASTRE et un peu d'IPS
    'systeme_exploitation_grand_public': {'ASTRE': 0.4, 'IPS': 0.6},  # Utilisation de macOS/Windows ==> IPS et ASTRE aussi, mais IPS domine
    'preferences_metier_tendance_astre': {'ASTRE': 0.8, 'IPS': 0.1},  # Métiers techniques orientés vers ASTRE
    'preferences_metier_tendance_ips': {'ASTRE': 0.2, 'IPS': 0.8},  # Métiers sociaux/créatifs orientés vers IPS
    'activites_personnelles': {'ASTRE': 0.5, 'IPS': 0.5},  # Activités personnelles est partagé entre IPS et ASRE
    'materiel_bureau_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Matériel technique sur le bureau (arduino, esp32, autres pcb, etc) ==> ASTRE
    'materiel_bureau_classique' : {'ASTRE': 0.3, 'IPS': 0.7}, #  Matériel classoque sur le bureau (crayon, stylo, feuilles,etc) ==> IPS0
    'palette_couleurs_ips': {'ASTRE': 0.2, 'IPS': 0.8},  # Couleurs sobres pour ASTRE
    'palette_couleurs_astre': {'ASTRE': 0.7, 'IPS': 0.3},  #  Couleurs vives pour IPS
    'entreprises_technique': {'ASTRE': 0.8, 'IPS': 0.2},  # Intérêt pour entreprises techniques (ex., STMicroelectronics) ==> ASTRE
    'entreprises_creative': {'ASTRE': 0.2, 'IPS': 0.8}  # Intérêt pour entreprises créatives (ex., Ubisoft) ==> IPS
}
