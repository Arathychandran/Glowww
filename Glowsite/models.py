from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __repr__(self):
        return f"<User {self.name}>"
    
    def get_id(self):
        return str(self.id)