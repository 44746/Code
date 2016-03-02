import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PlayerDatabase import *
from AddPlayerGUI import *
from PlayerInfo import *

class SquadList(QMainWindow):
	def __init__(self, parent):
		super().__init__()
		self.parent =parent

		self.setWindowTitle("Squad List")
				
		#Button set up
		self.btnInfo = QPushButton("Info")
		self.btnHome = QPushButton("Home")
		self.btnNew = QPushButton("New")
		#Widget set up
		self.squad_list = QListWidget()
		self.VlayoutMAIN = QVBoxLayout()
		self.hlayout1 = QHBoxLayout()
		
		self.hlayout1.addWidget(self.btnNew)
		self.hlayout1.addWidget(self.btnInfo)
		self.hlayout1.addWidget(self.btnHome)
		self.VlayoutMAIN.addWidget(self.squad_list)
		self.VlayoutMAIN.addLayout(self.hlayout1)
	
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
		#Running the refresh_List function
		self.refresh_List()
		#Button connections
		self.btnHome.clicked.connect(self.btnHome_pushed)
		self.btnInfo.clicked.connect(self.btnInfo_pushed)
		self.btnNew.clicked.connect(self.btnNew_pushed)
		
	
	def btnHome_pushed(self):
		#Show the parent window
		self.parent.show()
		#Close the current window
		self.close()
	
	def btnNew_pushed(self):
		#Call the AddPlayer class
		self.new_player = AddPlayer(self)
		#Show the window
		self.new_player.show()
		#Raise the window to the front of the desktop
		self.new_player.raise_()
		#Hide the current window
		self.hide()
		
	def btnInfo_pushed(self):	
		#Call the PlayerInfo class
		self.playerInfo = PlayerInfo(self)
		#Show the window
		self.playerInfo.show()
		#Raise the window to the front of the desktop
		self.playerInfo.raise_()
		#Hide the current window
		self.hide()
		
	def refresh_List(self):
		#Get all the players from the database(all entries)
		players = g_database.GetAllPlayers()
		row = -1
		#Clears the list
		self.squad_list.clear()
		#Runs the loop for each entry player in the players table
		for player in players:
			row = row+1
			#Sets up a blank list
			name_list = ""
			#Adds the forename intial to the list
			name_list = name_list + (player[1][0]) + " "
			#Adds the surname to the list
			name_list = name_list + (player[2])
			#Adds the player to the main list
			self.squad_list.addItem(name_list)
	