from app.app import db

class Noodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(1000))
    name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    spiciness = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    noodles = db.relationship('Noodle', backref='category', lazy=True)