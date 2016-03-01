from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class ErrorWindow(QMainWindow):
	def __init__(self,parent,error_message):
		super().__init__()
		#Widget setting
		self.error_message = error_message
		self.setWindowTitle("Error")
		#Setting the message to the passed in message from the parent
		self.message = QLabel(self.error_message)
		self.ok = QPushButton("OK")

		self.parent = parent

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.message)
		self.layout.addWidget(self.ok)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)

		self.setCentralWidget(self.widget)
		#Running the function 'back' if the button is pushed
		self.ok.clicked.connect(self.back)

	def back(self):
		#Showing the parent screen
		self.parent.show()
		#Raisng the parent screen to the front of the desktop
		self.parent.raise_()
		#Closing this window
		self.close()
