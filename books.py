class Book:
    def __init__(self, title, author, publication_year, ISBN_number,price,quantity):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN_number = ISBN_number
        self.price = price
        self.quantity = quantity

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

