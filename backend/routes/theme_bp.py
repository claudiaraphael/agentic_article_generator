from flask import Blueprint, jsonify
from flasgger import swag_from
from models.theme import Theme
from schemas.theme import ThemeSchema
from models import db

# theme
# id
# name
# description
# research report - agent 1
# analysis report - agent 2
# first draft - agent 3
# article - agent 4

theme_bp = Blueprint('theme', __name__)

@theme_bp.route('/theme', methods=['POST'])
@swag_from({
    'tags': ['Theme'],
    'summary': 'Receives a theme from the user input.',
    'responses': {
        '201': {
            'description': 'Anew theme.',
            'content': {
                'application/json': {
                    'schema': {
                        '$ref': '#/components/schemas/ThemeSchema'
                    }
                }
            }
        }
    }
})
def receive_theme():
    """
    Gets theme and theme description from user input and creates a new Theme entry in the database.
    """
    mock_theme = {
        "id": 1,
        "name": "Mock Theme",
        "description": "This is a mock theme for testing purposes.",
        "research_report": "This is the research report.",
        "analysis_report": "This is the analysis report.",
        "draft": "This is the draft content.",
        "article": "This is the final article."
    }
    return 200
