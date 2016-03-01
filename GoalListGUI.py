from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PlayerDatabase import *
from AddGoalGUI import *

class GoalList(QMainWindow):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle("Goals")
		#Setting up buttons
		self.btnNew = QPushButton("New Goal")
		self.btnHome = QPushButton("Home")
		
		
		#Widget setting
		
		self.table = QTableWidget()
		
		self.refreshTable()
		#Running the function 'btn' when the new button is pushed
		self.btnNew.clicked.connect(self.btnNew_pushed)
		#Running the function 'btnHome_pushed' when the home button is pushed
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
		#Calls the AddGoal class
		self.new_goal = AddGoal(self)
		#Shows the window
		self.new_goal.show()
		#Raises the window to the front of the desktop
		self.new_goal.raise_()
		#Hides the current window
		self.hide()
		
	def btnHome_pushed(self):
		#Shows the parent window
		self.parent.show()
		#Closes the current window
		self.close()
		
		
	def refreshTable(self):
		#Gets all goals from the database
		Goals = g_database.GetAllGoals()
		#Sets the row count to the number of entries 
		self.table.setRowCount(len(Goals))
		#Sets the column count to 4
		self.table.setColumnCount(4)
		#Labels each of the column headers
		self.table.setHorizontalHeaderLabels(["Id","Oppositon","Player","Quantity"])
		row = -1
		#Adds each item in the database to table under the correct header row by row
		for Goal in Goals:
			column = 0
			row = row+1
			for field in Goal:
				#Actually adding the item to the table
				self.table.setItem(row, column, QTableWidgetItem(str(field)))
				column = column +1