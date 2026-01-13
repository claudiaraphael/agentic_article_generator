from models import db

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Relationship to Article
    articles = db.relationship('Article', backref='theme', lazy=True)

    def __repr__(self):
        return f"<Theme {self.name}>"
