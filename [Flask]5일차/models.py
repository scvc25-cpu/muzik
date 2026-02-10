from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(10), nullable=False)  # 책 / 영화
    rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Review {self.title}>"