# 🔐 Digital Signature System

## 📜 Project Overview
This project implements a **Digital Signature System (DSS)** using **Flask** and **PyCryptodome** to securely authenticate messages. It allows users to:

✅ **Generate a Digital Signature** using DSA.  
✅ **Verify a Signature** to check authenticity.  
✅ **Use a Web Interface** for ease of use.  

---

## 🛠️ Tech Stack

- **Backend:** Flask, Python  
- **Cryptography Library:** PyCryptodome (DSA, SHA-256, DSS)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Localhost  

---

## 📂 Project Structure
```
digital_signature_project/
│── static/
│   ├── style.css          # Styling for frontend
│── templates/
│   ├── index.html         # Webpage UI
│── app.py                 # Flask Backend (DSA Implementation)
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
```



## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Nagendra0228/INS-Project.git
cd digital-signature-project
```
###2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
###3️⃣ Run the Application
```sh
python app.py
```
###4️⃣ Access the Web App
Open http://127.0.0.1:5000/ in your browser.

###📌 Features
-🔹 Sign Messages: Generates a unique signature for any input message.
-🔹 Verify Signatures: Ensures the message is authentic and untampered.
-🔹 Interactive UI: Web-based form for easy usage.
-🔹 Cryptographic Security: Uses DSA, SHA-256, and DSS (FIPS-186-3).

###🛡️ How It Works
-1️⃣ User inputs a message.
-2️⃣ SHA-256 hashes the message.
-3️⃣ Private Key signs the hash.
-4️⃣ Signature is displayed.
-5️⃣ User verifies the signature with the Public Key.
-6️⃣ If valid, the message is authenticated.

###📜 License
This project is open-source under the MIT License.
