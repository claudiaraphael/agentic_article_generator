# Application Factory
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from pydantic import ValidationError

from models import db
from models.article import Article
from models.drafts import Draft
from models.templates import Template
from models.theme import Theme

# Import Schemas
from schemas.theme import ThemeCreate
from schemas.article import ArticleSchema

from routes.article import article_bp

# create the application


def create_app():
    """
    Creates and configures the Flask application, integrating OpenAPI 3.0.
    """

    # config: create an object with metadata for OpenAPI
    info = {
        'title': 'Agentic Article Automator for Linkedin',
        'version': '0.1',
        'description': 'Agentic workflow that automates article generation and (optimizes the content for SEO)'
    }

    # create flask application and initialize OpenAPI
    app = Flask(__name__)

    # Flask and SQLAlchemy Configuration: criar a base de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///article-generator.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Swagger Configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }

    swagger_template = {

        "info": {
            "title": "Agentic Article Generator",
            "description": "Agentic workflow that automates article generation and (optimizes the content for SEO)",
            "version": "0.1",

            "schemes": ["http"],
            "tags": [
                {
                    "name": "Theme",
                    "description": "Recebe o input tema do usuario",
                },
                {
                    "name": "Research",
                    "description": "Faz pesquisa sobre o tema com o mcp",
                },
                {
                    "name": "Analysis",
                    "description": "analyses research report and generates critical and technical analysis",
                },
                {
                    "name": "Draft",
                    "description": "Operações relacionadas a usuários",
                },
                {
                    "name": "Edit",
                    "description": "Operações relacionadas a comentários",
                },
                {
                    "name": "Write",
                    "description": "output the article",
                },
                {
                    "name": "Article",
                    "description": "Operations related to articles"
                },

            ]
        }
    }

    # Inicializar Swagger
    Swagger(app, config=swagger_config, template=swagger_template)

    # Initialize DB
    db.init_app(app)

    # CORS Configuration: connect front end to back end
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:5500"],  # Frontend origin
            "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Create database tables
    with app.app_context():
        db.create_all()

    # Route Registration (Blueprints)
    # from routes.product_bp import product_bp
    # from routes.user_bp import user_bp
    # from routes.comment_bp import comment_bp
    from routes.theme import theme_bp
    from routes.article import article_bp

    app.register_blueprint(theme_bp, url_prefix='/api')
    app.register_blueprint(article_bp, url_prefix='/api')

    @app.route('/research-theme')
    def generate_article(theme: str):
        return theme
    
    generate_article('mock-theme')

    
    # CRUD
    # CREATE
    @app.route('/articles', methods=['POST'])
    def create_article():
        try:
            data = request.get_json()
            article_schema = ArticleSchema()
            article_data = article_schema.load(data)

            new_article = Article(**article_data)
            db.session.add(new_article)
            db.session.commit()

            return article_schema.jsonify(new_article), 201
        except ValidationError as ve:
            return jsonify({"error": ve.errors()}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
