import pandas as pd


def load_and_preprocess_data(filepath):
    # Charger les données
    df = pd.read_csv(filepath)

    # Nettoyage et normalisation de certaines colonnes
    df.columns = df.columns.str.strip()  # Suppression des espaces dans les noms de colonnes
    df = df.fillna('')  # Remplace les valeurs manquantes par des chaînes vides

    # Convertir certaines colonnes Oui/Non en numériques
    df['3. Savais-tu déjà ce que tu voulais faire avant de venir à l’ENSIM ?'] = df[
        '3. Savais-tu déjà ce que tu voulais faire avant de venir à l’ENSIM ?'].apply(lambda x: 1 if x == 'Oui' else 0)
    df['9. Envisages-tu l’auto-entreprenariat ?'] = df['9. Envisages-tu l’auto-entreprenariat ?'].apply(
        lambda x: 1 if x == 'Oui' else 0)
    df['21. Envisagez vous un travail sans code/programmation plus tard ?'] = df[
        '21. Envisagez vous un travail sans code/programmation plus tard ?'].apply(lambda x: 1 if x == 'Oui' else 0)

    return df
