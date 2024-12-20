from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import jwt
import datetime
import os
from functools import wraps

app = Flask(__name__)
CORS(app)

# Use environment variable for SECRET_KEY
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-dev-secret-key')

# Update database path for Render
DB_PATH = os.path.join(os.getcwd(), 'users.db')

# Database initialization
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Rest of your Flask code remains the same...

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)