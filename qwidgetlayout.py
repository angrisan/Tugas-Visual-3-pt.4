from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")
        btn3 = QPushButton("Button3")
        btn4 = QPushButton("Button4")
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
