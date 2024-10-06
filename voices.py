import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.screen = QLineEdit()
        self.layout.addWidget(self.screen)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', ' ',
            '1', '2', '3', '-', ' ',
            '0', '.', '=', '+', ' '
        ]

        row, col = 0, 0
        for button in buttons:
            if button != ' ':
                btn = QPushButton(button)
                btn.clicked.connect(self.on_click)
                self.grid_layout.addWidget(btn, row, col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.screen.clear()
        elif text == '=':
            try:
                result = str(eval(self.screen.text()))
                self.screen.setText(result)
            except Exception as e:
                self.screen.setText('Error')
        else:
            self.screen.setText(self.screen.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
