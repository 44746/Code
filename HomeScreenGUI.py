from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from SquadListGUI import *
from MatchListGUI import *
from GoalListGUI import *
from teamSheet import *

class HomeScreen(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("Home")
		
		self.btnTeamSheet = QPushButton("Team Sheet")
		self.btnSquad = QPushButton("Squad")
		self.btnMatch = QPushButton("Match")
		self.btnGoals = QPushButton("Goals")
		self.btnQuit = QPushButton("Exit")

		

		self.btnTeamSheet.clicked.connect(self.ShowTS)
		self.btnSquad.clicked.connect(self.ShowSquad)
		self.btnMatch.clicked.connect(self.ShowMatch)
		self.btnGoals.clicked.connect(self.ShowGoals)
		self.btnQuit.clicked.connect(self.QuitProgram)

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
		self.team = FourFourTwo(self)
		self.team.show()
		self.team.raise_()
		self.hide()

		

	def ShowSquad(self):
		self.squad = SquadList(self)
		self.squad.show()
		self.squad.raise_()
		self.hide()

	def ShowMatch(self):
		self.match = MatchList(self)
		self.match.show()
		self.match.raise_()
		self.hide()

	def ShowGoals(self):
		self.goals = GoalList(self)
		self.goals.show()
		self.goals.raise_()
		self.hide()

	def QuitProgram(self):
		sys.exit()
		

