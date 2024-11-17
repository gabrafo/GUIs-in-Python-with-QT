from PySide6.QtWidgets import QMainWindow, QPushButton

def button_clicked(action): # ação gerada quando recebemos um sinal
    print("Clicou ai?")

class ButtonHolder(QMainWindow): # herda de qmainwindow, podemos acessar métodos dessa classe
    def __init__(self): # construtor
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Click me!")
        button.setCheckable(True)

        button.clicked.connect(button_clicked) # envio do sinal

        self.setCentralWidget(button)