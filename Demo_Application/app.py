from flask  import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


book_list = [
  {
    "book_id": 1,
    "language": "English",
    "book_title": "To Kill a Mockingbird",
    "author": "Harper Lee"
  },
  {
    "book_id": 2,
    "language": "French",
    "book_title": "Les Misérables",
    "author": "Victor Hugo"
  },
  {
    "book_id": 3,
    "language": "Spanish",
    "book_title": "Cien años de soledad",
    "author": "Gabriel García Márquez"
  },
  {
    "book_id": 4,
    "language": "German",
    "book_title": "Der Vorleser",
    "author": "Bernhard Schlink"
  },
  {
    "book_id": 5,
    "language": "Japanese",
    "book_title": "ノルウェイの森",
    "author": "Haruki Murakami"
  },
  {
    "book_id": 6,
    "language": "Russian",
    "book_title": "Война и мир",
    "author": "Leo Tolstoy"
  },
  {
    "book_id": 7,
    "language": "Chinese",
    "book_title": "活着",
    "author": "Yan Mo"
  },
  {
    "book_id": 8,
    "language": "Italian",
    "book_title": "La ragazza di Bube",
    "author": "Carlo Cassola"
  },
  {
    "book_id": 9,
    "language": "Portuguese",
    "book_title": "O Alquimista",
    "author": "Paulo Coelho"
  },
  {
    "book_id": 10,
    "language": "Arabic",
    "book_title": "ألف ليلة وليلة",
    "author": "Unknown (Arabian Nights)"
  }
]


@app.route("/")
def hello():
    return "Creating Flask RESTAPI's"

@app.route("/books",methods=["GET","POST"])
# View function
def books():
    if request.method=="GET":
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            "nothing Found 404 error"
    if request.method=="POST":
        new_book_language = request.form['language']
        new_book_title = request.form['title']
        new_book_auther_name = request.form['author']
        iD = book_list[-1]['book_id']+1
        
        new_obj = {
            "book_id": iD,
            "language":new_book_language,
            "author":new_book_auther_name,
            "title":new_book_title
        }
        book_list.append(new_obj)
        return jsonify(book_list)

@app.route("/book/<int:id>",methods =["GET","PUT","DELETE"])
def single_book(id):
    if request.method =="GET":
        for book in book_list:
            if book["book_id"] == id:
                return jsonify(book_list)
            pass
            if request.method == "PUT":

                for book in book_list:
                    if book["book_id"]==id:
                     new_book_language = request.form['language']
                     new_book_title = request.form['title']
                     new_book_auther_name = request.form['author']
                     updated_book = {
                            "book_id": id,
                            "language":new_book_language,
                            "author":new_book_auther_name,
                            "title":new_book_title
                                }
                     return jsonify(updated_book)
        if request.method=="DELETE":
            for index, book in enumerate(book_list):
                if book["book_id"] == id:
                    book.remove(index)
                    return jsonify(book)

# @app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
# def single_book(id):
#     if request.method == "GET":
#         for book in book_list:
#             if book["book_id"] == id:
#                 return jsonify(book)
#         return jsonify({"message": "Book not found"}), 404

#     elif request.method == "PUT":
#         for book in book_list:
#             if book["book_id"] == id:
#                 data = request.json
#                 book["language"] = data.get("language", book["language"])
#                 book["book_title"] = data.get("title", book["book_title"])
#                 book["author"] = data.get("author", book["author"])
#                 return jsonify(book)
#         return jsonify({"message": "Book not found"}), 404

    # elif request.method == "DELETE":
    #     for book in book_list:
    #         if book["book_id"] == id:
    #             book_list.remove(book)
    #             return jsonify({"message": "Book deleted successfully"})
    #     return jsonify({"message": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)