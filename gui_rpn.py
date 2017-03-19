#!/usr/bin/env python3

import rpn
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt

op = False

class Main(QtWidgets.QMainWindow):
 
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.initUI()
 
	def initUI(self):
 
		self.line = QtWidgets.QLineEdit(self)
		self.line.move(5,5)
		self.line.setReadOnly(True)
		self.line.setAlignment(Qt.AlignRight)
		self.line.resize(200,25)
 
		zero = QtWidgets.QPushButton("0",self)
		zero.move(10,180)
		zero.resize(35,30)
 
		one = QtWidgets.QPushButton("1",self)
		one.move(10,145)
		one.resize(35,30)
 
		two = QtWidgets.QPushButton("2",self)
		two.move(50,145)
		two.resize(35,30)
 
		three = QtWidgets.QPushButton("3",self)
		three.move(90,145)
		three.resize(35,30)
 
		four = QtWidgets.QPushButton("4",self)
		four.move(10,110)
		four.resize(35,30)
 
		five = QtWidgets.QPushButton("5",self)
		five.move(50,110)
		five.resize(35,30)
 
		six = QtWidgets.QPushButton("6",self)
		six.move(90,110)
		six.resize(35,30)
 
		seven = QtWidgets.QPushButton("7",self)
		seven.move(10,75)
		seven.resize(35,30)
 
		eight = QtWidgets.QPushButton("8",self)
		eight.move(50,75)
		eight.resize(35,30)
 
		nine = QtWidgets.QPushButton("9",self)
		nine.move(90,75)
		nine.resize(35,30)

		clear = QtWidgets.QPushButton("CE",self)
		clear.move(170,75)
		clear.resize(35,30)
		clear.clicked.connect(self.Clear)
		clear.setStyleSheet("color:red;")

		space = QtWidgets.QPushButton("_",self)
		space.move(90,180)
		space.resize(35,30)

		minus = QtWidgets.QPushButton("-",self)
		minus.move(130,145)
		minus.resize(35,30)

		point = QtWidgets.QPushButton(".",self)
		point.move(50,180)
		point.resize(35,30)
 
		plus = QtWidgets.QPushButton("+",self)
		plus.move(130,180)
		plus.resize(35,30)

		multiply = QtWidgets.QPushButton("*",self)
		multiply.move(130,110)
		multiply.resize(35,30)

		divide = QtWidgets.QPushButton("/",self)
		divide.move(130,75)
		divide.resize(35,30)
 
		squared = QtWidgets.QPushButton("^",self)
		squared.move(170,110)
		squared.resize(35,30)
 
		equal = QtWidgets.QPushButton("=",self)
		equal.move(170,145)
		equal.resize(35,65)
		equal.clicked.connect(self.Enter)
		equal.setStyleSheet("color:red;")

		nums = [zero,one,two,three,four,five,six,seven,eight,nine]
 
		ops = [minus,plus,multiply,divide,squared,point,space]
 
		for i in nums:
			i.setStyleSheet("color:blue;")
			i.clicked.connect(self.Number)
 
		for i in ops:
			i.setStyleSheet("color:red;")
			i.clicked.connect(self.Number)

		self.setGeometry(300,300,210,220)
		self.setFixedSize(210,220)
		self.setWindowTitle("")
		self.setWindowIcon(QtGui.QIcon(""))
		self.show()

	def Number(self):
		
		global op

		sender = self.sender()

		setNum = str(sender.text())

		if setNum == '_':
			setNum = ' '
 
		if op == False:
			self.line.setText(self.line.text() + setNum)
 
		else:
			self.line.setText(setNum)
			op = False

	def Clear(self):
		empty = ''
		self.line.setText(empty)

	def Enter(self):
		global op

		text = self.line.text()
		result = rpn.calculate(text)

		text = str(result)
		self.line.setText(text)
		op = True

def main():
	app = QtWidgets.QApplication(sys.argv)
	main= Main()
	main.show()
 
	sys.exit(app.exec_())
 
if __name__ == "__main__":
	main()
