# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, relationship
import datetime
from pydantic import BaseModel
from typing import List

# Database Setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Models


class User(Base):
    __tablename__ = "users"
    UserID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Email = Column(String, unique=True, index=True)
    MembershipDate = Column(Date)
    borrowed_books = relationship("BorrowedBooks", back_populates="user")



class Book(Base):
    __tablename__ = "books"
    BookID = Column(Integer, primary_key=True, index=True)
    Title = Column(String, index=True)
    ISBN = Column(String, unique=True, index=True)
    PublishedDate = Column(Date)
    Genre = Column(String)
    details = relationship("BookDetails", uselist=False, back_populates="book")


class BookDetails(Base):
    __tablename__ = "book_details"
    DetailsID = Column(Integer, primary_key=True, index=True)
    BookID = Column(Integer, ForeignKey("books.BookID"))
    NumberOfPages = Column(Integer)
    Publisher = Column(String)
    Language = Column(String)
    book = relationship("Book", back_populates="details")


class BorrowedBooks(Base):
    __tablename__ = "borrowed_books"
    UserID = Column(Integer, ForeignKey("users.UserID"), primary_key=True)
    BookID = Column(Integer, ForeignKey("books.BookID"), primary_key=True)
    BorrowDate = Column(Date)
    ReturnDate = Column(Date)
    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book", back_populates="borrowed_books")

# Pydantic model for request validation

class UserCreate(BaseModel):
    Name: str
    Email: str
    MembershipDate: datetime.date
    borrowed_books: List[BorrowedBooks]

# class UserCreate(BaseModel):
#     Name: str
#     Email: str
#     MembershipDate: Date


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints for User
@app.post("/users/create/")
def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    db.refresh(user)
    return db.user

# # API Endpoints for User


# @app.post("/users/create/", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(**user.dict())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


@app.get("/users/all/")
def list_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.get("/users/{user_id}/")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.UserID == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# API Endpoints for Book


@app.post("/books/create/")
def create_book(book: Book, db: Session = Depends(get_db)):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@app.get("/books/all/")
def list_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@app.get("/books/{book_id}/")
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.BookID == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}/details/")
def assign_update_book_details(book_id: int, details: BookDetails, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.BookID == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    existing_details = db.query(BookDetails).filter(
        BookDetails.BookID == book_id).first()
    if existing_details:
        existing_details.NumberOfPages = details.NumberOfPages
        existing_details.Publisher = details.Publisher
        existing_details.Language = details.Language
    else:
        details.BookID = book_id
        db.add(details)

    db.commit()
    db.refresh(details)
    return details

# API Endpoints for BorrowedBooks


@app.post("/borrowed-books/borrow/")
def borrow_book(user_id: int, book_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.UserID == user_id).first()
    book = db.query(Book).filter(Book.BookID == book_id).first()

    if user is None or book is None:
        raise HTTPException(status_code=404, detail="User or Book not found")

    borrowed_book = BorrowedBooks(UserID=user_id, BookID=book_id)
    db.add(borrowed_book)
    db.commit()
    db.refresh(borrowed_book)
    return borrowed_book


@app.put("/borrowed-books/return/")
def return_book(user_id: int, book_id: int, db: Session = Depends(get_db)):
    borrowed_book = db.query(BorrowedBooks).filter(
        BorrowedBooks.UserID == user_id, BorrowedBooks.BookID == book_id
    ).first()

    if borrowed_book is None:
        raise HTTPException(status_code=404, detail="Borrowed book not found")

    borrowed_book.ReturnDate = datetime.now().date()
    db.commit()
    db.refresh(borrowed_book)
    return borrowed_book


@app.get("/borrowed-books/all/")
def list_all_borrowed_books(db: Session = Depends(get_db)):
    borrowed_books = db.query(BorrowedBooks).all()
    return borrowed_books
