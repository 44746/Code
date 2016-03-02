from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *
from errorMessage import *
class AddPlayer(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		
		self.parent = parent
		
		self.setWindowTitle("Add Player")
		#Widget setting
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		
		self.rating = QLineEdit()
		self.labelR = QLabel("Rating: ")
		
		self.email = QLineEdit()
		self.labelE = QLabel("Email: ")
		
		self.position = QLineEdit()
		self.labelP = QLabel("Position: ")
		
		self.avaliable = QLineEdit()
		self.labelA = QLabel("Avaliable: ")
		
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		self.hlayout1 = QHBoxLayout()
		self.vlayout1 = QVBoxLayout()
		self.vlayout2 = QVBoxLayout()
		self.vlayout3 = QVBoxLayout()
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
		self.vlayout1.addWidget(self.btnAdd)
		self.vlayout2.addWidget(self.btnCancel)
		self.hlayout1.addLayout(self.vlayout1)
		self.hlayout1.addLayout(self.vlayout2)
		self.vlayout3.addLayout(self.hlayout1)
		self.hlayout2.addWidget(self.btnAdd)
		self.hlayout2.addWidget(self.btnCancel)
		self.vlayout3.addLayout(self.hlayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.vlayout3)
		self.setCentralWidget(self.widget)
	
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
		
	
	def btnAdd_pushed(self):
		#Assigning 'forename' to the inputted forename as text
		forename = self.forename.text()
		#Assigning 'surname' to the inputted surname as text
		surname = self.surname.text()
		#Assigning 'rating' to the inputted rating as text
		rating = self.rating.text()
		#Assigning 'email' to the inputted email as text
		email = self.email.text()
		#Assigning 'position' to the inputted position as text
		position = self.position.text()
		#Assigning avaliable to the inputted avaliable  as text
		avaliable = self.avaliable.text()
		
		#Validation
		email_valid = False
		rating_valid = False
		position_valid = False
		avaliable_valid = False
		forename_valid = False
		surname_valid = False
		#Checking that each field has an entry of some sort
		if forename != "" and surname != "" and rating!= "" and email != "" and position != "" and avaliable != "":	
			#Setting up alphabet lists
			alphabet_lower = []
			alphabet_upper =[]
			#Adding each lower case letter to the lower list
			for letter in map(chr, range(97, 123)):
				alphabet_lower.append(letter)
			#Adding each upper case letter to the upper list
			for letter in map(chr, range(65,91)):
				alphabet_upper.append(letter)
			#Forename validation
			forename_valid = True
			count = -1
			for each in forename:
				count = count +1
				#Checking the first letter
				if count == 0:
					#Checking if its a capital letter
					if forename[count] not in alphabet_upper:
						forename_valid = False
				#Checking the rest of the entry	
				else:
					#Checking the letter is lower case
					if forename_valid == True and each not in alphabet_lower:
						forename_valid = False
					
			if forename_valid == False:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid Forename")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()
				
			#Surname validation
			surname_valid = True
			count = -1
			for each in surname:
				count = count +1
				#Checking the first letter
				if count == 0:
					#Checking its a capital letter
					if surname[count] not in alphabet_upper:
						surname_valid = False
				#Checking the rest of the entry
				else:
					#Checking the letter is lower case
					if surname_valid == True and each not in alphabet_lower:
						surname_valid = False
						
			if surname_valid == False:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid Surname")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()			
			
			#Email Validation
			at_valid = False
			dot_valid = False
			#Checking the email contains an @ and . symbol
			for each in email:
				if each == "@":
					at_valid = True
				if each == ".":
					dot_valid = True
			#Setting email_valid to true if the input contains an @ and an .		
			if at_valid == True and dot_valid == True:
					email_valid = True

			else:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid Email address")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()
			
		
			#Rating validation
			#List of valid entries
			if rating in ["0","1","2","3","4","5","6","7","8","9","10"]:
				rating_valid = True
			else:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid Rating")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()
			
			#Position Validation
			#List of valid entries
			if position in ["GK","LB","CB","RB","LM","CM","RM","ST"]:
				position_valid = True
			else:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid Position")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()
			
			#Avaliable Validation
			#List of valid entries
			if avaliable in ["Y","y","YES","Yes","N","n","NO","no"]:
				avaliable_valid = True
			else:
				#Running the Error widget, passing in the message to display
				self.error = ErrorWindow(self,"Please enter a valid avaliabilty")
				#Showing the error window
				self.error.show()
				#Raising the error window to the front of the screen
				self.error.raise_()
				
		else:
			#Running the Error widget, passing in the message to display
			self.error = ErrorWindow(self,"Please enter data into all the required fields")
			#Showing the error window
			self.error.show()
			#Raising the error window to the front of the screen
			self.error.raise_()
		#Checking all the valid statements are all true
		if email_valid == True and rating_valid == True and position_valid == True and avaliable_valid == True and forename_valid == True and surname_valid == True:
			#Updating the database by running the UpdatePlayer function
			g_database.AddPlayer(forename, surname, int(rating), email, position, avaliable)
			#Showing the parent window
			self.parent.show()
			#Running the refresh_List function in the parent window
			self.parent.refresh_List()
			#Closing the current window
			self.close()
	
		

	def btnCancel_pushed(self):
		#Showing the parent window
		self.parent.show()
		#Closing the current window
		self.close()
