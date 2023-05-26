from flask import Flask, redirect, render_template, g, session, flash, request, abort


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret_key'
app.config['WTF_CSRF_ENABLED'] = True

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