from Customer import Customer
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class InsurancePolicy:
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float, policy_number: str = ""):
        self.__status = "ACTIVE"            #приватна властивість
        self.policy_id = policy_id
        self.policy_number = policy_number or f"POL-{policy_id}"
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.coverage_amount = coverage_amount
        self.premium = premium

    @property
    def status(self):
        return self.__status

    def get_summary(self) -> str:
        return (f"Policy {self.policy_id}: customer={self.customer.fullname}, "
                f"coverage={self.coverage_amount:.2f}, premium={self.premium:.2f}, status={self.status}")

    def cancel(self):
        self.__status = "CANCELLED"
        print(f"[Policy] {self.policy_number} скасовано.")

    def calc_premium(self) -> float:
        days = (self.end_date - self.start_date).days
        years = max(1, int(days / 365.0))
        calculated = self.coverage_amount * 0.01 * years
        return round(calculated, 2)

    def __str__(self):
        return f"InsurancePolicy({self.policy_number}, status={self.status})"