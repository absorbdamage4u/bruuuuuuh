from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from config import *
class Over_Weight_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appearence()
        self.initUi()
        self.show() 

    def appearence(self):
        self.setWindowTitle(windowT)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUi(self):
        self.txt = QLabel('Since you are Over-Weight. Here is your health/nutrition informations:')
        self.moretxt = QLabel(overweightmsg)
        self.bye2 = QLabel(byebye_msg)
    
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.txt)
        self.v_line.addWidget(self.moretxt)
        self.v_line.addWidget(self.bye2)

        self.setLayout(self.v_line)
