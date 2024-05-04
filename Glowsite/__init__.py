from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "User.db"

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
    app.config['MYSQL_DATABASE_PORT'] = 3307
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'User'
    app.config['SECRET_KEY'] = 'dkjfnhe'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.signup'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(str(user_id))

    return app

def create_database(app):
    if not path.exists('Glowsite/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')