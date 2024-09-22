J'ai crée 3 fichier .py pour chaqu'un des test.

J'ai Créer un dossier docker_images contant les dockerfiles des 3 images.

J'ai crée des images à partire d'une image ubuntu à la quel j'ai ajouté python3 et pip 
et le package request.

Dans le dossier racine contenant les fichier .py j'ai crée un fichier docker-compose.ym qui 
lance l'image de l'api ensuite il lancera les images de test.

Les containers utilisent le même network avec le port 8000 pour communiquer. 

Un volume logs est monté sur les container pour permettre de rensigner les resultats des test 
sur le même repertoire de la machine hot.

Pour lancer les services utiliser le fichier setup.sh :

1- Donner les droits necessaires au script pour le rendre exécutable
chmod +x setup.sh

2- Lancer le script dans le terminal:
./setup.sh

3- les resultats des tests sont disponibles dans le repertoire logs. 
