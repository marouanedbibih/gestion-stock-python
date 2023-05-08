# Gestion de Stock - README
Ce projet est une application de gestion de stock développée en Python. L'application permet de gérer les utilisateurs, les produits et fournit une interface graphique utilisateur (GUI) pour faciliter l'interaction.

## Installation

Avant de pouvoir exécuter l'application de gestion de stock, assurez-vous d'avoir installé les éléments suivants :

Python (version 3.11.2)

Les bibliothèques Python suivantes :

### mysql-connector : 
Utilisé pour la connexion à la base de données MySQL. Vous pouvez l'installer avec la commande 
pip install mysql-connector-python.
### tkinter : 
Utilisé pour créer l'interface graphique. Pour l'installer, vous pouvez exécuter la commande 
pip install tk
### tkcalendar : 
Utilisé pour afficher un calendrier dans l'interface graphique. Vous pouvez l'installer avec la commande 
pip install tkcalendar.

## Configuration
Créez une base de données (stock) MySQL (utilisez Wamp ou Xamp).

Importez le fichier SQL stock.sql situé dans le dossier sql pour créer les tables nécessaires.

Ouvrez le fichier connexion.py situé dans le dossier backend.

Modifiez les paramètres de connexion à la base de données selon vos besoins. Par exemple, vous pouvez modifier l'hôte, le nom d'utilisateur, le mot de passe et le nom de la base de données.


### Exemple de configuration de la connexion à la base de données
host = "localhost"

user = "utilisateur"

password = "mot_de_passe"

database = "nom_de_la_base_de_données"

Assurez-vous de fournir les informations correctes pour votre environnement de base de données.

## Demarage
Accédez au répertoire du projet.

Pour exécuter le système de gestion de stock, exécutez le script principal root.py.

$ python main.py


## Fonctionnalités

Le système de gestion de stock comprend les fonctionnalités suivantes :

### Backend (classe) :

Connexion : Gère la connexion à la base de données.

User : Gère les opérations liées aux utilisateurs (ajouter, supprimer, mettre à jour, afficher).

Product : Gère les opérations liées aux produits (ajouter, supprimer, mettre à jour, afficher).

### Frontend (interface graphique) :

Login : Permet aux utilisateurs de se connecter au système.

Menu : Affiche le menu principal du système.

User : Manipulation des Utilisateurs

### Acteurs 
    ### Marouane Dbibih
    ### Jaafar El-ansari

