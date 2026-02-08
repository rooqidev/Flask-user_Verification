# Flask User Verification API

A simple **Flask-based API** for user registration, login, and verification, with secure password hashing and SQLite integration.

This is my **first live backend project** — deployed on PythonAnywhere!

## 🚀 Live Demo
Check it out here: [Flask User Verification API](https://rooqidev.pythonanywhere.com)

## 💡 Features

- User registration with **secure password hashing** (PBKDF2 + salt)
- User login and verification
- SQLite database for storage
- Lightweight and easy to extend
- Git-based project history for version tracking

## 📂 Project Structure

Flask-user_Verification/ ├── app.py # Main Flask app ├── UV_modules/ # Helper modules │ └── UV_FUNCTIONS.py # Database functions └── UV_DB.db # SQLite database

---

## 🔗 Endpoints

| Endpoint | Method | Description |
|-----------------|--------|-------------------------------|
| `/add-user` | POST | Register a new user with username/email/password|
| `/login` | POST | Login with username/password |
| `/verify` | POST | Verify user account with username/password|

> Last endpoint '/delete-user' is currently under refinement..

## 🛠 Tech Stack

- **Flask** – Lightweight Python web framework
- **SQLite** – Lightweight database
- **PBKDF2 + binascii** – Secure password hashing
- **Python 3.12** – Programming language

## 📌 Example Requests
You can test the API using curl, Postman, or Python requests.
Example with Python `requests` module:

```python
import requests

url = "https://rooqidev.pythonanywhere.com/add-user"
data = {"user_name": "test_user", "user_email":"test_user@gmail", "user_password": "mtsetassword"}
response = requests.post(url, json=data)
print(response.json())

> Screenshots of requests are available in the screenshots/ folder.


💾 How to Run Locally

1. Clone the repo:

git clone https://github.com/rooqidev/Flask-user_Verification.git
cd Flask-user_Verification

2. Create virtual environment:

python3 -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows

3. Install requirements:

pip install flask

4. Run locally:

python app.py

> Note: Dont add app.run() line if deploying via WSGI (PythonAnywhere).

🔧 Future Improvements

Refine the last endpoint
Add token-based authentication
Enhance error handling

📜 License

This project is open for learning and experimentation. Feel free to fork and improve!


