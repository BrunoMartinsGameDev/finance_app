import sqlite3
from pathlib import Path
from models.transaction import Transaction


class Database:
    def __init__(self):
        base_dir = Path(__file__).resolve().parent.parent
        self.db_path = base_dir / 'finance_app.db'

        self._create_tables()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def add_transaction(self, transaction: Transaction):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions (type, description, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
        """, (transaction.type, transaction.description, transaction.category, transaction.amount, transaction.date))

        conn.commit()
        conn.close()

    def get_all_transactions(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        rows = cursor.fetchall()

        transactions = []
        for row in rows:
            transaction = Transaction(
                type=row[1],
                description=row[2],
                category=row[3],
                amount=row[4],
                date=row[5]
            )
            transactions.append(transaction)

        conn.close()
        return transactions