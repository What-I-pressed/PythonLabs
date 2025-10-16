from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Customer import Customer
from InsurancePolicy import InsurancePolicy

class AutoInsurancePolicy(InsurancePolicy):             #еаслідування
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float, vehicle_number: str):
        super().__init__(policy_id, customer, start_date, end_date, coverage_amount, premium)
        self.vehicle_number = vehicle_number

    def calc_premium(self) -> float:
        age = int(self.vehicle_number[-1]) if self.vehicle_number[-1].isdigit() else 3
        base = super().calc_premium()
        multiplier = 1 + 0.10 * (age - 1)
        return round(base * multiplier, 2)

    def get_summary(self) -> str:
        return f"Auto {super().get_summary()} vehicle_number={self.vehicle_number}"