from flask import Blueprint,render_template,redirect,url_for,request,flash,session
from flask_login import login_required, current_user
from . import db
from Glowsite.models import User

views = Blueprint('views' , __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    else:
        return render_template("index.html")

@views.route('/new_page', methods=['POST'])
def new_page():
    # Handle form submission and redirect to new page
    return render_template("signin.html")
# def getstarted():
#     if request .method== 'POST':
#        return redirect(url_for('/signin'))

@views.route('/process_signup', methods=['POST'])
def process_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.add(new_user)
        db.session.commit()
        
        # cursor = db.get_db().cursor()
        # cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        # db.get_db().commit()
        # cursor.close()
        
        # Redirect to a success page along with the form data 
        return render_template('receptive.html', name=name, email=email)

@views.route('/signup_success')
def signup_success():
    name = request.args.get('name')
    email = request.args.get('email')
    password =request.args.get('password',None)
    
    
    return render_template('signup_success.html', name=name, email=email, password=password)