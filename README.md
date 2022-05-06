Ce projet a pour objet de mettre en oeuvre le processus ETL (Extract,Transform,Load) sur un site test à savoir books.toscrape.com


#création du clone du dépot et déplacement dans le répertoire du projet

"git clone https://github.com/Herve-2476/OpenClassRoomsProjet_2.git"

"cd OpenClassRoomsProjet_2"


#Mise en place de l'environnement virtuel

Dans le répertoire du projet lancer les commandes dans une console.

"python -m venv venv"   #le deuxième venv étant le nom de l'environnement que l'on retrouvera dans le .gitignore d'où le choix d'un nom générique

"source venv/bin/activate" #pour lancer votre environnement sous linux ("venv\Scripts\activate.bat" sous windows)

Remarque: Si vous avez plusieurs versions de python installées il faut préciser celle que vous souhaitez utiliser si ce n'est pas celle par défaut.Par exemple:

"python3.7 -m venv venv"

Les modules nécessaires à l'exécution sont indiqués dans le fichier requirements.txt.
Vous pouvez installez automatiquement ces modules avec la commande suivante.

"pip install -r requirements.txt"


#exécution des programmes

Le premier fichier, extraction.py va extraire les informations du site et créer les fichiers csv correspondants aux données des livres par catégorie.

Le deuxième fichier, chargement_images.py ouvre chaque fichier csv pour parcourir tous les livres et récupérer pour chaque livre l'url de l'image et télécharger cette image.

L'exécution des deux programmes doit se faire impérativement à la racine du projet.

"python extraction.py"

"python chargement_images.py"