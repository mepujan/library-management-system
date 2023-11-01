import csv
import os
from utility import write_csv, get_id, delete_csv_data


class Book:
    def __init__(self, title, author, publication_year, ISBN_number, price, quantity, shelf_number):
        self.book_id = get_id()
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN_number = ISBN_number
        self.price = price
        self.quantity = quantity
        self.shelf_number = shelf_number

    # getter methods

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def get_ISBN_number(self):
        return self.ISBN_number

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_shelf(self):
        return self.shelf_number

    # setter methods

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publication_year(self, year):
        self.publication_year = year

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def does_book_exist(self):
        if self.quantity > 0:
            return True
        return False

    def __str__(self):
        return self.title

    @staticmethod
    def get_book_info_by_title_or_ISBN(book_info):
        '''
            This function takes book_info as a parameter and
            returns the information related to book if it existed in csv file
            otherwise None is returned.
        '''
        try:
            with open("books.csv", "r") as book:
                book_data = csv.reader(book)
                for data in book_data:
                    if data[1] == book_info:
                        return data
                    elif data[4] == book_info:
                        return data

            book.close()
        except FileNotFoundError:
            print(
                "File Not Found. Either No Data has been created or Some internal error occurs")
        except:
            print("Some error occurs. Try Again...")

    @staticmethod
    def update_book_data(file_name, id, new_data):
        '''
            This function takes file_name, id and new_data as a parameter and
            update the existing data with the new data.
        '''
        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.DictReader(file)
                rows = []
                for row in reader:
                    row_values = row.values()
                    if id in row_values:
                        row['BookId'] = id
                        row['Title'] = new_data[0]
                        row['Author'] = new_data[1]
                        row['Publication'] = new_data[2]
                        row['ISBN'] = new_data[3]
                        row['Price'] = new_data[4]
                        row['Quantity'] = new_data[5]
                        row['Shelf'] = new_data[6]
                        rows.append(row)
                    else:
                        rows.append(row)
            headers = ["BookId", "Title", 'Author', 'Publication',
                       "ISBN", "Price", "Quantity", "Shelf"]
            with open(file_name, 'w', newline="") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)
        except FileNotFoundError:
            print(
                "File Not Found. Either No Data has been created or Some internal error occurs")
        except:
            print("Some error occurs. Try Again...")


# adding book to the system

    @staticmethod
    def add_book():
        '''
        This method will takes book different informations from the user and return those informations.
        '''

        try:
            title = input("Enter Title: ")

            while title is None or title == "":
                print("Invalid Title. Try Again....")
                title = input("Enter Title: ")
                print(os.path.exists("books.csv"))
            if os.path.exists("books.csv"):
                book = Book.get_book_info_by_title_or_ISBN(title)
                if book:
                    while book[1] == title:
                        print("Book Already Exist. Try Again...")
                        title = input("Enter Title: ")
            author = input('Enter Author: ')

            while author is None or author == "":
                print("Invalid Title. Try Again....")
                author = input("Enter Author: ")

            publication_year = input("Enter Publication Year: ")
            while publication_year is None or publication_year == "":
                print("Invalid publication year. Try Again...")
                publication_year = input("Enter Publication Year: ")

            isbn_number = input("Enter ISBN Number: ")
            while isbn_number is None or isbn_number == "":
                print("Invalid ISBN Number. Try Again...")
                isbn_number = input("Enter ISBN Number: ")
            if os.path.exists("books.csv"):
                if book:
                    while book[4] == isbn_number:
                        print("Book Already Exist. Try Again...")
                        isbn_number = input("Enter ISBN Number: ")

            price = float(input("Enter Price: "))
            while price <= 0 or price is None:
                print("Invalid Price. Try Again...")
                price = float(input("Enter Price: "))

            quantity = int(input("Enter how many books: "))
            while quantity <= 0 or quantity is None:
                print("Invalid Input. Try again...")
                quantity = int(input("Enter how many books: "))

            shelf_num = int(input("Enter shelf number: "))
            while shelf_num <= 0 or shelf_num is None:
                print("Invalid Input. Try again...")
                shelf_num = int(input("Enter shelf number: "))

            return title, author, publication_year, isbn_number, price, quantity, shelf_num

        except ValueError as e:
            print(e)
        except:
            print("Invalid Input. Try Again...")

# this function will print the menu item related to book


def book_menu():
    print("----------------------------------------------------------------")
    print("Welcome to Book Menu")
    print("----------------------------------------------------------------")
    print()
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book Informations")
    print("4. Search Book (ISBN Number or Title)")
    print("5. Exit")
    try:
        choice = int(input("Enter Choice: "))

        while choice not in range(1, 6):
            print("Invalid Input. Try Again...")
            choice = int(input("Enter Choice: "))

        match choice:
            case 1:
                title, author, publication_year, isbn_number, price, quantity, shelf_num = Book.add_book()
                book = Book(title, author, publication_year,
                            isbn_number, price, quantity, shelf_num)
                data = [book.book_id, title, author, publication_year,
                        isbn_number, price, quantity, shelf_num]
                file_name = "books.csv"
                headers = ["BookId", "Title", 'Author', 'Publication',
                           "ISBN", "Price", "Quantity", "Shelf"]
                write_csv(file_name, data, headers)
            case 2:
                file_name = "books.csv"
                title_or_isbn = input("Enter title or isbn number of book: ")
                while title_or_isbn is None or title_or_isbn == "":
                    print("Invalid Input. Try Again...")
                    title_or_isbn = input(
                        "Enter title or isbn number of book: ")

                data = Book.get_book_info_by_title_or_ISBN(title_or_isbn)
                if data:
                    delete_csv_data(file_name, data[0])
                else:
                    print("Book Doesnot Exist in Database to Delete. Try Again...")
            case 3:
                book_isbn = input(
                    "Enter Book ISBN Number to update book informations: ")
                book = Book.get_book_info_by_title_or_ISBN(book_isbn)
                if book:
                    print("Provide New Informations")
                    title, author, publication_year, isbn_number, price, quantity, shelf_num = Book.add_book()
                    new_data = [title, author, publication_year,
                                isbn_number, price, quantity, shelf_num]
                    Book.update_book_data("books.csv", book[0], new_data)
                else:
                    print("No Book Exist with that ISBN Number. Try Again...")

            case 4:
                title_or_isbn = input("Enter book title or isbn number: ")
                book = Book.get_book_info_by_title_or_ISBN(title_or_isbn)
                if book:
                    print(
                        "---------------------------------------------------------------------------------------")
                    print("Title \t\t Author \t\t ISBN \t\t Quantity \t\t Shelf")
                    print(
                        "---------------------------------------------------------------------------------------")
                    print(book[1], "\t\t", book[2], "\t\t",
                          book[4], '\t\t', book[6], '\t\t', book[7])
                    print(
                        "---------------------------------------------------------------------------------------")
                else:
                    print(
                        "---------------------------------------------------------------------------------------")
                    print("No Book Found. Try Again...")
            case _:
                os._exit(0)

    except ValueError as e:
        print(e)
    except:
        print("Invalid Input. Try Again...")
