from flask import Blueprint, jsonify
from flasgger import swag_from
from models.article import Article
from schemas.article import ArticleSchema
from models import db

article_bp = Blueprint('article_bp', __name__)

# Mock article data
mock_articles = [
    {
        "id": 1,
        "title": "Mock Article 1",
        "research_report": "This is the research report.",
        "analysis_report": "This is the analysis report.",
        "seo_keyword_list": ["mock", "article", "testing"],
        "draft": "This is the draft content.",
        "edition": "This is the edited content.",
        "output": "This is the final output.",
        "theme_id": 1
    }
]

@article_bp.route('/articles', methods=['POST'])
@swag_from({
    'tags': ['Article'],
    'summary': 'Creates a new mock article.',
    'responses': {
        '201': {
            'description': 'A new mock article.',
            'content': {
                'application/json': {
                    'schema': {
                        '$ref': '#/components/schemas/ArticleSchema'
                    }
                }
            }
        }
    }
})
def create_article():
    """
    Creates a new mock article and returns it.
    """
    new_article = {
        "id": len(mock_articles) + 1,
        "title": "New Mock Article",
        "research_report": "New research.",
        "analysis_report": "New analysis.",
        "seo_keyword_list": ["new", "mock"],
        "draft": "New draft.",
        "edition": "New edition.",
        "output": "New output.",
        "theme_id": 2
    }
    mock_articles.append(new_article)
    return jsonify(new_article), 201

@article_bp.route('/articles', methods=['GET'])
@swag_from({
    'tags': ['Article'],
    'summary': 'Returns a list of mock articles.',
    'responses': {
        '200': {
            'description': 'A list of mock articles.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'array',
                        'items': {
                            '$ref': '#/components/schemas/ArticleSchema'
                        }
                    }
                }
            }
        }
    }
})
def get_articles():
    """
    Returns all mock articles.
    """
    return jsonify(mock_articles)