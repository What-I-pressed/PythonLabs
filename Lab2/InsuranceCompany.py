from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Customer import Customer
from InsurancePolicy import InsurancePolicy
from AutoInsurancePolicy import AutoInsurancePolicy
from LifeInsurancePolicy import LifeInsurancePolicy
from AutoRepairPolicy import AutoRepairPolicy

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
