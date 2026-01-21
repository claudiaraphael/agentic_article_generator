from flask import jsonify
from flasgger import swag_from
from models.theme import Theme
from schemas.theme import ThemeSchema
from models import db

templates_bp = Blueprint('template', __name__)


@templates_bp.route('/template', methods=['GET'])
@swag_from({
    'tags': ['Template'],
    'summary': 'Shows a template.',
    'responses': {
        '201': {
            'description': 'Shows a template.',
            'content': {
                'application/json': {
                    'schema': {
                        '$ref': '#/components/schemas/TemplateSchema'
                    }
                }
            }
        }
    }
})

def article_template():
    """
    Returns a mock article template.
    """
    mock_template = {
        "id": 1,
        "title": "Article Template",
        "sections": [
            "Introduction",
            "Main Content",
            "Conclusion"
        ],
        "placeholders": {
            "Introduction": "Write an engaging introduction here.",
            "Main Content": "Provide the main content here.",
            "Conclusion": "Summarize the article here."
        }
    }
    return jsonify(mock_template), 200


