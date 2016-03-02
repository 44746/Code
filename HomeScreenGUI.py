from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
#Importing everything from all the required files 
from SquadListGUI import *
from MatchListGUI import *
from GoalListGUI import *
from teamSheet import *
#Class set up
class HomeScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Home")
		#Push button set up
		self.btnTeamSheet = QPushButton("Team Sheet")
		self.btnSquad = QPushButton("Squad")
		self.btnMatch = QPushButton("Match")
		self.btnGoals = QPushButton("Goals")
		self.btnQuit = QPushButton("Exit")

		
		#Setting up connections
		#Runs the 'ShowTS' function when the team sheet button is pushed
		self.btnTeamSheet.clicked.connect(self.ShowTS)
		#Runs the 'ShowSquad' function when the squad button is pushed
		self.btnSquad.clicked.connect(self.ShowSquad)
		#Runs the 'ShowMatch' function when the match button is pushed
		self.btnMatch.clicked.connect(self.ShowMatch)
		#Runs the 'ShowGoals' function when the goals button is pushed
		self.btnGoals.clicked.connect(self.ShowGoals)
		#Runs the 'QuitProgram' function when the quit button is pushed
		self.btnQuit.clicked.connect(self.QuitProgram)
		#Widget setting 
		self.layout = QVBoxLayout()

		self.layout.addWidget(self.btnTeamSheet)
		self.layout.addWidget(self.btnSquad)
		self.layout.addWidget(self.btnMatch)
		self.layout.addWidget(self.btnGoals)
		self.layout.addWidget(self.btnQuit)

		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
	
	def ShowTS(self):
		#Calls the FourFourTwo class
		self.team = FourFourTwo(self)
		#Shows the window
		self.team.show()
		#Raises the window to the front of the desktop
		self.team.raise_()
		#Hides the current window
		self.hide()

	def ShowSquad(self):
		#Calls the SquadList class
		self.squad = SquadList(self)
		#Shows the window
		self.squad.show()
		#Raises the window to the front of the desktop
		self.squad.raise_()
		#Hides the current window
		self.hide()

	def ShowMatch(self):
		#Calls the MatchList lass
		self.match = MatchList(self)
		#Shows the window
		self.match.show()
		#Raises the window to the front of the desktop
		self.match.raise_()
		#Hides the current window
		self.hide()

	def ShowGoals(self):
		#Calls the GoalList class
		self.goals = GoalList(self)
		#Shows the window
		self.goals.show()
		#Raises the window to the front of the desktop
		self.goals.raise_()
		#Hides the current window
		self.hide()

	def QuitProgram(self):
		#Exits the program
		sys.exit()
		

