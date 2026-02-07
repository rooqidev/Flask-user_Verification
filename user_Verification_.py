# Building a User verifiecaiton API
from flask import Flask, jsonify, request
from UV_FUCTions.DB_modules import registeration, login, delete_user
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"Message":"Hey, welcome to User Verification API!"}), 204

# signing Up
@app.route("/add-user", methods=["POST"])
def add_User():
    user_data = request.json
    try:
        user_name = user_data["user_name"]
        user_email = user_data["user_email"]
        user_password = uer_data["user_password"]
        registered = registeration(user_name, user_email, user_password)
        if registered:
            return jsonify({"Success":"User registered succesfully!"}), 202
        else:
            return jsonify({"Failed":"User already exists!"}), 404

    except Exception as e:
        return jsonify({"error":f"please provide data..{e}"}), 400

# Login / verifying 
@app.route("/login", methods=["POST"])
def login():
    user_data = request.json
    try: 
        user_name = user_data["user_name"]
        user_password = user_data["user_password"]
        verified = login(user_name, user_password)
        if verified:
            return jsonify({"Success":"User login sucessfully!"}), 201
        else:
            return jsonify({"Failed":"User is'nt registered!!"}), 403

    except Exception as e:
        return jsonify({"Oops!":"Entered data is incorrect!"}), 401

@app.route("/delete-user", methods=["POST"])
def delete_User():
    user_data = request.json
    try:
        user_email = user_data["user_email"]
        user_password = user_data["user_password"]
        deleted = delete_user(user_email, user_password)
        if deleted:
            return jsonify({"success":"User deleted succesfully!"}), 205
        else:
            return jsonify({"error":"Oops! user already is'nt registered!"}), 406
    except Exception as e:
        return jsonify({"Oops!":"Entered data is incorrect!"}), 407


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
