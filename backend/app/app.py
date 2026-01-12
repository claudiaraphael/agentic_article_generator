# Application Factory
from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

# import db
# import data models to create data base tables
# os modelos de dados sao as entidades em forma de classes que sao tabelas no banco de dados
# from models.article import Article
# from models.drafts import Drafts
# from models.templates import Templates
# from models.theme import Theme

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

            ]
        }
    }

    # Inicializar Swagger
    Swagger(app, config=swagger_config, template=swagger_template)

    # db.init_app(app) initializes the SQLAlchemy database with the Flask app
    # db.init_app(app)

    # CORS Configuration: connect front end to back end
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:5500"],  # Frontend origin
            "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Database Initialization
   #  with app.app_context():
    #   db.create_all()

    # Route Registration (Blueprints)
    # from routes.product_bp import product_bp
    # from routes.user_bp import user_bp
    # from routes.comment_bp import comment_bp

    @app.route('/generate-article')
    def generate_article():
        return 'Article Generator Online'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
