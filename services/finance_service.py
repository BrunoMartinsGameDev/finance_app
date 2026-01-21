from datetime import date
from database.db import Database
from models.transaction import Transaction


class FinanceService:
    def __init__(self):
        self.db = Database()

    def add_income(self, description: str, category: str, amount: float, date=None):
        self._validate_amount(amount)
        transaction = Transaction(
            id=None,
            type='income',
            description=description,
            category=category,
            amount=amount,
            date=self._format_date(date)
        )
        self.db.add_transaction(transaction)

    def add_expense(self, description: str, category: str, amount: float, date=None):
        transaction = Transaction(
            id=None,
            type='expense',
            description=description,
            category=category,
            amount=amount,
            date=self._format_date(date)
        )
        self.db.add_transaction(transaction)

    def get_all_transactions(self):
        return self.db.get_all_transactions()

    def get_balance(self):
        transactions = self.get_all_transactions()
        balance = 0
        for t in transactions:
            if t.type == 'income':
                balance += t.amount
            elif t.type == 'expense':
                balance -= t.amount
        return balance
    
    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        
    def _format_date(self, trans_date):
        if trans_date is None:
            return date.today().isoformat()
        return trans_date