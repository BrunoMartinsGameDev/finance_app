from dataclasses import dataclass

@dataclass
class Transaction:
    id: int
    type: str # 'income' or 'expense'
    description: str
    category: str
    amount: float
    date: str # ISO format date string (YYYY-MM-DD)