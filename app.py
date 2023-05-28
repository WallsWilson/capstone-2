from flask import Flask, redirect, render_template, flash, abort, url_for
from models import db, connect_db, CustomerReview
from form import ReviewForm;



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jordanwalls-wilson:Snowblind98@localhost:5432/body_shop_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret_key'
app.config['WTF_CSRF_ENABLED'] = True

connect_db(app)

"""Home pages"""

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/claims-process', methods=['GET'])
def claim():
    return render_template('claims-process.html')

@app.route('/warranty', methods=['GET'])
def warranty():
    return render_template('warranty.html')

@app.route('/booking', methods=['GET'])
def booking():
    return render_template('booking.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html') 

@app.route('/customerReviews', methods=['GET', 'POST'])
def customerReviews():
    #create an instance of the ReviewForm
    form = ReviewForm()

    if form.validate_on_submit():
        customerReview = CustomerReview(
            #retrieve the data to fill out the form
            name = form.name.data,
            rating = form.rating.data,
            review_text = form.review_text.data
        )
        #add the customerReview to the database
        db.session.add(customerReview)
        db.session.commit()
        #redirct back to the cusotmer review page with the new review they just subbimtted uploaded. 
        return redirect(url_for('customerReviews'))
    
    #retrieve all the customerreviews from the DB
    reviews = CustomerReview.query.all()
    #render the customer review page with the fomr and all the reviews.
    return render_template('customerReviews.html', form=form, reviews=reviews)
