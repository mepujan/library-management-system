class Person:
    def __init__(self, name, address, email,mobile) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.mobile = mobile


    # getter functions
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def email(self):
        return self.email
    
    def mobile(self):
        return self.mobile
    
    # setter functions

    def set_name(self, name):
        self.name = name

    def set_address(self,address):
        self.address = address

    def set_email(self,email):
        self.email = email
    
    def set_mobile(self, mobile):
        self.mobile = mobile
    
    
def create_profile():
    name = input("Enter Your Name: ")
    while name is None or name == "":
        print("Invalid Name. Try Again...")
        name = input("Enter Your Name: ")
    address = input("Enter your address: ")
    while address is None or address == "":
        print("Invalid input. Try Again...")
        address = input("Enter your address: ")
    email = input("Enter your address: ")
    while email is None or email == "":
        print("Invalid Input. Try Again...")
        email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")
    while mobile is None or len(mobile) != 10:
        print("Invalid Mobile Number. Try Again...")
        print("Length of mobile number should be 10.")
        mobile = input("Enter your mobile number: ")
    
    return name, address, email, mobile
