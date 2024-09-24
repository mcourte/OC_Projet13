# Utilise une image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements
COPY requirements.txt /app/

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances avec des options pour limiter les ressources
RUN pip install --no-cache-dir --no-use-pep517 -r requirements.txt

# Copier tout le code source de l'application dans le conteneur
COPY . /app/

# Exposer le port 8000
EXPOSE 8000

# Commande à exécuter
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
