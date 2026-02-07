from flask_smorest import Blueprint, abort
from schemas import BookSchema

blp = Blueprint(
    "books",
    "books",
    url_prefix="/books",
    description="Operations on books"
)

# 메모리 데이터 저장소
books = []
book_id_counter = 1


@blp.route("/")
class Books:
    @blp.response(200, BookSchema(many=True))
    def get(self):
        """책 목록 조회"""
        return books

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, book_data):
        """새 책 추가"""
        global book_id_counter

        book = {
            "id": book_id_counter,
            **book_data
        }
        book_id_counter += 1
        books.append(book)
        return book


@blp.route("/<int:book_id>")
class BookById:
    @blp.response(200, BookSchema)
    def get(self, book_id):
        """특정 책 조회"""
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            abort(404, message="Book not found")
        return book

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, book_data, book_id):
        """책 정보 수정"""
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            abort(404, message="Book not found")

        book.update(book_data)
        return book

    @blp.response(204)
    def delete(self, book_id):
        """책 삭제"""
        global books
        book = next((b for b in books if b["id"] == book_id), None)
        if not book:
            abort(404, message="Book not found")

        books = [b for b in books if b["id"] != book_id]
        return ""