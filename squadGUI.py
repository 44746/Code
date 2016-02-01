from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PlayerDatabase import *
from AddPlayerGUI import *

class SquadList(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		self.setWindowTitle("Squad")
		self.btnNew = QPushButton("New Player")
		self.btnHome = QPushButton("Home")
		self.table = QTableWidget()
		
		self.refreshTable()
	
		self.btnNew.clicked.connect(self.btnNew_pushed)
		self.btnHome.clicked.connect(self.btnHome_pushed)
		self.VlayoutMAIN = QVBoxLayout()
		self.Vlayout = QVBoxLayout()
		self.Hlayout= QHBoxLayout()
		self.Hlayout.addWidget(self.btnNew)
		self.Hlayout.addWidget(self.btnHome)
		self.Vlayout.addWidget(self.table)
		self.VlayoutMAIN.addLayout(self.Vlayout)
		self.VlayoutMAIN.addLayout(self.Hlayout)		
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
	
	def btnNew_pushed(self):
		self.new_player = AddPlayer(self)
		self.new_player.show()
		self.new_player.raise_()
		self.hide()

	def btnHome_pushed(self):
		self.parent.show()
		self.close()
				
		
	def refreshTable(self):
		players = g_database.GetAllPlayers()
		self.table.setRowCount(len(players))
		self.table.setColumnCount(7)
		self.table.setHorizontalHeaderLabels(["Id","Forename","Surname","Rating","Email","Position","Avaliable"])
		row = -1
		for player in players:
			column = 0
			row = row+1
			for field in player:
				self.table.setItem(row, column, QTableWidgetItem(str(field)))
				column = column +1
