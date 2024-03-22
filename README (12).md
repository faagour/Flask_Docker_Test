# Test Technique - Justification des Choix


## Choix de l'Application


Pour répondre aux besoins du test technique, j'ai choisi de développer une application web en utilisant le framework Flask afin de developper mes compétences en Flask parce que j'ai jamais travaillé avec et parce que c'est un framework minimaliste je trouve qui permet de garder le code simple et léger, et parce que c'est facile à apprendre et à utiliser.

## Endpoints de l'Application

- GET /health: Cet endpoint renvoie une réponse vide avec un statut 200 pour indiquer que l'API est en bonne santé. Cela permet de vérifier facilement si l'application fonctionne correctement. Alors pour tester ça, j'ai utilisé Postman afin de voir si on reçoit le statut 200. Le fait que ça donne une page vide n'implique pas nécessairement qu on aura le statut 200. C'est pour cela pour toutes les requetes de ce projet, j'ai utilisé Postman.

- GET /key: Cet endpoint renvoie la clé publique RSA générée par l'application. La clé est exportée au format PEM et envoyée en réponse. Exportation de la clé publique au format PEM et envoi en réponse. Dans cette partie, j'ai défini la clé générée hors la fonction pour faire codage/decodage avec la même clé.

- GET /decode: Cet endpoint décode un message encodé avec la clé publique récupérée depuis /key. Le message est lu depuis le paramètre de requête "msg". Pour cela, j'ai utilisé une requête HTTP pour récupérer la clé publique, puis j'ai déchiffré le message encodé avec cette clé. Avant de réaliser cela, j'ai défini aussi : 

- GET /encode : Cet endpoint code un message avec la clé publique récupérée depuis /key. Le message est lu depuis le paramètre de requête "msg". Pour cela, j'ai utilisé une requête HTTP pour récupérer la clé publique, puis j'ai codé le message avec cette clé.

Alors pour tester que mon code/decode fonctionne très bien, après avoir codé un message donné par exemple "hello world", je copie le résultat affiché (message codé) . Et ensuite je la colle dans msg de la requete de decode pour voir si j'aurai le résultat initial (message de départ). C'est ce que j'ai obtenu.


## Choix des Bibliothèques
Pour la génération de clés RSA et le chiffrement/déchiffrement des messages, j'ai utilisé la bibliothèque pycryptodome. Cette bibliothèque est une implémentation en Python de nombreux algorithmes de cryptographie, y compris RSA et PKCS1 OAEP que j ai utilisé dans ce projet.

J'ai également utilisé la bibliothèque requests pour effectuer des requêtes HTTP dans Python. J'ai opté pour cette solution car dans les spécifications de l'endpoint /key, il était indiqué que je devais récupérer la clé publique en utilisant une requête GET. Mais dans mon code, c'était un peu forcé genre il y avait moyen de ne pas l'utiliser vu que ma clé se trouve hors les fonctions mais je l'ai fait quand même.


## Dockerisation de l'Application
J'ai dockerisé l'application en utilisant Dockerfile. Voilà quelques éléments et choix faits :

- Choix de l'Image de Base: J'ai utilisé l'image de base python:3.9-alpine. J'ai choisi Alpine pour sa légèreté et sa rapidité de téléchargement. elle est suffisamment complète pour nos besoins dans ce projet.

- Définition du Répertoire de Travail: J'ai défini le répertoire de travail dans le conteneur comme étant /app.

- Installation des Dépendances: J'ai copié le fichier requirements.txt dans le conteneur et j'ai installé les dépendances Python nécessaires en utilisant pip. dans requirements.txt, j'ai créé un dossier vierge que j'ai rempli avec les requirments qui sont obligatoires pour mon projet. Dans le commande pour installer les dépendances, j'ai ajouté : --no-cache-dir pour m'assurer que j installe toujours les dernières versions des dépendances sans utiliser de cache local parce que à chaque je crée de nouvelles images pour tester mon code.

- Exposition du Port: J'ai exposé le port 5000 sur le conteneur pour permettre l'accès à l'application Flask.

Dans ce projet, il n'y a pas beaucoup d'éléments (un petit projet) donc on avait moinds d'éléments dans le dockerfile. Par contre dans un grand projet il faut faire attention à l'ordre des lignes dans le dockerfile. par exemple les elements qui restent dans le cache et ceux qui n en restent pas. dans ce cas il faudra commencer par le cache d'abord

## Exécution et Démarrage: 

Pour construire et exécuter l'application à l'aide de Docker, voici quelques commandes que j'ai utilisées dans ce projet :

- Construction de l'Image:  la commande docker build -t myapp . pour construire l'image Docker. Cette commande construit l'image à partir du Dockerfile présent dans le répertoire courant (.) et lui donne le nom myapp

- Exécution du Conteneur:  la commande docker run -p 5000:5000 myapp pour exécuter le conteneur Docker. Cette commande mappe le port 5000 du conteneur sur le port 5000 de l'hôte.

J'ai utilisé Docker Desktop pour supprimer et executer des images créés parce que c'était facile un peu au début. Par contre, au final j'ai utilisé la commande rmi ; docker rmi myapp. mais un astuce c est que avant de supprimer un container on l'arrête d'abord

Ces choix et commandes permettent de dockeriser et exécuter l'application de manière efficace et portable.


Dans ce projet, Docker Compose n'a pas été utilisé grâce à la simplicité du projet : Étant donné la taille relativement petite du projet et son caractère simple, l'utilisation de Docker Compose aurait introduit une complexité inutile malgré le fait qu'il simplifie un peu (la commande docker-compose up semble simple surtout quand on a plusieurs containers).

## Authors

Fouad AAGOUR

- [@faagour](https://www.github.com/faagour)


