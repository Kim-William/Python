# import sqlite3

# db=sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

all_books=[]

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

app.app_context().push()
db.create_all()


#CREATE RECORD
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()
def create(title, author, rating):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()
    
def read_all():
    all_books =db.session.query(Book).all()
    return all_books

def read_title(title):
    book = Book.query.filter_by(title = title).first()
    return book    

def read_author(author):
    books = Book.query.filter_by(author=author).all()
    return books

def update(book_updated):
    book_to_update = Book.query.get(book_updated.id)
    book_to_update.title = book_updated.title
    book_to_update.author = book_updated.author
    book_to_update.rating = book_updated.rating
    db.session.commit()

def delete(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()

create(title="Harry Potter", author="J. K. Rowling", rating=9.3)

create(title="Google", author="J. K. Rowling", rating=9.3)

all_books = read_all()
print(all_books)

read_book = read_title('Harry Potter')
print(read_book)

read_book.title = 'Harry Potter and the Goblet of Fire'
read_book.rating = 3.4
read_book.author = 'Rowling'
update(read_book)

all_books = read_all()
print(all_books)

if len(all_books)> 0:
    for book in all_books:
        delete(book.id)        


all_books = read_all()
print(all_books)
