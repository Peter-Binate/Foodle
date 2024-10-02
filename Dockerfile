# Utilisation de l'image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /usr/src/app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet dans le conteneur
COPY . .

# Exposer le port sur lequel l'application sera disponible
EXPOSE 8000

# Lancer l'application Django avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodle.wsgi:application"]
