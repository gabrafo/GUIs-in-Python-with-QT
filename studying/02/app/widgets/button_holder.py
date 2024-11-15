from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow): # herda de qmainwindow, podemos acessar métodos dessa classe
    def __init__(self): # construtor
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Click me!")

        self.setCentralWidget(button)