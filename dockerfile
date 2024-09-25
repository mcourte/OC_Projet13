# Utiliser l'image Python 3.10 complète
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances sans mise à jour de pip
RUN pip install --upgrade pip==24.2 --progress-bar off
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt --progress-bar off

# Copier le reste de l'application dans le conteneur
COPY . .


# Donne les permissions d'exécution à start_render.sh
RUN chmod a+x start_render.sh

EXPOSE 8000

CMD ["sh", "-c", "./start_render.sh && gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application"]