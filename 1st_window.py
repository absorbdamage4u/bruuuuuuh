from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from config import *
from secondary import *
class Main_window(QWidget):
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
        # texts / button
        self.introT = QLabel(introd_text)
        self.intoTask = QLabel(intro_task)
        self.moreT = QLabel(moretalking)
        self.Rq = QLabel(remarqueTxt)
        self.btn = QPushButton(buttonT)
        
        #layout + adding the widgs in layout
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.introT)
        self.v_line.addWidget(self.intoTask)
        self.v_line.addWidget(self.Rq)
        self.v_line.addWidget(self.moreT)
        self.v_line.addWidget(self.btn)
        #lay to wind
        self.setLayout(self.v_line)
    
    def connects(self):
        self.btn.clicked.connect(self.next_page)

    def next_page(self):
        self.hide()
        self.second = Second_window()
        self.second.show()    
app = QApplication([])
window = Main_window()
app.exec_()