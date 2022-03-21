from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60))
    