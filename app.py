from flask import Flask, render_template, request, jsonify
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
import binascii

app = Flask(__name__)

# Generate DSA Key Pair (Static for now, can be regenerated per session)
key = DSA.generate(2048)
public_key = key.publickey()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign_message():
    try:
        message = request.form['message'].encode()  # Get input message from frontend
        hash_obj = SHA256.new(message)  # Hash the message
        signer = DSS.new(key, 'fips-186-3')  
        signature = signer.sign(hash_obj)  # Generate Signature
        
        return jsonify({
            'message': message.decode(),
            'hash': hash_obj.hexdigest(),
            'signature': binascii.hexlify(signature).decode()  # Convert bytes to hex for display
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/verify', methods=['POST'])
def verify_signature():
    try:
        message = request.form['message'].encode()
        received_signature = binascii.unhexlify(request.form['signature'])  # Convert hex back to bytes

        hash_obj = SHA256.new(message)  
        verifier = DSS.new(public_key, 'fips-186-3')  

        verifier.verify(hash_obj, received_signature)  # Verify signature
        return jsonify({'status': '✅ Signature is valid!'})
    except ValueError:
        return jsonify({'status': '❌ Signature is invalid!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
