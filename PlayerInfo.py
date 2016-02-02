from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *
from errorMessage import *

class PlayerInfo(QMainWindow):
	def __init__(self, parent,):
		super().__init__(parent)
		index = parent.squad_list.selectedIndexes()[0].row()
		

		
		self.parent = parent
		players = g_database.GetAllPlayers()
		self.players=players
		self.index = index
		self.setWindowTitle("Player Info")
		
		self.forename = QLineEdit(players[index][1])
		self.labelF = QLabel("Forename: ")
		
		self.surname = QLineEdit(players[index][2])
		self.labelS = QLabel("Surname: ")
		
		self.rating = QLineEdit(str(players[index][3]))
		self.labelR = QLabel("Rating: ")
		
		self.email = QLineEdit(players[index][4])
		self.labelE = QLabel("Email: ")
		
		self.position = QLineEdit(players[index][5])
		self.labelP = QLabel("Position: ")
		
		self.avaliable = QLineEdit(players[index][6])
		self.labelA = QLabel("Avaliable: ")
		
		self.btnSave = QPushButton("Save")
		self.btnDel = QPushButton("Delete")
		self.btnCancel = QPushButton("Cancel")
		
		self.hlayout1 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout_main = QVBoxLayout()
		self.hlayout2 = QHBoxLayout()
		
		self.vlayout1.addWidget(self.labelF)
		self.vlayout2.addWidget(self.forename)
		self.vlayout1.addWidget(self.labelS)
		self.vlayout2.addWidget(self.surname)
		self.vlayout1.addWidget(self.labelR)
		self.vlayout2.addWidget(self.rating)
		self.vlayout1.addWidget(self.labelE)
		self.vlayout2.addWidget(self.email)
		self.vlayout1.addWidget(self.labelP)
		self.vlayout2.addWidget(self.position)
		self.vlayout1.addWidget(self.labelA)
		self.vlayout2.addWidget(self.avaliable)
		
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		
		self.vlayout_main.addLayout(self.hlayout1)
		self.hlayout2.addWidget(self.btnSave)
		self.hlayout2.addWidget(self.btnDel)
		self.hlayout2.addWidget(self.btnCancel)
		
		self.vlayout_main.addLayout(self.hlayout2)
		
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout_main)
		self.setCentralWidget(self.widget)
	
		self.btnSave.clicked.connect(self.btnSave_pushed)
		self.btnDel.clicked.connect(self.btnDel_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
		
	
	def btnSave_pushed(self):
		forename = self.forename.text()
		surname = self.surname.text()
		rating = self.rating.text()
		email = self.email.text()
		position = self.position.text()
		avaliable = self.avaliable.text()
		PlayerID = self.players[self.index][0]
		
		#Validation
		email_valid = False
		rating_valid = False
		position_valid = False
		avaliable_valid = False
		
		if forename != "" and surname != "" and rating!= "" and email != "" and position != "" and avaliable != "":	
			#Email Validation
			at_valid = False
			dot_valid = False
			
			for each in email:
				if each == "@":
					at_valid = True
				if each == ".":
					dot_valid = True
			if at_valid == True and dot_valid == True:
					email_valid = True
			else:
				self.error = ErrorWindow(self,"Please enter a valid Email address")
				self.error.show()
				self.error.raise_()
			
		
			#Rating validation	
			if rating in ["0","1","2","3","4","5","6","7","8","9","10"]:
				rating_valid = True
			else:
				self.error = ErrorWindow(self,"Please enter a valid Rating")
				self.error.show()
				self.error.raise_()
			
			#Position Validation
			if position in ["GK","LB","CB","RB","LM","CM","RM","ST"]:
				position_valid = True
			else:
				self.error = ErrorWindow(self,"Please enter a valid Position")
				self.error.show()
				self.error.raise_()
			
			#Avaliable Validation
			if avaliable in ["Y","y","YES","Yes","N","n","NO","no"]:
				avaliable_valid = True
			else:
				self.error = ErrorWindow(self,"Please enter a valid avaliabilty")
				self.error.show()
				self.error.raise_()
				
		else:
			self.error = ErrorWindow(self,"You did not enter data into all the required fields")
			self.error.show()
			self.error.raise_()

		if email_valid == True and rating_valid == True and position_valid == True and avaliable_valid == True:
			g_database.UpdatePlayer(forename, surname, int(rating), email, position, avaliable,PlayerID)
			self.parent.show()
			self.parent.refresh_List()
			self.close()
		
	
		
		
	def btnDel_pushed(self):
		PlayerID = self.players[self.index][0]
		g_database.DeletePlayer(PlayerID)
		self.parent.show()
		self.parent.refresh_List()
		self.close()
	def btnCancel_pushed(self):
		self.parent.show()
		self.close()
