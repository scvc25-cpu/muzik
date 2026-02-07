from flask import Flask
from flask_smorest import Api
from api import blp as BooksBlueprint

def create_app():
    app = Flask(__name__)

    # Flask-Smorest 필수 설정
    app.config["API_TITLE"] = "Book API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(BooksBlueprint)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)