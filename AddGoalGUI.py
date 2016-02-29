from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PlayerDatabase import *

class AddGoal(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle("Add Goal")
	# Widget setting
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
	
	#Button Clicking
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
	#Adding each players Surname to a combo box
	def PopulatePlayerComboBox(self):
		#Retrieving all the player details from the database
		players = g_database.GetAllPlayers()
		for player in players:
			#Adds the players Surname to the combo box
			self.playerCombo.addItem(player[2])
	#Adding each match oppositon to a combo box		
	def PopulateMatchComboBox(self):
		#Retrieving all the Match details from the database
		matches = g_database.GetAllMatches()
		for match in matches:
			#Adds the match Opposition to the combo box
			self.matchCombo.addItem(match[2])
			
			
	def btnAdd_pushed(self):
		#Assigning 'indexP'(P for Player) to the seleceted index in the combo box
		indexP= self.playerCombo.currentIndex()
		#Retrieving all the player details from the database
		players = g_database.GetAllPlayers()
		#Assigning 'name' to the surname of the selected player from the combo box
		name = players[indexP][2]
		
		#Assigning 'indexM'(M for Match) to the seleceted index in the combo box
		indexM =self.matchCombo.currentIndex()
		#Retrieving all the Match details from the database
		matches = g_database.GetAllMatches()
		#Assigning 'match' to the oppositon of the selected match from the combo box
		match = matches[indexM][2]
		#Validation
		#Assigning 'quantity' to the inputted quantity as text
		quantity = self.quantity.text()
		#Checking its not blank
		if quantity != "":
			#Running the 'AddGoals' function in the database and adding the data inputted by the user
			g_database.AddGoals(match,name,int(quantity))
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
