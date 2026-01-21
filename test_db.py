from database.db import Database
from models.transaction import Transaction

db = Database()

t = Transaction(
    id = None,
    type="expense",
    description="Grocery shopping",
    category="Food",
    amount=150.75,
    date="2024-06-15"
)

db.add_transaction(t)

for transaction in db.get_all_transactions():
    print(transaction)