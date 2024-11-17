from flask import Blueprint, request, jsonify
import sqlite3

users_bp = Blueprint("users", __name__)

@users_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect("sistema_vendas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login bem-sucedido!", "user_type": user[3]})
    return jsonify({"error": "Usuário ou senha inválidos"}), 401
