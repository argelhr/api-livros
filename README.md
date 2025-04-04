# Documentação da API de Livros

## Introdução
Bem-vindo à documentação da API de livros. Esta API foi desenvolvida para fins de estudo e apresentação do desafio final do curso FullStack proporcionado pelo Vai na Web.

A API utiliza as tecnologias **Flask** e **SQLite** e atualmente possui três endpoints: visualizar esta documentação, cadastrar livros e listar os livros doados.

---

## Links

**Front: https://vnw-desafio-final-mod-1.vercel.app/livros_doados**
**Link da Api: https://api-livros-kdj3.onrender.com/**

---

## Endpoints

### Página Inicial
**Método:** `GET`
**Endpoint:** `/`

**Descrição:** Retorna esta documentação.

**Resposta de Sucesso (200):**
```json
Retorna um template HTML que documenta a mesma coisa desde README
```

---

### Doar um Livro
**Método:** `POST`
**Endpoint:** `/api/doar`

**Descrição:** Adiciona um novo livro ao banco de dados.

**Corpo da Requisição (JSON):**
```json
{
    "title": "Nome do Livro",
    "category": "Categoria",
    "author": "Autor",
    "image_url": "URL da Imagem"
}
```

**Resposta de Sucesso (201):**
```json
{
    "message": "Livro cadastrado com sucesso",
    "livro": {
        "id": 1,
        "title": "Nome do Livro",
        "category": "Categoria",
        "author": "Autor",
        "image_url": "URL da Imagem"
    }
}
```

---

### Listar todos os Livros
**Método:** `GET`
**Endpoint:** `/api/livros`

**Descrição:** Retorna uma lista de todos os livros cadastrados.

**Resposta de Sucesso (200):**
```json
[
    {
        "id": 1,
        "title": "Nome do Livro",
        "category": "Categoria",
        "author": "Autor",
        "image_url": "URL da Imagem"
    },
  ...
]
```

---

## Considerações Finais
#### Esta API foi desenvolvida com o propósito educacional e método de avaliação final do curso de Fullstack proposto pelo instituto Vai na web. 