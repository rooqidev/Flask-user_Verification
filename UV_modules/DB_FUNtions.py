#from UV_FUCTions.DB_modules import create_UV_Table, registeration, login, delete_user
import sqlite3
import os
import hashlib
import binascii
import hmac

# initiallizing a databae and default iterstion for password hashing 
UV_DB = "UV_DB.db"
DEFAULT_ITERATION = 100_000


def generate_Salt():
    #generating hash for password
    return binascii.hexlify(os.urandom(16)).decode()
    
    # now merging that hash with user passord & default iterations
def hash_password(password: str, salt: str, iterations: int = DEFAULT_ITERATION):
    return hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt.encode(),
            iterations
            ).hex()


# setuping up SQLITE3
def get_Connection():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, UV_DB)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_UV_Table():
    # creating tablw for UV_DB
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

# this function is addding user to the database, & required username, email, password for making hash, 
def registeration(username, email, password):
    salt = generate_Salt()
    password_hash = hash_password(password, salt, DEFAULT_ITERATION)
    conn = get_Connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO UV_DB (username, email, password_hash, salt, iterations) VALUES (?, ?, ?, ?, ?)", (username, email, password_hash, salt, DEFAULT_ITERATION))
        conn.commit()

    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

# This funtion is checking through database, wether this user exits or not, by comparing hash of this user with his given password
def user_Login(username, password):
    conn = get_Connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt, iterations FROM UV_DB WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        return False

    stored_hash, salt, iterations = row
    input_hash = hash_password(password, salt, iterations)

    if hmac.compare_digest(stored_hash, input_hash):
        return True
    return False

# I think, you already guessed, this funtion is deleting a user if he registeed already, otherwise it will return  message like "User already is'nt exosts"
def delete_user(user_email, password):
    conn = get_Connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash, salt, iterations FROM UV_DB WHERE email = ?", (user_email,))
    row = cursor.fetchone()
    if not row:
        return False

    stored_hash, salt, iterations = row
    input_hash = hash_password(password, salt, iterations)

    if hmac.compare_digest(stored_hash, input_hash):
        cursor.execute("DELETE FROM UV_DB WHERE email = ?", (user_email,))
        conn.commit()
        conn.close()
        return True
    return False



