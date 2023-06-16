from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Noodle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    spiciness = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    noodles = db.relationship('Noodle', backref='category', lazy=True)

@app.route('/', methods=['GET'])
def home():
    company_filter = request.args.get('company')
    spiciness_filter = request.args.get('spiciness')

    query = Noodle.query.join(Category)

    if company_filter:
        query = query.filter(Category.company == company_filter)
    if spiciness_filter:
        query = query.filter(Noodle.spiciness == spiciness_filter)

    noodles = query.all()
    categories = Category.query.distinct().all()
    spiciness_values = [x[0] for x in db.session.query(Noodle.spiciness).distinct()]

    return render_template('index.html', noodles=noodles, categories=categories, spiciness_values=spiciness_values)

@app.route('/submit_review', methods=['GET', 'POST'])
def submit_review():
    if request.method == 'POST':
        name = request.form['name']
        review = request.form['review']
        rating = request.form['rating']
        spiciness = request.form['spiciness']
        company_id = request.form['company']

        new_review = Noodle(name=name, review=review, rating=rating, spiciness=spiciness, category_id=company_id)
        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('home'))

    categories = Category.query.all()
    return render_template('submit_review.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)

