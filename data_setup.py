#This file just creates the database with data, and used for testing purposes
from app import app, db, Category, Noodle

# Perform database actions within the application context
with app.app_context():
    # Create the database tables
    db.create_all()

    # Define the data
    categories_data = [
        {'company': 'Nongshim'},
        {'company': 'Maruchan'},
        {'company': 'Trident'},
        {'company': 'Maggi'},
        {'company': 'Mi Goreng'}
    ]
    
    noodles_data = [
        {'name': 'Shin Ramyun', 'review': 'This is the best ramen ever!', 'rating': 5, 'spiciness': 5, 'category': 'Nongshim'},
        {'name': 'Instant Lunch', 'review': 'Great for a quick meal!', 'rating': 4, 'spiciness': 2, 'category': 'Maruchan'},
        {'name': 'Yakisoba', 'review': 'Delicious and easy to make!', 'rating': 4, 'spiciness': 3, 'category': 'Maruchan'},
        {'name': 'Beef Noodles', 'review': 'Tastes pretty average', 'rating': 2, 'spiciness': 1, 'category': 'Trident'},
        {'name': 'Hot & Spicy', 'review': 'It tastes very good but its not actually that spicy', 'rating': 4, 'spiciness': 2, 'category': 'Mi Goreng'},
    ]
    
    # Insert categories
    for cat in categories_data:
        category = Category.query.filter_by(company=cat['company']).first()
        if category is None:
            new_category = Category(company=cat['company'])
            db.session.add(new_category)
    
    # Commit the categories
    db.session.commit()
    
    # Insert noodles
    for nood in noodles_data:
        noodle = Noodle.query.filter_by(name=nood['name']).first()
        if noodle is None:
            category = Category.query.filter_by(company=nood['category']).first()
            new_noodle = Noodle(name=nood['name'], review=nood['review'], rating=nood['rating'], spiciness=nood['spiciness'], category_id=category.id)
            db.session.add(new_noodle)
    
    # Commit the noodles
    db.session.commit()


