from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from config import *
from final_window import *
class Second_window(QWidget):
    def __init__(self):
        super().__init__()
        self.appearance()
        self.initUi()
        self.connects()
        self.show()
    
    def appearance(self):
        self.setWindowTitle(windowT)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUi(self):
        # Widgets (texts, buttons..)
        self.secondT = QLabel(secondT)
        self.getWeight = QLineEdit()
        self.h = QLabel(hei)
        self.getHeight = QLineEdit()
        self.continu = QLabel(click_check_result)
        self.botn = QPushButton(b2n)
        #Layout + adding the widgs 
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.secondT)
        self.v_line.addWidget(self.getWeight)
        self.v_line.addWidget(self.h)
        self.v_line.addWidget(self.getHeight)
        self.v_line.addWidget(self.continu)
        self.v_line.addWidget(self.botn)
        # layout and 2nd windo
        self.setLayout(self.v_line)

    def connects(self):
        self.botn.clicked.connect(self.next_to_final)

    def next_to_final(self):
        weight = self.getWeight.text()
        height = self.getHeight.text()
        self.hide()
        self.final = Final_window(weight, height)
        self.final.show()