# Utiliser l'image Python 3.10 complète
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Mettre à jour pip et installer les dépendances sans cache
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . /app

# Commande par défaut pour exécuter l'application
CMD ["python", "manage.py"] 
