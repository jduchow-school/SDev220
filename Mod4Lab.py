'''
Jackson Duchow
API Mod 4 Lab
Following the API tutorial, we create an API for books
'''

from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), unique=True, nullable=False)
    publisher = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.book_name} {self.author} {self.publisher}"

@app.route('/')
def index():
    return "Welcome to the Book API!"

@app.route('/books')
def get_books():
    
    return {"books": "books data"}

