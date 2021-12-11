from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
QMessageBox, QRadioButton)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Программа Кирилла Ефремова')
question = QLabel('В каком году создался Brawl Stars&')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
btn_answer5 = QRadioButton('202222200')
layout_main = QVBoxLayout()

layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer5, alignment = Qt.AlignCenter)
main_win.setLayout(layout_main)
main_win.show()

app.exec_()