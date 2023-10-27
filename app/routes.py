from app.app import app, db
from flask import request, redirect, render_template, url_for
from app.models import Category, Noodle

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

    return render_template('index.html', noodles=noodles, categories=categories, spiciness_values=spiciness_values, SPICINESS_EMOJI_MAP=SPICINESS_EMOJI_MAP, RATING_EMOJI_MAP=RATING_EMOJI_MAP)

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

SPICINESS_EMOJI_MAP = {
    1: "🌶️",
    2: "🌶️🌶️",
    3: "🌶️🌶️🌶️",
    4: "🌶️🌶️🌶️🌶️",
    5: "🌶️🌶️🌶️🌶️🌶️"
}

RATING_EMOJI_MAP = {
    1: "⭐",
    2: "⭐⭐",
    3: "⭐⭐⭐",
    4: "⭐⭐⭐⭐",
    5: "⭐⭐⭐⭐⭐"
}
