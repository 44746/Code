from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *
from errorMessage import *

class AddMatch(QMainWindow):
	def __init__(self,parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle("Add Match")
		# Widget setting
		self.date = QLineEdit()
		self.labelD = QLabel("Date: ")
		self.opposition = QLineEdit()
		self.labelO = QLabel("Opposition: ")
		self.result = QLineEdit()
		self.labelR = QLabel("Result: ")
		
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		self.hlayout1 = QHBoxLayout()
		self.hlayout2 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
		
		self.vlayout1.addWidget(self.labelD)
		self.vlayout2.addWidget(self.date)
		self.vlayout1.addWidget(self.labelO)
		self.vlayout2.addWidget(self.opposition)
		self.vlayout1.addWidget(self.labelR)
		self.vlayout2.addWidget(self.result)
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout3.addLayout(self.hlayout1)
		self.vlayout3.addLayout(self.hlayout2)
		
		
		
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)
		
		
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
	
	def btnAdd_pushed(self):
		#Assigning 'date' to the inputted date as text
		date = self.date.text()
		#Assigning 'opposition' to the inputted opposition as text
		opposition=self.opposition.text()
		#Assigning 'result' to the inputted result as text
		result = self.result.text()
		
		#Checking that each field has an entry
		if date != "" and opposition != "" and result!="":
			#Running the 'AddMatch' function in the database and adding the data inputted by the user
			g_database.AddMatch(date,opposition,result)
			#Showing the window that this window was activated from
			self.parent.show()
			#Running the 'refreshTable' function in the parent window
			self.parent.refreshTable()
			#Closing this window
			self.close()
		else:
			#Running the Error widget, passing in the message to display
			self.error = ErrorWindow(self,"You did not enter data into all the required fields")
			#Showing the error window
			self.error.show()
			#Raising the error window to the front of the screen
			self.error.raise_()
	
	def btnCancel_pushed(self):
		#Showing the window that this window was activated from
		self.parent.show()
		#Closing this window
		self.close()

	