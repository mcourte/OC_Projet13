# Utilisation de l'image Python slim pour un conteneur plus léger
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt /app/

# Installer les dépendances avec pip optimisé
RUN pip install --upgrade pip==24.2 --progress-bar off \
    && pip install --no-cache-dir --disable-pip-version-check -r requirements.txt --progress-bar off

# Copier le reste de l'application
COPY . .

# Ajouter un utilisateur non-root pour exécuter l'application
RUN useradd -m appuser
USER appuser

# Donne les permissions d'exécution au script
RUN chmod a+x start_render.sh

# Exposer le port
EXPOSE 8000

# Commande de démarrage
CMD ["sh", "-c", "./start_render.sh && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application"]
