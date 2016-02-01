from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class ErrorWindow(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.setWindowTitle("Error")
		self.message = QLabel("You did not enter data into all the required fields")
		self.ok = QPushButton("OK")

		self.parent = parent

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.message)
		self.layout.addWidget(self.ok)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)

		self.setCentralWidget(self.widget)

		self.ok.clicked.connect(self.back)

	def back(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
