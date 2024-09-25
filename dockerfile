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
COPY . /app

# Commande par défaut pour exécuter l'application
# Remplacez par la commande appropriée pour démarrer votre application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]