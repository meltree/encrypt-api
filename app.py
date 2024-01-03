from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def encrypt_string(text: str, key, alphabet):
    try:
        encrypted_string = ''
        for letter in text:
            index = alphabet.index(letter)
            encrypted_string += key[index]
        return encrypted_string
    except:
        return 400
    
def decrypt_string(text: str, key, alphabet):
    try: 
        decrypted_string = ''
        for letter in text:
            index = key.index(letter)
            decrypted_string += alphabet[index]
        return decrypted_string
    except:
        return 400

def generate_key():
    import random

    alphabet = open('alphabet.txt', 'r').readline()
    random_string = ''

    counter = 0
    for i in alphabet:
        random_letter = random.choice(alphabet)
        random_string += random_letter
        alphabet = alphabet.replace(random_letter, '', 1)
        counter += 1

    return random_string

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    json = request.json
    key = json['key']
    text = json['text']
    
    if not key or not text:
        return 'no key or string given'
    
    es = encrypt_string(text, key, open('alphabet.txt', 'r').readline())
    
    response = {'status': 200 if es != 400 else 400}
    response = {**response, **({'string': es} if es != 400 else {})}
    
    return jsonify(response)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    json = request.json
    key = json['key']
    text = json['text']
    
    if not key or not text:
        return 'no key or string given'

    return decrypt_string(text, key, open('alphabet.txt', 'r').readline())

@app.route('/gen_key')
def gen_key_route():
    return generate_key()

@app.route('/')
def index():
    return render_template('index.html')

app.run('127.0.0.1', 9999, debug=True)