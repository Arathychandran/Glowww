from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth' , __name__)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("Email entered:", email)
        print("Password entered:", password)

        user = User.query.filter_by(email=email).first()
        if user:
            print("User found in database:", user.email)
            print("Stored Password:", user.password)
            print("Entered Password:", password)
            if check_password_hash((generate_password_hash(password, method='pbkdf2:sha512')), password):
                print("Password matched")
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                print("Password did not match")
                flash('Incorrect password, try again.', category='error')
        else:
            print("User not found")
            flash('Email does not exist.', category='error')

    return render_template('recemain2.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' :
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4 :
            flash('Email must be greater than 3 characters',category='error')
        elif len(name) < 2 :
            flash('Name must be greater than 1 characters',category='error')
        elif len(password) < 7 :
            flash('Password must be atleast than 7 characters',category='error')
        else:
            new_user = User(email=email,name=name, password=generate_password_hash(password, method='pbkdf2:sha512'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created',category='success')
            return redirect(url_for('auth.signin'))
        
    return render_template('signin.html')

