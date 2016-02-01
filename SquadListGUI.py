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
				
		self.squad_list = QListWidget()
		self.btnInfo = QPushButton("Info")
		self.btnHome = QPushButton("Home")
		self.btnNew = QPushButton("New")
		
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
		

		self.refresh_List()
		
		self.btnHome.clicked.connect(self.btnHome_pushed)
		self.btnInfo.clicked.connect(self.btnInfo_pushed)
		self.btnNew.clicked.connect(self.btnNew_pushed)
		
	
	def btnHome_pushed(self):
		self.parent.show()
		self.close()
	
	def btnNew_pushed(self):
		self.new_player = AddPlayer(self)
		self.new_player.show()
		self.new_player.raise_()
		self.hide()
		
	def btnInfo_pushed(self):	
		self.playerInfo = PlayerInfo(self)
		self.playerInfo.show()
		self.playerInfo.raise_()
		self.hide()
		
	def refresh_List(self):
		players = g_database.GetAllPlayers()
		row = -1
		self.squad_list.clear()
		for player in players:
			row = row+1
			name_list = ""
			name_list = name_list + (player[1][0]) + " "
			name_list = name_list + (player[2])
			self.squad_list.addItem(name_list)
	