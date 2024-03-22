from flask import Flask, request, jsonify
from Crypto.PublicKey import RSA  # Importation de la classe RSA pour la génération de clés RSA
from Crypto.Cipher import PKCS1_OAEP  # Importation de l'algorithme PKCS1 OAEP pour le chiffrement RSA
import requests

app = Flask(__name__)  # Création de l'application Flask

# Génération d'une paire de clés RSA de 2048 bits
cle_rsa = RSA.generate(2048)

# Création d'un objet de chiffrement avec la clé générée
chiffreur_rsa = PKCS1_OAEP.new(cle_rsa)

# Endpoint pour vérifier l'état de santé de l'API
@app.route('/health', methods=['GET'])
def etat_api():
    return '', 200  # Réponse vide avec un code de statut 200 pour indiquer que l'API est en santé

# Endpoint pour récupérer la clé publique RSA
@app.route('/key', methods=['GET'])
def obtenir_cle_publique():
    return cle_rsa.publickey().export_key().decode(), 200  # # Exportation de la clé publique au format PEM et envoi en réponse. J'ai fait comme ça parce 
                                                        # dans l'execice vous demandez qu'il renvoie une clé publique RSA. Donc je l'ai défini hors la fonction 
                                                        # pour que ça ne change pas pour faire codage/decodage avec la même clé.

# Endpoint pour encoder un message avec la clé publique RSA
@app.route('/encode', methods=['GET'])
def encoder_message():
    message = request.args.get('msg')  # Récupération du message à encoder depuis la requête URL
    if message:
        # Récupération de la clé publique depuis /cle en utilisant une requête HTTP
        reponse = requests.get('http://localhost:5000/key')
        cle_recue = RSA.import_key(reponse.text)  # Importation de la clé publique reçue
        chiffreur_rsa = PKCS1_OAEP.new(cle_recue)  # Création d'un nouvel objet de chiffrement avec la clé publique reçue

        # Encodage du message avec la clé publique récupérée
        message_encode = chiffreur_rsa.encrypt(message.encode())
        return jsonify({'message_encode': message_encode.hex()}), 200  # Envoi du message encodé en réponse
    else:
        return 'Aucun message fourni', 400  # Message d'erreur si aucun message n'est fourni dans la requête

# Endpoint pour décoder un message avec la clé publique RSA
@app.route('/decode', methods=['GET'])
def decoder_message():
    message_encode = request.args.get('msg')  # Récupération du message encodé depuis la requête URL
    if message_encode:
        message_decode = chiffreur_rsa.decrypt(bytes.fromhex(message_encode))  # Déchiffrement du message encodé
        return jsonify({'message_decode': message_decode.decode()}), 200  # Envoi du message décodé en réponse
    else:
        return 'Aucun message fourni', 400  # Message d'erreur si aucun message n'est fourni dans la requête

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Démarrage de l'application Flask sur le port 5000 en mode debug
