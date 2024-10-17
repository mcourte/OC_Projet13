# Utiliser l'image Python 3.10 slim
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip==24.2 --progress-bar off
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt --progress-bar off

# Copier le reste de l'application dans le conteneur
COPY . .

# Donner les permissions d'exécution au script start_render.sh
RUN chmod +x start_render.sh

# Créer un utilisateur non-root
RUN useradd -m appuser

# Passer à cet utilisateur pour l'exécution des commandes
USER appuser

# Exposer le port 8000 pour l'application Django
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["sh", "-c", "./start_render.sh && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application"]
