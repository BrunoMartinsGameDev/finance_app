from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QDateEdit
)
from PySide6.QtCore import QDate

class TransactionDialog(QDialog):
    def __init__(self, transaction_type:str):
        super().__init__()
        self.transaction_type = transaction_type
        self.setWindowTitle("Adicionar Receita" if transaction_type == "income" else "Adicionar Despesa")
        
        self._create_ui()

    def _create_ui(self):
        layout = QVBoxLayout()

        # Descricao
        layout.addWidget(QLabel("Descrição:"))
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)

        # Categoria
        layout.addWidget(QLabel("Categoria:"))
        self.category_input = QLineEdit()
        layout.addWidget(self.category_input)

        # Valor
        layout.addWidget(QLabel("Valor:"))
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("EX: 150.50")
        layout.addWidget(self.amount_input)

        # Data
        layout.addWidget(QLabel("Data:"))
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        layout.addWidget(self.date_input)

        # Botões
        button_layout = QHBoxLayout()

        btn_cancel = QPushButton("Cancelar")
        btn_save = QPushButton("Salvar")

        btn_cancel.clicked.connect(self.reject)
        btn_save.clicked.connect(self.accept)

        button_layout.addWidget(btn_cancel)
        button_layout.addWidget(btn_save)

        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def get_data(self):
        return {
            "description": self.description_input.text(),
            "category": self.category_input.text(),
            "amount": float(self.amount_input.text()),
            "date": self.date_input.date().toString("yyyy-MM-dd"),
        }