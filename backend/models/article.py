from models import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    research_report = db.Column(db.Text, nullable=True)
    analysis_report = db.Column(db.Text, nullable=True)
    seo_keyword_list = db.Column(db.JSON, nullable=True)
    draft = db.Column(db.Text, nullable=True)
    edition = db.Column(db.Text, nullable=True)
    output = db.Column(db.Text, nullable=True)
    
    # Foreign Key to link to the Theme
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'), nullable=False)

    def __repr__(self):
        return f"<Article {self.id}>"