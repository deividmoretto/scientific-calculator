import sys
from PyQt6.QtWidgets import QApplication
from app.ui import CalculatorWindow

def main():
    app = QApplication(sys.argv)

    window = CalculatorWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()    