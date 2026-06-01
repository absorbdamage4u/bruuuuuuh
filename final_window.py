from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QPushButton
from config import *
from Underweight import *
from NormalWeight import *
from OverWeight import *
from Obesity import *

class Final_window(QWidget):
    def __init__(self, weight, height):
        super().__init__()
        # User data
        self.weight = float(weight)
        self.height = float(height)
        # BMI calculation
        self.bmi = self.weight / (self.height ** 2)

        self.appearance()
        self.initUi()
        self.connects()
        self.show()

    def appearance(self):
        self.setWindowTitle(windowT)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUi(self):
        # BMI condition checking
        if self.bmi < 18.5:
            self.condition = "Underweight"
        elif self.bmi < 25:
            self.condition = "Normal weight"
        elif self.bmi < 30:
            self.condition = "Overweight"
        else:
            self.condition = "Obesity"
        # Widgets
        self.final_txt = QLabel(f"-Your BMI result is: {self.bmi:.2f}")
        self.condition_txt = QLabel(f"-Body condition: {self.condition}")
        self.body_stat_btn = QPushButton(bodybutton)
        self.txtxt = QLabel("For your health and nutrition facts/tips. Click the button under.")
        # Layout
        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.final_txt)
        self.v_line.addWidget(self.condition_txt)
        self.v_line.addWidget(self.txtxt)
        self.v_line.addWidget(self.body_stat_btn)

        self.setLayout(self.v_line)

    def check_body(self):
        if self.condition == 'Underweight':
            self.hide()
            self.underWeight = Under_Weight_win()
            self.underWeight.show()

        elif self.condition == 'Normal weight':
            self.hide()
            self.normalWeight = Normal_Weight_win()
            self.normalWeight.show()

        elif self.condition == 'Overweight':
            self.hide()
            self.overWeight = Over_Weight_win()
            self.overWeight.show()

        elif self.condition == 'Obesity':
            self.hide()
            self.obesity = Obesity_win()
            self.obesity.show()

    def connects(self):
        self.body_stat_btn.clicked.connect(self.check_body)
    