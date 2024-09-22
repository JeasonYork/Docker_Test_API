#!/bin/bash

# Créez le dossier de logs sur la machine hôte
mkdir -p ./logs

# Construire les images Docker des tests
docker build -t my_image_auth -f Dockerfile.auth .
docker build -t my_image_authz -f Dockerfile.authz .
docker build -t my_image_content -f Dockerfile.content .

# Lancer les services avec docker-compose
docker-compose up --build
