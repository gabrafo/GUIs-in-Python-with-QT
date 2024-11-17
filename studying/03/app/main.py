from PySide6.QtWidgets import QApplication, QSlider

def slider_moved(action): # ação gerada quando recebemos um sinal
    print("Slider moved to: ", action)

app = QApplication()
slider = QSlider()
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(slider_moved) # envio do sinal
slider.show()
app.exec()