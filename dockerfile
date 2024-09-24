FROM python:3.12
ENV PYTHONUNBUFFERED  1 \
    PYTHONDONTWRITEBYTECODE 1 \
    PIP_NO_PROGRESS_BAR=off
WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt --progress-bar off


# Commande par défaut exécutée au démarrage du conteneur
CMD ["python", "manage.py"]