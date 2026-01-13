from models import db

class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Template {self.name}>"
