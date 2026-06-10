from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QListWidget,
    QLabel,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt

from app.calculator import Calculator
from app.styles import DISPLAY_STYLE, get_button_style


class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.calculator = Calculator()

        self.setWindowTitle("Calculadora Científica")
        self.setFixedSize(500, 720)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet(DISPLAY_STYLE)

        self.history_label = QLabel("Histórico de cálculos")
        self.history_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
        """)

        self.history_list = QListWidget()
        self.history_list.setStyleSheet("""
            QListWidget {
                font-size: 14px;
                padding: 6px;
                border-radius: 8px;
                border: 1px solid #999;
                background-color: #ffffff;
            }
        """)

        self.clear_history_button = QPushButton("Limpar histórico")
        self.clear_history_button.setFixedHeight(40)
        self.clear_history_button.clicked.connect(self.clear_history)
        self.clear_history_button.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                background-color: #d9534f;
                color: white;
                border-radius: 8px;
                border: 1px solid #aaaaaa;
            }

            QPushButton:hover {
                background-color: #c9302c;
            }
        """)

        self.setup_layout()

    def setup_layout(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        button_layout = QGridLayout()

        buttons = [
            ("C", 0, 0), ("⌫", 0, 1), ("(", 0, 2), (")", 0, 3), ("/", 0, 4),

            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("√", 1, 3), ("*", 1, 4),

            ("log", 2, 0), ("ln", 2, 1), ("x²", 2, 2), ("xʸ", 2, 3), ("-", 2, 4),

            ("π", 3, 0), ("e", 3, 1), ("%", 3, 2), ("!", 3, 3), ("+", 3, 4),

            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), (".", 4, 3), ("=", 4, 4),

            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("0", 5, 3), ("Ans", 5, 4),

            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2),
        ]

        for text, row, column in buttons:
            button = QPushButton(text)
            button.setFixedSize(85, 55)
            button.setStyleSheet(get_button_style(text))
            button.clicked.connect(lambda checked, value=text: self.handle_button_click(value))

            button_layout.addWidget(button, row, column)

        main_layout.addLayout(button_layout)

        history_header_layout = QHBoxLayout()
        history_header_layout.addWidget(self.history_label)

        main_layout.addLayout(history_header_layout)
        main_layout.addWidget(self.history_list)
        main_layout.addWidget(self.clear_history_button)

        self.setLayout(main_layout)

    def handle_button_click(self, value: str):
        if value == "C":
            self.clear_display()

        elif value == "⌫":
            self.remove_last_character()

        elif value == "=":
            self.calculate_result()

        elif value == "sin":
            self.add_to_display("sin(")

        elif value == "cos":
            self.add_to_display("cos(")

        elif value == "tan":
            self.add_to_display("tan(")

        elif value == "log":
            self.add_to_display("log(")

        elif value == "ln":
            self.add_to_display("ln(")

        elif value == "√":
            self.add_to_display("sqrt(")

        elif value == "x²":
            self.add_to_display("**2")

        elif value == "xʸ":
            self.add_to_display("**")

        elif value == "π":
            self.add_to_display("pi")

        elif value == "e":
            self.add_to_display("e")

        elif value == "%":
            self.add_to_display("/100")

        elif value == "!":
            self.add_to_display("factorial(")

        elif value == "Ans":
            self.add_to_display(str(self.calculator.last_result))

        else:
            self.add_to_display(value)

    def add_to_display(self, value: str):
        self.display.setText(self.display.text() + value)

    def clear_display(self):
        self.display.clear()

    def remove_last_character(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])

    def calculate_result(self):
        expression = self.display.text()
        result = self.calculator.calculate(expression)

        self.display.setText(str(result))

        if result != "Erro" and expression:
            self.update_history_list()

    def update_history_list(self):
        """
        Atualiza a lista visual do histórico.
        """
        self.history_list.clear()

        for item in self.calculator.get_history():
            self.history_list.addItem(item)

        self.history_list.scrollToBottom()

    def clear_history(self):
        """
        Limpa o histórico da lógica e da interface.
        """
        self.calculator.clear_history()
        self.history_list.clear()