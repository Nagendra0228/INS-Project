from flask import Flask, request, render_template, jsonify
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


app = Flask(__name__)

# Key generation
key = DSA.generate(2048)
pub_key = key.publickey()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_signature', methods=['POST'])
def generate_signature():
    message = request.form['message'].encode()
    email = request.form['email']

    # Create hash and signature
    h = SHA256.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(h)

    # Send email
    send_email(email, message.decode(), signature.hex())

    return jsonify({'signature': signature.hex(), 'message': message.decode()})

@app.route('/verify_signature', methods=['POST'])
def verify_signature():
    message = request.form['message'].encode()
    signature_hex = request.form['signature']
    signature = bytes.fromhex(signature_hex)

    h = SHA256.new(message)
    verifier = DSS.new(pub_key, 'fips-186-3')

    try:
        verifier.verify(h, signature)
        return jsonify({'result': '✅ Signature is valid!'})
    except ValueError:
        return jsonify({'result': '❌ Signature is NOT valid.'})

def send_email(to, message, signature):
    from_email = EMAIL_ADDRESS
    password = EMAIL_PASSWORD

    content = f"Message: {message}\nDigital Signature: {signature}"
    msg = MIMEText(content)
    msg['Subject'] = "Your Digital Signature"
    msg['From'] = from_email
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
