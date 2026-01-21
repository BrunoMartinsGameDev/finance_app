from dataclasses import astuple
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QTableWidgetItem
)
from PySide6.QtCore import Qt
from services.finance_service import FinanceService
from ui.dialogs.transaction_dialog import TransactionDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FInance App")
        self.resize(900, 600)

        self.service = FinanceService()

        self._create_ui()
        self._create_status_bar()
        self._load_data()

    def _create_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        # Saldo
        self.balance_label = QLabel("Saldo: R$ 0,00")
        self.balance_label.setAlignment(Qt.AlignCenter)
        self.balance_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Tabela de transações
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            ["Tipo", "Descrição", "Categoria", "Valor","Data"])
        self.table.horizontalHeader().setStretchLastSection(True)

        # Botões
        button_layout = QHBoxLayout()
        self.btn_add_income = QPushButton("Adicionar Receita")
        self.btn_add_expense = QPushButton("Adicionar Despesa")

        self.btn_add_income.clicked.connect(self.open_income_dialog)
        self.btn_add_expense.clicked.connect(self.open_expense_dialog)

        button_layout.addWidget(self.btn_add_income)
        button_layout.addWidget(self.btn_add_expense)

        # Montagem do layout principal
        main_layout.addWidget(self.balance_label)
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def _create_status_bar(self):
        self.statusBar().showMessage("Pronto")

    def open_income_dialog(self):
        self._open_transaction_dialog("income")

    def open_expense_dialog(self):
        self._open_transaction_dialog("expense")

    def _open_transaction_dialog(self, transaction_type: str):
        dialog = TransactionDialog(transaction_type)

        if dialog.exec():
            try:
                data = dialog.get_data()

                if transaction_type == "income":
                    self.service.add_income(**data)
                else:
                    self.service.add_expense(**data)

                self._load_data()
                self.statusBar().showMessage("Transação adicionada com sucesso!", 5000)
            except Exception as e:
                QMessageBox.critical(self, "Erro", str(e))

    def _load_data(self):
        self.table.setRowCount(0)
        transactions = self.service.get_all_transactions()
        for transaction in transactions:
            row_number = self.table.rowCount()
            self.table.insertRow(row_number)
            for column, value in enumerate(astuple(transaction)):
                if column == 0:
                    continue # Pula o ID
                print(value)
                self.table.setItem(row_number, column-1,
                                   QTableWidgetItem(str(value)))

        balance = self.service.get_balance()
        self.balance_label.setText(f"Saldo: R$ {balance:.2f}")
        if balance > 0 :
            color = "green"
        elif balance < 0:
            color = "red"
        else:
            color = "gray"
        self.balance_label.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {color};")
