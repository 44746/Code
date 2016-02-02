from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *

class AddGoal(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle("Add Goal")
	## Widget setting
		self.labelM = QLabel("Match: ")
		self.matchCombo = QComboBox()
		self.PopulateMatchComboBox()
		self.labelP = QLabel("Player: ")
		self.playerCombo = QComboBox()
		self.PopulatePlayerComboBox()
		
		
		self.quantity = QLineEdit()
		self.labelQ = QLabel("Quantity: ")
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		
		self.hlayout1 = QHBoxLayout()
		self.hlayout2 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
		
		
		self.vlayout1.addWidget(self.labelM)
		self.vlayout2.addWidget(self.matchCombo)
		self.vlayout1.addWidget(self.labelP)
		self.vlayout2.addWidget(self.playerCombo)
		self.vlayout1.addWidget(self.labelQ)
		self.vlayout2.addWidget(self.quantity)
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout3.addLayout(self.hlayout1)
		self.vlayout3.addLayout(self.hlayout2)
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)
	##Widget setting end
	
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
	
	def PopulatePlayerComboBox(self):
		players = g_database.GetAllPlayers()
		for player in players:
			self.playerCombo.addItem(player[2])
			
	def PopulateMatchComboBox(self):
		matches = g_database.GetAllMatches()
		for match in matches:
			print(match)
			self.matchCombo.addItem(match[2])
			
			
	def btnAdd_pushed(self):
		indexP= self.playerCombo.currentIndex()
		players = g_database.GetAllPlayers()
		name = players[indexP][2]
		indexM =self.matchCombo.currentIndex()
		matches = g_database.GetAllMatches()
		match = matches[indexM][2]
		
		quantity = self.quantity.text()
		if quantity != "":
			g_database.AddGoals(match,name,int(quantity))
			self.parent.show()
			self.parent.refreshTable()
			self.close()
		else:
			self.error = ErrorWindow(self,"You did not enter data into all the required fields")
			self.error.show()
			self.error.raise_()

		
	
	def btnCancel_pushed(self):
		self.parent.show()
		self.close()
