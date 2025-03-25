from flask import Flask, request, jsonify
from app.database import get_db_connection, init_db
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/init', methods=['GET'])
def initialize_database():
    # Vulnerable: Endpoint público para inicializar base de datos
    init_db()
    return jsonify({"status": "Database initialized"})

@app.route('/users', methods=['GET'])
def get_users():
    # Vulnerable: Sin autenticación ni autorización
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route('/login', methods=['POST'])
def login():
    # Vulnerable: Inyección SQL potencial
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    
    conn = get_db_connection()
    # Vulnerable: Consulta directa sin preparación
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = conn.execute(query).fetchone()
    conn.close()
    
    if user:
        return jsonify({
            "status": "Login successful", 
            "is_admin": bool(user['is_admin'])
        })
    return jsonify({"status": "Login failed"}), 401

@app.route('/change_password', methods=['POST'])
def change_password():
    # Vulnerable: Sin validación de token/sesión
    username = request.json.get('username')
    new_password = request.json.get('new_password')
    
    conn = get_db_connection()
    # Vulnerable: Actualización directa sin verificación
    conn.execute(
        "UPDATE users SET password = ? WHERE username = ?", 
        (new_password, username)
    )
    conn.commit()
    conn.close()
    
    return jsonify({"status": "Password changed"})