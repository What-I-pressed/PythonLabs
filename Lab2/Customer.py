from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Customer:
    def __init__(self, fullname: str, tax_number: str, date_of_birth: date, email: str, phone: str, address: str = ""):
        self.fullname = fullname
        self.tax_number = tax_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        self.address = address

    @property
    def age(self) -> int:
        return relativedelta(date.today(), self.date_of_birth).years