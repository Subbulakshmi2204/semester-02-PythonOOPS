import re
class Member:
    def __init__(self,name,email):
        self.member_id=self.generate_member_id()
        self.name=name
        self.email=email
    def generate_member_id(self):
        from random import randint
        return f"LIB{randint(1000,9999)}"
    def validate_email(self):
        email_pat=r"^[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]$"
        if re.match(email_pat,self.email):
            print("Correct Email Id...")
        else:
            print("Invalid Email Id!!!")
    def verify_member_id(member_id):
        pat=r"^LIB\d{4}$"
        if re.match(pat,member_id):
            print("Correct Member Id...")
        else:
            print("Incorrect Member Id!!!")
class Library(Member):
    def __init__(self,name,email):
        super().__init__(name,email)
        self.books=[]
        self.members=[]
        self.borrowed_books={}
    def add_book(self,book_id,title,author):
        self.books.append({"book_id":book_id,"title":title,"Author":author})
        print(f"Book {title}  by {author} added successfully.")
    def register_member(self,name,email):
        try:
            new_member = Member(name, email)
            self.members.append(new_member)
            print(f"Member '{name}' registered successfully with ID: {new_member.member_id}")
        except ValueError as e:
            print(e)
    def borrow_book(self, book_id, member_id):
        for book in self.books:
            if book["book_id"]==book_id:
                if book_id not in self.borrowed_books:
                    self.borrowed_books[book_id]=member_id
                    print(f"Book '{book['title']}' borrowed by member ID {member_id}.")
                    return
                else:
                    print(f"Book '{book['title']}' is already borrowed.")
                    return
        print(f"Book ID {book_id} not found.")
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            del self.borrowed_books[book_id]
            print(f"Book ID {book_id} returned successfully.")
        else:
            print(f"Book ID {book_id} was not borrowed.")
if __name__ == "__main__":
    library = Library(name="Admin", email="admin@library.com")
    library.add_book(book_id="B001", title="The Great Gatsby", author="F. Scott Fitzgerald")
    library.add_book(book_id="B002", title="1984", author="George Orwell")
    library.register_member(name="Alice", email="alice@example.com")
    library.register_member(name="Bob", email="bob@example.com")
    library.borrow_book(book_id="B001", member_id="LIB1234")
    library.return_book(book_id="B001")

        
