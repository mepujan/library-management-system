import csv
import os
# from main_menu import menu

class Book:
    def __init__(self, title, author, publication_year, ISBN_number,price,quantity, shelf_number):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN_number = ISBN_number
        self.price = price
        self.quantity = quantity
        self.shelf_number = shelf_number

    #getter methods

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
    

    # setter methods

    def set_title(self, title):
        self.title = title

    def set_author(self,author):
        self.author = author

    def set_publication_year(self,year):
        self.publication_year = year

    def set_price(self,price):
        self.price = price
    
    def set_quantity(self,quantity):
        self.quantity = quantity


    def does_book_exist(self):
        if self.quantity > 0 :
            return True
        return False
    

    def save_book_csv(self,data):
        headers = ["Title",'Author','Publication',"ISBN","Price","Quantity","Shelf"]
        csv_file = "books.csv"
        with open(csv_file, "a", newline="") as book:
            writer = csv.writer(book)
            if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
                writer.writerow(headers)
            writer.writerow(data)
        print("Book informations saved to books.csv file.")


def get_book_info_by_title_or_ISBN(book_info):
    with open("books.csv","r") as book:
        book_data = csv.reader(book)
        for data in book_data:
            if data[0] == book_info:
                return data
                print(data)
                # return data
            elif data[3]== book_info:
                return data

    book.close()

# adding book to the system

def add_book():
    title = input("Enter Title: ")

    while title is None or title == "":
        print("Invalid Title. Try Again....")
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
        isbn_number= input("Enter ISBN Number: ")

    price = float(input("Enter Price: "))
    while price <=0 or price is None:
        print("Invalid Price. Try Again...")
        price = float(input("Enter Price: "))

    quantity = int(input("Enter how many books: "))
    while quantity <=0 or quantity is None:
        print("Invalid Input. Try again...")
        quantity = int(input("Enter how many books: "))

    shelf_num = int(input("Enter shelf number: "))
    while shelf_num <=0 or shelf_num is None:
        print("Invalid Input. Try again...")
        shelf_num =int(input("Enter shelf number: ")) 

    return title, author, publication_year, isbn_number, price, quantity, shelf_num





def book_menu():
    print("----------------------------------------------------------------")
    print("Add New Book")
    print("----------------------------------------------------------------")
    print()
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book Informations")
    print("4. Return to main menu")
    print("5. Search Book (ISBN Number or Title)")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    while choice not in range(1,6):
        print("Invalid Input. Try Again...")
        choice = int(input("Enter Choice: "))

    match choice:
        case 1:
            title, author, publication_year, isbn_number, price, quantity, shelf_num = add_book()
            book = Book(title, author,publication_year,isbn_number,price,quantity,shelf_num)
            book.save_book_csv([title, author, publication_year, isbn_number, price, quantity, shelf_num])
        case 2:
            # remove book
            pass
        case 3: 
            # update book
            pass
        case 4: 
            # return to main menu
            # menu()
            pass
        case 5:
            title_or_isbn = input("Enter book title or isbn number: ")
            book = get_book_info_by_title_or_ISBN(title_or_isbn)
            if book:
                print("---------------------------------------------------------------------------------------")
                print("Title \t\t Author \t\t ISBN \t\t Quantity \t\t Shelf")
                print("---------------------------------------------------------------------------------------")
                print(book[0],"\t\t",book[1],"\t\t", book[3], '\t\t', book[5],'\t\t',book[6])
                print("---------------------------------------------------------------------------------------")
            else:
                print("---------------------------------------------------------------------------------------")
                print("No Book Found. Try Again...")
        case _:
            exit(0)

    