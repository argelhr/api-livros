import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

            livro_inserido = conn.execute("SELECT * FROM BOOKS ORDER BY id DESC",).fetchone()
            print(livro_inserido)

        livro_inserido = {
            "id": livro_inserido[0],
            "title": livro_inserido[1],
            "category": livro_inserido[2],
            "author": livro_inserido[3],
            "image_url": livro_inserido[4]
        }


        return jsonify({"message": "Livro cadastrado com sucesso", "livro": livro_inserido}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Erro inesperado"}), 500

@app.route("/")
def home():
    return "<h1>X-tudo, batata-frita, coca trincando de gelada, strogonoff; Sempre acaba em comida, agora é a vez de voces ficar com fome :D </h1>"


@app.route("/api/livros", methods=["GET"])
def get_livros():
    try:
        with sqlite3.connect("database.db") as conn:
            livros = conn.execute("SELECT * FROM BOOKS").fetchall()

        livros_list = []
        for livro in livros:
            livros_list.append({
                "id": livro[0],
                "title": livro[1],
                "category": livro[2],
                "author": livro[3],
                "image_url": livro[4]
            })

        return jsonify(livros_list), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Erro inesperado"}), 500

if __name__ == "__main__":
    app.run(debug=True)