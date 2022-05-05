Ce projet a pour objet de mettre en oeuvre le processus ETL (Extract,Transform,Load) sur un site test à savoir books.toscrape.com
#Mise en place de l'environnement virtuel
Dans le répertoire du projet lancer les commandes dans une console.
python -m venv venv   #le deuxième venv étant le nom de l'environnement que l'on retrouvera dans le .gitignore d'où le choix d'un nom générique
source venv/bin/activate #pour lancer votre environnement sous linux (venv\Scripts\activate.bat sous windows)
Remarque: Si vous avez plusieurs versions de python installées il faut préciser celle que vous souhaitez utiliser si ce n'est pas celle par défaut. Ex = python3.7 -m venv venv
