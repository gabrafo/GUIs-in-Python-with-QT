from PySide6.QtWidgets import QApplication, QWidget

# para argumentos no terminal
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# começa o laço de execução
app.exec()