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
    
    
        