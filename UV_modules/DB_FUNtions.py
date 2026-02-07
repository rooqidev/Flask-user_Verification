#from UV_FUCTions.DB_modules import create_UV_Table, registeration, login, delete_user
import sqlite3
import os
import hashlib
import binascii
import hmac

UV_DB = "UV_DB.db"
DEFAULT_ITERATION = 100_000

def generate_Salt():
    return binascii.hexlify(os.urandom(16)).decode()

def hash_password(password: str, salt: str, iterations: int = DEFAULT_ITERATION):
    return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt.encode(),
            iterations
            ).hex()


def get_Connection():
    conn = sqlite3.connect(UV_DB)
    conn.row_factory = sqlite3.Row
    return conn

def create_UV_Table():
    conn = get_Connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS UV_DB(

    username TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    iterations INTEGER NOT NULL

    )
                   """)
    conn.commit()
    conn.close()

def registeration(usename, email, password):
    salt = generate_Salt()
    password_hash = hash_password(password, salt, DEFAULT_ITERATION)
    conn = get_Connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO UV_DB (username, email, password_hash, salt, iterations) VALUES (?, ?, ?, ?, ?)", (username, email, password_hash, salt, DEFAULT_ITERAION))
        conn.commit()

    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def login(username, password):
    conn = get_Connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password_hash, salt, iterations FROM UV_DB WHERE username = ?", (username,))
        row = cursor.fetchone()
        stored_hash, salt, iterations = row
        input_hash = hash_password(password, salt, iterations)
        if hmac.compare_digest(stored_hash, input_hash):
            conn.close()
            return True

    except Exception as e:
        conn.close()
        return False


def delete_user(username, password):
    conn = get_Connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password_hash, salt, iterations FROM UV_DB WHERE username = ?", (username,))
        row = cursor.fetchone()
        stored_hash, salt, iterations = row
        input_hash = hash_password(password, salt, iterations)
        if hmac.compare_digest(stored_hash, input_hash):
            cursor.execute("DELETE FROM UV_DB WHERE username = ?", (username,))
            conn.commit()
            conn.close()
            return True

    except Exception as e:
        conn.close()
        return False




