import csv
import os
from utility import write_csv, get_id, delete_csv_data


class Person:
    def __init__(self, name, address, email, mobile) -> None:
        self.user_id = get_id()
        self.name = name
        self.address = address
        self.email = email
        self.mobile = mobile

    def __str__(self):
        return self.email

    @staticmethod
    def search_user(email):
        '''This method will filter out the borrowers informations using email provided by user
         and return that informations if user is present '''

        try:
            with open('person.csv', 'r') as persons:
                persons_data = csv.reader(persons)
                for data in persons_data:
                    if data[3] == email:
                        return data
            persons.close()
        except FileNotFoundError:
            print(
                "File Not Found. Either No Data has been created or Some internal error occurs")
        except:
            print("Some error occurs. Try Again...")

    @staticmethod
    def update_person_data(file_name, id, new_data):
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
                        row['UserId'] = id
                        row['Name'] = new_data[0]
                        row['Address'] = new_data[1]
                        row['Email'] = new_data[2]
                        row['Mobile'] = new_data[3]
                        rows.append(row)
                    else:
                        rows.append(row)
            headers = ["UserId", "Name", 'Address', 'Email',
                       "Mobile"]
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

    @staticmethod
    def get_user_transaction(email):
        '''
        This method takes email as an argument and returns all the user transaction as a list.
        '''
        try:
            with open('transaction.csv', 'r', newline="") as transaction:
                data = csv.reader(transaction)
                datas = []
                if data:
                    for row in data:
                        if email in row:
                            datas.append(row)
                return datas
        except FileNotFoundError:
            print(
                "File Not Found. Either No Data has been created or Some internal error occurs")
        except:
            print("Some error occurs. Try Again...")

    @staticmethod
    def create_profile():
        '''This functions ask different informations from the user and return that informations to the program'''

        try:
            name = input("Enter Your Name: ")
            while name is None or name == "":
                print("Invalid Name. Try Again...")
                name = input("Enter Your Name: ")
            address = input("Enter your address: ")
            while address is None or address == "":
                print("Invalid input. Try Again...")
                address = input("Enter your address: ")
            email = input("Enter your email address: ")
            while email is None or email == "":
                print("Invalid Input. Try Again...")
                email = input("Enter your email: ")
            mobile = input("Enter your mobile number: ")
            while mobile is None or len(mobile) != 10:
                print("Invalid Mobile Number. Try Again...")
                print("Length of mobile number should be 10.")
                mobile = input("Enter your mobile number: ")

            return name, address, email, mobile
        except ValueError as e:
            print(e)
        except:
            print("Invalid Input. Try Again...")


def menu():
    # menu of borrowers module
    print("Borrowers Menu")
    print("1. Add User")
    print("2. Update User Info")
    print("3. Remove User")
    print("4. Get User Transaction")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                name, address, email, mobile = Person.create_profile()
                person = Person(name, address, email, mobile)
                data = [person.user_id, name, address, email, mobile]
                file_name = "person.csv"
                headers = ["UserId", "Name", 'Address', 'Email', "Mobile"]
                write_csv(file_name, data, headers)
            case 2:
                user_email = input("Enter user email to update person data: ")
                person = Person.search_user(user_email)
                if person:
                    name, address, email, mobile = Person.create_profile()
                    data = [name, address, email, mobile]
                    Person.update_person_data('person.csv', person[0], data)
                else:
                    print("No user found.Try Again...")
            case 3:
                file_name = 'person.csv'
                email = input("Enter the email of user you want to delete: ")
                user = Person.search_user(email)
                if user:
                    delete_csv_data(file_name, user[0])
                    print("User Deleted Successfully")
                else:
                    print("Cannot Delete Data. Try Again...")
            case 4:
                email = input("Enter User Email to Extract all Transaction: ")
                history = Person.get_user_transaction(email)
                if history:
                    print(
                        "---------------------------------------------------------------------------------------")
                    print(
                        "Book \t\t User \t\t\t Borrow Date \t\t Expected Return Date \t Return Date \t\t Penalty")
                    print(
                        "---------------------------------------------------------------------------------------")
                    for transaction in history:
                        print(transaction[1], "\t\t", transaction[2], '\t\t', transaction[3],
                              '\t\t', transaction[4], '\t\t\t', transaction[5], '\t\t', transaction[6])

                        print(
                            "---------------------------------------------------------------------------------------")
                else:
                    print("No Transaction Found. Try Again...")
            case 5:
                os._exit(0)

            case _:
                print("Invalid Input. Try Again.")
    except ValueError as e:
        print(e)
    except:
        print("Invalid Input. Try Again...")
