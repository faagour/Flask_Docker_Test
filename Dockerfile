# Utiliser une image de base Python Alpine
FROM python:3.9-alpine

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu du répertoire actuel dans le répertoire de travail du conteneur
COPY . /app

# Installer les dépendances du projet
RUN  pip install --no-cache-dir -r requirements.txt
# Exposer le port 3000 pour l'application Flask
EXPOSE 5000

# Commande pour démarrer l'application Flask
CMD python ./app.py


