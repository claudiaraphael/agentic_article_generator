from flask import jsonify

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