from services.finance_service import FinanceService

service = FinanceService()

service.add_income("Salário", "Trabalho", 5000.00)
service.add_expense("Aluguel", "Moradia", 1200.00)
service.add_expense("Jantar fora", "Lazer", 85.50)
print("Saldo atual:", service.get_balance())