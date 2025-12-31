"""Assignment Title:

“Smart Library Management System (OOP in Python)”



Problem Statement

You are required to design a Smart Library Management System using Object-Oriented Programming in Python.

The system should allow managing books, members, and issuing/returning of books."""
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def __init__(self,member_id,name):
        self.__member_id=member_id
        self.name=name
    def display_member_name(self):
        return self.name
    def get_member_info(self):
        return self.__member_id
    def display_member_info(self):
        pass
class Book:
    def __init__(self,book_id,title,author,available=True):
        self.__book_id=book_id
        self.title=title
        self.author=author
        self.available=available
    def get_book_id(self):
        return self.__book_id
    def display_info(self):
        print(f"Book Title is :{self.title}, Book's author :{self.author}, Available{self.available}")
    def mark_issued(self):
        self.available=False
    def mark_returned(self):
        self.available=True
class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.issued_books=[]
    def issue_book(self,book):
        self.issued_books.append(book)
    def return_book(self,book):
        self.issued_books.remove(book)
    def display_member_info(self):
        print(f"Name {self.name}, Issued Books :{len(self.issued_books)}")
class StudentMember(Member):
    Borrow_Limit=3
    def display_member_name(self):
        print(f"[Student]Name :{self.name}, Issued books:{len(self.issued_books)}")
Student1=StudentMember(101,"Alisha")
Student2=StudentMember(103,"Areeba")
class TeacherMember(Member):
    Borrow_Limit=5
    def display_member_name(self):
        print(f"[Teacher]Name :{self.name}, Issued books:{len(self.issued_books)}")
Teacher1=TeacherMember(104,"Shehnaz Saeed")
Teacher2=TeacherMember(102,"Najmus Sehar")
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def add_book(self,book):
        self.books.append(book)
    def register_member(self,member):
        self.members.append(member)
    def issue_book(self,member_id,book_id):
        member = next((m for m in self.members if m.get_member_info()== member_id),None)
        book = next((b for b in self.books if b.get_book_id()==book_id),None)
        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if not book.available:
            print("Book already issued.")
            return
        limit = member.Borrow_Limit if hasattr(member,"Borrow_Limit") else 0
        if len(member.issued_books)>=limit:
            print("Borrow limit reached!")
            return
        book.mark_issued()
        member.issue_book(book)
        print(f"Book'{book.title}' issued to {member.name}")

    def new_method(self, book_id):
        book = next((b for b in self.books if b.book_info()== book_id),None)
        return book
    def return_book(self,member_id,book_id):
        member = next((m for m in self.members if m.display_member_info()== member_id),None)
        book = next((b for b in self.books if b.get_book_id()== book_id),None)
        if book in member.issued_books:
            book.mark_returned()
            member.return_book(book)
            print(f"Book'{book.title}' returned.")
    def display_all_books(self):
        for book in self.books:
            book.display_info()
    def display_all_members(self):
        for member in self.members:
            member.display_member_info()
lib=Library()
lib.add_book(Book(100001,"Python Essential 1","John Smith"))
lib.add_book(Book(100002,"Python Essential 2","John Smith"))
lib.add_book(Book(100003,"Python Essential 3","John Smith"))
lib.add_book(Book(100004,"Python Essential 4","John Smith"))
lib.add_book(Book(100005,"JavaScript Essential 1","Alexander Voral"))
lib.add_book(Book(100006,"JavaScript Essential 2","Alexander Voral"))
lib.add_book(Book(100007,"JavaScript Essential 3","Alexander Voral"))
lib.add_book(Book(100008,"JavaScript Essential 4","Alexander Voral"))
lib.add_book(Book(100009,"ML Algorithms","Sumaira Farhan"))
lib.add_book(Book(100010,"DL Algorithms","Sumaira Farhan"))
lib.add_book(Book(100011,"Front-end Web Development","Maheer Faizan"))
lib.add_book(Book(100012,"Back-end Web Development","Maheer Faizan"))
lib.add_book(Book(100013,"MERN Stack Development","Maheer Faizan"))
lib.add_book(Book(100014,"Full-Stack Web Development","Maheer Faizan"))
lib.add_book(Book(100015,"Python Basics","John Smith"))
lib.add_book(Book(100016,"Python Advance","John Smith"))
lib.add_book(Book(100017,"JavaScript Basics","Maheer Faizan"))
lib.add_book(Book(100018,"JavaScript Advance","Maheer Faizan"))
lib.add_book(Book(100019,"SQL Basics","Sumaira Farhan"))
lib.add_book(Book(100020,"Introduction to Data Science","Sumaira Farhan"))
lib.register_member(Student1)
lib.register_member(Student2)
lib.register_member(Teacher1)
lib.register_member(Teacher2)
lib.issue_book(104,100015)
lib.issue_book(104,100001)
lib.issue_book(104,100004)
lib.issue_book(104,100016)
lib.issue_book(104,100002)
lib.issue_book(101,100005)
lib.issue_book(101,100006)
lib.issue_book(101,100008)
lib.issue_book(103,100001)
lib.issue_book(103,100009)
lib.issue_book(102,100011)
lib.issue_book(102,100019)
lib.display_all_books()
lib.display_all_members()
