from models import db

class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    # Foreign Key to link to an Article
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    
    # Relationship
    article = db.relationship('Article', backref=db.backref('drafts', lazy=True))

    def __repr__(self):
        return f"<Draft {self.name}>"
