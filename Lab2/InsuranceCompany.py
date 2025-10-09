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


class LifeInsurancePolicy(InsurancePolicy):
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float):
        super().__init__(policy_id, customer, start_date, end_date, coverage_amount, premium)

    def calc_premium(self) -> float:
        base = super().calc_premium()
        age_factor = 1 + max(0, (self.customer.age - 33) / 49)
        return round(base * age_factor, 2)

    def get_summary(self) -> str:
        return f"Life {super().get_summary()} age={self.customer.age}"


class RepairService:
    def __init__(self, garage_name):
        self.garage_name = garage_name

    def schedule_repair(self, num: str, when: date) -> str:
        return f"Авто {num} записано в {self.garage_name} на {when.isoformat()}"

    def repair_status(self, num: str) -> str:
        return f"Status for {num}: IN_PROGRESS"


class AutoRepairPolicy(AutoInsurancePolicy, RepairService):             #множинне наслідування
    def __init__(self, policy_id: int, customer: Customer, start_date: date, end_date: date, coverage_amount: float, premium: float, vehicle_number: str, garage_name: str):
        AutoInsurancePolicy.__init__(self, policy_id, customer, start_date, end_date, coverage_amount, premium, vehicle_number)
        RepairService.__init__(self, garage_name)

    def get_summary(self) -> str:
        return f"AutoRepair {super().get_summary()} garage:{self.garage_name}"

    def schedule_repair_for_policy(self, when: date) -> str:
        return self.schedule_repair(self.vehicle_number, when)


def demo():
    buba = Customer("Boba Buba", "12345678", date(1979, 5, 10), "buba@gmail.com", "380111111")
    petya = Customer("Petya", "87654321", date(2002, 8, 15), "petrik@gmail.com", "380222222")

    today = date.today()
    one_year = today + timedelta(days=365)

    base_policy = InsurancePolicy(100, buba, today, one_year, coverage_amount=10000.0, premium=100.0)
    print(base_policy.get_summary())
    print(f"Premium standart: {base_policy.calc_premium():.2f}")
    auto_pol = AutoInsurancePolicy(101, petya, today, one_year, coverage_amount=20000.0, premium=200.0, vehicle_number="1HGCM82633A004352")
    print(auto_pol.get_summary())
    print(f"Premium auto: {auto_pol.calc_premium():.2f}")

    life_pol = LifeInsurancePolicy(102, buba, today, one_year, coverage_amount=50000.0, premium=500.0)
    print(life_pol.get_summary())
    print(f"Premium life: {life_pol.calc_premium():.2f}")
    auto_repair_pol = AutoRepairPolicy(103, petya, today, one_year, coverage_amount=15000.0, premium=150.0, vehicle_number="WP0ZZZ99ZTS392124", garage_name="Giga garage")
    print(auto_repair_pol.get_summary())
    print(f"Premium auto repair: {auto_repair_pol.calc_premium():.2f}")

    when = today + timedelta(days=7)
    scheduled = auto_repair_pol.schedule_repair_for_policy(when)
    print(scheduled)
    print(auto_repair_pol.repair_status(auto_repair_pol.vehicle_number))

    policies = [base_policy, auto_pol, life_pol, auto_repair_pol]
    print("\nPolymorphism")
    for p in policies:
        print(f"{p.policy_number}: type={p.__class__.__name__}, premium_calc={p.calc_premium():.2f}")
    life_pol.cancel()
    print(life_pol.get_summary())

demo()
