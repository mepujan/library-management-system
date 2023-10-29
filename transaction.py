import csv
from datetime import date, timedelta, datetime
from utility import get_id, write_csv, delete_csv_data
from books import Book
from borrowers import Person


class Transaction:
    def __init__(self, book, user, returned_date=None) -> None:
        self.transaction_id = get_id()
        self.book = book
        self.user = user
        self.borrow_date = date.today()
        self.expected_return_date = date.today() + timedelta(days=10)
        self.returned_date = returned_date
        self.penalty = 0

    @staticmethod
    def calculate_penalty(expected_date, returned_date):
        penalty_per_day = 15
        if expected_date < returned_date:
            days_exceeds = returned_date - expected_date
            penalty_amount = days_exceeds.days * penalty_per_day
            return penalty_amount
        return 0

    @staticmethod
    def get_transaction_by_Id(transaction_id):
        with open("transaction.csv", "r") as transaction:
            transaction_data = csv.reader(transaction)
            for row in transaction_data:
                if row[0] == transaction_id:
                    return row

    @staticmethod
    def update_transaction_data(file_name, id, data):
        with open(file_name, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                row_values = row.values()
                if id in row_values:
                    row['ReturnDate'] = data[0]
                    row['Penalty'] = data[1]
                    rows.append(row)
                else:
                    rows.append(row)
        headers = ["TransactionId", "Book", "User", "BorrowDate",
                   "ExpectedReturnDate", "ReturnDate", "Penalty"]
        with open(file_name, 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

    @staticmethod
    def display(transaction):

        print(transaction[1], "\t\t", transaction[2], '\t\t', transaction[3],
              '\t\t', transaction[4], '\t\t\t', transaction[5], '\t\t', transaction[6])
        print("---------------------------------------------------------------------------------------")

    @staticmethod
    def extend_return_date(id, new_date):
        with open('transaction.csv', "r", newline="") as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                row_values = row.values()
                if id in row_values:
                    row['ExpectedReturnDate'] = new_date
                    rows.append(row)
                else:
                    rows.append(row)
        headers = ["TransactionId", "Book", "User", "BorrowDate",
                   "ExpectedReturnDate", "ReturnDate", "Penalty"]
        with open('transaction.csv', 'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)


def menu():
    print("1. Borrow Book")
    print("2. View Transaction By Id")
    print("3. Update Transaction")
    print("4. Remove Transaction")
    print("5. Extend Return Date")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            file_name = "transaction.csv"
            headers = ["TransactionId", "Book", "User", "BorrowDate",
                       "ExpectedReturnDate", "ReturnDate", "Penalty"]
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

            book = Book(book_info[1], book_info[2], book_info[3],
                        book_info[4], book_info[5], book_info[6], book_info[7])
            user = Person(user_info[1], user_info[2],
                          user_info[3], user_info[4])
            if book.does_book_exist():
                transaction = Transaction(book, user)
                data = [transaction.transaction_id, book, user, transaction.borrow_date,
                        transaction.expected_return_date, transaction.returned_date, transaction.penalty]
                write_csv(file_name, data, headers)
            print("No Book Available At The Moment. Please Come back later.")

        case 2:
            transaction_id = input("Enter Transaction Id: ")
            transaction = Transaction.get_transaction_by_Id(transaction_id)
            if transaction:
                print(
                    "---------------------------------------------------------------------------------------")
                print(
                    "Book \t\t User \t\t\t Borrow Date \t\t Expected Return Date \t Return Date \t\t Penalty")
                print(
                    "---------------------------------------------------------------------------------------")
                Transaction.display(transaction)
            else:
                print(
                    "---------------------------------------------------------------------------------------")
                print("No Transaction Found. Try Again...")

        case 3:
            transaction_id = input("Enter transaction Id: ")
            transaction = Transaction.get_transaction_by_Id(transaction_id)
            if transaction:
                print("Enter Book Returned date")
                year = int(input("Enter Year: "))
                while year < 2023:
                    print("Invalid Year. Try Again.")
                    year = int(input("Enter Year: "))
                month = int(input("Enter Month: "))
                while month not in range(1, 13):
                    print("Month should be in range 1 to 12 inclusive. Try Again...")
                    month = int(input("Enter Month: "))
                day = int(input("Enter Day: "))
                while day not in range(1, 31):
                    print("Month consist of 30 days. Try Again...")
                    day = int(input("Enter Day: "))
                returned_date = date(year, month, day)
                expected_date = datetime.strptime(
                    transaction[4], "%Y-%m-%d").date()
                penalty = Transaction.calculate_penalty(
                    expected_date, returned_date)
                data = [returned_date, penalty]
                Transaction.update_transaction_data(
                    'transaction.csv', transaction[0], data)
            else:
                print("No Transaction Found. Try Again...")

        case 4:
            transaction_id = input("Enter Transaction Id: ")
            while transaction_id is None or transaction_id == "":
                print("Invalid Input. Try Again...")
                transaction_id = input("Enter Transaction Id: ")

            transaction_details = Transaction.get_transaction_by_Id(
                transaction_id)
            if transaction_details:
                file_name = "transaction.csv"
                delete_csv_data(file_name, transaction_details[0])
                print("Data Deleted Successfully")
            else:
                print("Cannot Delete Data. Try again...")

        case 5:
            transaction_id = input("Enter transaction id: ")
            transaction = Transaction.get_transaction_by_Id(transaction_id)
            if transaction:
                print("Enter new expected return date: ")
                year = int(input("Year: "))
                while year < 2023:
                    print("Invalid Year. Currently its 2023. Try again...")
                    year = int(input("Year: "))
                month = int(input("month: "))
                while month not in range(1, 12):
                    print("Month should be in range 1 to 12")
                    month = int(input("month: "))
                day = int(input("Day: "))
                while day not in range(1, 31):
                    print("Days should be in between 1 to 30. Try Again...")
                    day = int(input("Day: "))

                new_expected_date = date(year, month, day)
                Transaction.extend_return_date(
                    transaction[0], new_expected_date)
            else:
                print("No Transaction Found. Try Again...")
