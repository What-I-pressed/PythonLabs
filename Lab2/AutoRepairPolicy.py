from datetime import date
from Customer import Customer
from AutoInsurancePolicy import AutoInsurancePolicy
from RepairService import RepairService

class AutoRepairPolicy(AutoInsurancePolicy, RepairService):             #множинне наслідування
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float, vehicle_number: str, garage_name: str):
        AutoInsurancePolicy.__init__(self, policy_id, customer, start_date, end_date, coverage_amount, premium, vehicle_number)
        RepairService.__init__(self, garage_name)

    def get_summary(self) -> str:
        return f"AutoRepair {super().get_summary()} garage:{self.garage_name}"

    def schedule_repair_for_policy(self, when: date) -> str:
        return self.schedule_repair(self.vehicle_number, when)