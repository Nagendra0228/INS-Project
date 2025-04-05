# Flask Email Signature App ✉️🔐

A secure and user-friendly Flask web application that allows users to generate cryptographic digital signatures for messages and sends the signed message to a specified email address.

## 🚀 Features

- 🔏 **Digital Signature Generation**: Uses RSA cryptography to generate a secure digital signature for the message.
- 📧 **Email Integration**: Sends the original message and its signature to the provided email address using SMTP.
- 🌐 **Web Interface**: Clean and responsive frontend built with HTML and CSS.
- 🔒 **Environment Variable Security**: Sensitive credentials are managed securely using a `.env` file.

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Security**: RSA (from `cryptography` package)
- **Email**: SMTP (Simple Mail Transfer Protocol)

## 📂 Project Structure

```
INS Project/
│
├── app.py             # Main Flask backend application
├── .env               # Environment variables (not committed)
├── Media/  
│   └── Demo.mp4       #Demo of the project           
├── templates/
│   └── index.html     # HTML form for input
├── static/
│   └── style.css      # CSS styling
└── Report.pdf         #Report of the project
└── README.md          # Project documentation
 
```

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-email-signer.git
cd flask-email-signer
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have `requirements.txt`, run:
> `pip install flask cryptography python-dotenv`

### 4. Set up environment variables

Create a `.env` file in the root directory with the following:

```env
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_password_or_app_password
```

> ⚠️ If using Gmail, make sure 2-Step Verification is OFF or use an [App Password](https://support.google.com/accounts/answer/185833?hl=en).

### 5. Run the application

```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000/`.

## 🧪 Example

1. Enter a message and email address.
2. Click “Generate Signature”.
3. Check the email inbox for the signed message and the signature.

## 🛡️ Security Note

- Never commit `.env` files containing sensitive credentials.
- Always use app passwords or OAuth for production environments.

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Cryptography](https://cryptography.io/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

Made with ❤️ for secure communication.
