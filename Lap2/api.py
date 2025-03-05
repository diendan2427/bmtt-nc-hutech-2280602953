from flask import Flask, request, jsonify
from Cipher.Caesar import CeasarCipher
app = Flask(__name__)

Ceasar_cipher = CeasarCipher()

@app.route("/api/Caesar/encrypt", methods=["POST"])
def ceasar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = Ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})


@app.route("/api/Caesar/decrypt", methods=["POST"])
def ceasar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = Ceasar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})


#main function
if __name__ == "__main__":
    app.run(host ="0.0.0.0", port=5000, debug=True)

