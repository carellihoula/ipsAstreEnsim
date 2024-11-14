# Utiliser une image de base Python avec un OS Linux
FROM python:3.8-slim

# Installation de JDK 11
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean

# Définir JAVA_HOME pour JDK 11
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

# Installation des dépendances de l'application
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code dans le conteneur
COPY . .

# Définir la commande pour démarrer l'application (remplacez par la commande de votre app)
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
