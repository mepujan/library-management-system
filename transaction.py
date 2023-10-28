from datetime import date , timedelta
from utility import get_id,write_csv
from books import Book
from borrowers import Person

class Transaction:
    def __init__(self, book, user, returned_date = None) -> None:
        self.transaction_id = get_id()
        self.book = book
        self.user = user
        self.borrow_date = date.today()
        self.expected_return_date = date.today()+ timedelta(days= 10)
        self.returned_date = returned_date
        self.penalty = 0
        

    # getter
    def get_borrow_date(self):
        return self.borrow_date
    
    def get_expected_return_date(self):
        return self.expected_return_date
    
    def get_return_date(self):
        return self.returned_date
    
    # setter
    def set_borrow_date(self, date):
        self.borrow_date = date
    
    def set_expected_return_date(self,date):
        self.expected_return_date = date
    
    def set_returned_date(self,date):
        self.returned_date = date

    def calculate_fine(self):
        penalty_per_day = 15
        if date.today() > self.borrow_date():
            days_exceeds = date.today() - self.borrow_date()
            penalty_amount = days_exceeds.days * penalty_per_day
            return penalty_amount
        return 0


def menu():
    print("1. Borrow Book")
    print("2. View All Transactions.")
    print("3. View Transaction By Id")
    print("4. Update Transaction")
    print("5. Remove Transaction")
    

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            file_name = "transaction.csv"
            headers = ["TransactionId", "Book", "User","BorrowDate", "ExpectedReturnDate","ReturnDate","Penalty"]
            title_or_isbn = input("Enter book title or ISBN number: ")
           
            book_info = Book.get_book_info_by_title_or_ISBN(title_or_isbn)
            while not book_info:
                print("Book Doesnot Exist. Try Again")
                title_or_isbn = input("Enter book title or ISBN number: ")
                book_info = Book.get_book_info_by_title_or_ISBN(title_or_isbn)
            email = input("Enter user email: ")
            user_info = Person.search_user(email)
            while not user_info:
                print("User Doesnot exist. Try Again")
                email = input("Enter user email: ")
                user_info = Person.search_user(email)

            book = Book(book_info[1],book_info[2],book_info[3],book_info[4],book_info[5],book_info[6],book_info[7])
            user = Person(user_info[1],user_info[2],user_info[3],user_info[4])
            
            transaction = Transaction(book, user)
            data = [transaction.transaction_id,book,user,transaction.borrow_date,transaction.expected_return_date,transaction.returned_date,transaction.penalty]
            write_csv(file_name,data,headers)

        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass



    