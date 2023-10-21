class Transaction:
    def __init__(self, ISBN_number, email, borrow_date, expected_return_date, returned_date = None) -> None:
        self.ISBN_number = ISBN_number
        self.email = email
        self.borrow_date = borrow_date
        self.expected_return_date = expected_return_date
        self.returned_date = returned_date
        

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