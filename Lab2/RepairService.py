from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Customer import Customer
from InsurancePolicy import InsurancePolicy

class RepairService:
    def __init__(self, garage_name):
        self.garage_name = garage_name

    def schedule_repair(self, num: str, when: date) -> str:
        return f"Авто {num} записано в {self.garage_name} на {when.isoformat()}"

    def repair_status(self, num: str) -> str:
        return f"Status for {num}: IN_PROGRESS"