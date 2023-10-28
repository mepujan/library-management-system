from books import book_menu
from borrowers import menu as borrowers_menu
from transaction import menu as transaction_menu

def menu():
    print("----------------------------------------------------------------")
    print("Welcome to Pujan's Library")
    print("----------------------------------------------------------------")
    print("1. Books")
    print("2. Borrowers")
    print("3. Transactions")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    while choice not in range(1,5):
        print("Invalid Choice. Try Again.")
        choice = int(input("Enter Choice: "))
    match choice:
        case 1:
            book_menu()
        case 2:
            borrowers_menu()
        case 3:
            transaction_menu()
        case _:
            exit(0)

while True:
    menu()