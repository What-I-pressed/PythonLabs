from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Customer import Customer
from InsurancePolicy import InsurancePolicy

class LifeInsurancePolicy(InsurancePolicy):
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float):
        super().__init__(policy_id, customer, start_date, end_date, coverage_amount, premium)

    def calc_premium(self) -> float:
        base = super().calc_premium()
        age_factor = 1 + max(0, (self.customer.age - 33) / 49)
        return round(base * age_factor, 2)

    def get_summary(self) -> str:
        return f"Life {super().get_summary()} age={self.customer.age}"