import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS BOOKS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT NOT NULL,  
                    category TEXT NOT NULL,  
                    author TEXT NOT NULL,  
                    image_url TEXT NOT NULL  
                )
            """
        )

init_db()

@app.route("/api/doar", methods=["POST"])
def save():
    try:
        dados = request.get_json()

        title = dados.get("title")
        category = dados.get("category")
        author = dados.get("author")
        image_url = dados.get("image_url")

        if not title or not category or not author or not image_url:
            return jsonify({"error": "Todos os campos são obrigatórios"}), 400

        with sqlite3.connect("database.db") as conn:
            conn.execute(f"""
            INSERT INTO BOOKS (title, category, author, image_url) 
            VALUES ("{title}", "{category}", "{author}", "{image_url}")
            """)

            conn.commit()

        return jsonify({"message": "Livro cadastrado com sucesso"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Erro inesperado"}), 500


if __name__ == "__main__":
    app.run(debug=True)