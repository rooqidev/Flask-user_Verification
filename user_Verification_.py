# Building a User verifiecaiton API
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Message":"Hey, welcome to User Verification API!"})

# signing Up
@app.route("/add-user", methods=["POST"])
def add_User():
    user_data = request.json
    try:
        user_name = user_data["user_name"]
        user_email = user_data["user_email"]
        user_password = user_data["user_password"]
        return jsonify({"your_data": f"{user_name, user_email, user_password}"}), 200

    except Exception as e:
        return jsonify({"error":f"please provide data..{e}"}), 400

# Login / verifying 
@app.route("/login", methods=["POST"])
def login():
    user_data = request.json
    try: 
        user_name = user_data["user_name"]
        user_password = user_data["user_password"]
        return jsonify({"Success":"Checking your Data!"})

    except Exception as e:
        return jsonify({"Oops!":"Entered data is incorrect!"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
