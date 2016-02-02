from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PlayerDatabase import *
from TeamLayoutData import *

class PlayerSelect(QMainWindow):
	def __init__(self,parent, teamindex):
		super().__init__(parent)
		self.parent = parent
		self.teamindex = teamindex
		self.setWindowTitle("Player Select")
		
		self.list = QListWidget()
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		self.VlayoutMAIN = QVBoxLayout()
		self.hlayout1 = QHBoxLayout()
		
		
		self.hlayout1.addWidget(self.btnAdd)
		self.hlayout1.addWidget(self.btnCancel)
		self.VlayoutMAIN.addWidget(self.list)
		self.VlayoutMAIN.addLayout(self.hlayout1)
	
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
	
		players = g_database.GetAllPlayers()
		row = -1
		self.list.clear()
		for player in players:
			if player[6] != "n" and player[6] != "N" and player[6] != "no" and player[6] != "No" and player[6] != "NO": 
				row = row+1
				name_list = ""
				name_list = name_list + (player[1][0]) + " "
				name_list = name_list + (player[2])
				self.list.addItem(name_list)
			
		
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
		
	def btnAdd_pushed(self):
		index = self.list.selectedIndexes()[0].row()
		player_data = self.list.selectedIndexes()[0].data()
		# linear search of gloal list using player_data as the search term.
		
		
		players = g_database.GetAllPlayers()
		
		for l_index, player in enumerate(players):
			if player[1][0]+" "+player[2] == player_data:
				index = l_index
				break
	
		g_teamlayout.player_assigned[self.teamindex] = player
		player_list = g_teamlayout.player_assigned
		
		# Get rid of the existing duplicate(s) of the player.
		
		for count, list_item in enumerate(player_list):
			if list_item != None and player_list[self.teamindex] == list_item and count != self.teamindex:
				g_teamlayout.player_assigned[count] = None
		
		g_teamlayout.player_assigned[self.teamindex] = player
		
		self.parent.show()
		self.parent.refresh()
		self.close()

		
	def btnCancel_pushed(self):
		self.parent.show()
		self.close()

