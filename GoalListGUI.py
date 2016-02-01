from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PlayerDatabase import *
from AddGoalGUI import *

class GoalList(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle("Goals")
		self.btnNew = QPushButton("New Goal")
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
		self.new_goal = AddGoal(self)
		self.new_goal.show()
		self.new_goal.raise_()
		self.hide()
		
	def btnHome_pushed(self):
		self.parent.show()
		self.close()
		
		
	def refreshTable(self):
		Goals = g_database.GetAllGoals()
		self.table.setRowCount(len(Goals))
		self.table.setColumnCount(4)
		self.table.setHorizontalHeaderLabels(["Id","Oppositon","Player","Quantity"])
		row = -1
		for Goal in Goals:
			column = 0
			row = row+1
			for field in Goal:
				self.table.setItem(row, column, QTableWidgetItem(str(field)))
				column = column +1