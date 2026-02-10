from flask import Flask, render_template, request, redirect, url_for
from models import db, Review

app = Flask(__name__)

# DB 설정
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# DB 생성
with app.app_context():
    db.create_all()

    @app.route("/")
def index():
    reviews = Review.query.all()
    return render_template("index.html", reviews=reviews)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        review = Review(
            title=request.form["title"],
            category=request.form["category"],
            rating=request.form["rating"],
            content=request.form["content"]
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html")

@app.route("/review/<int:id>")
def detail(id):
    review = Review.query.get_or_404(id)
    return render_template("detail.html", review=review)

if __name__ == "__main__":
    app.run(debug=True)