FROM python:3.10-slim

WORKDIR /app

# Mettre à jour pip
RUN pip install --upgrade pip

COPY requirements.txt /app/

# Installer les dépendances sans l'option --no-use-pep517
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "app.py"]
