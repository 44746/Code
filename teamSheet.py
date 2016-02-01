import sys
from PyQt4 import QtGui
from PlayerSelect import *
from PlayerDatabase import *

from TeamLayoutData import *

class FourFourTwo(QtGui.QDialog):
	
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.setWindowTitle('Team Sheet')  

		#FORWARD
		self.lblSTR = QtGui.QPushButton(self.GetPlayer(10), self)
		self.lblSTR.move(225, 50)

		self.lblSTL = QtGui.QPushButton(self.GetPlayer(9), self)
		self.lblSTL.move(125, 50)

		
		#MIDFIELD
		self.lblRM = QtGui.QPushButton(self.GetPlayer(8), self)
		self.lblRM.move(325, 100)

		self.lblCMR = QtGui.QPushButton(self.GetPlayer(7), self)
		self.lblCMR.move(225, 100)

		self.lblCML = QtGui.QPushButton(self.GetPlayer(6), self)
		self.lblCML.move(125, 100)

		self.lblLM = QtGui.QPushButton(self.GetPlayer(5), self)
		self.lblLM.move(25, 100)
 
		#DEFENCE 
		self.lblRB = QtGui.QPushButton(self.GetPlayer(4), self)
		self.lblRB.move(325, 150)

		self.lblCBR = QtGui.QPushButton(self.GetPlayer(3), self)
		self.lblCBR.move(225, 150)

		self.lblCBL = QtGui.QPushButton(self.GetPlayer(2), self)
		self.lblCBL.move(125, 150)

		self.lblLB = QtGui.QPushButton(self.GetPlayer(1), self)
		self.lblLB.move(25, 150)

		#GK
		self.lblGK = QtGui.QPushButton(self.GetPlayer(0), self)
		self.lblGK.move(175, 200)

		self.btnHome = QtGui.QPushButton('Home', self)
		self.btnHome.move(275,250)
		
		self.btnClear = QtGui.QPushButton('Clear', self)
		self.btnClear.move(75,250)
		
		##
		self.setGeometry(350, 300, 425, 300)
		self.setWindowTitle('Team Sheet')
		
		self.btnHome.clicked.connect(self.Home)
		self.btnClear.clicked.connect(self.Clear)
		self.lblSTR.clicked.connect(self.btnAdd10)
		self.lblSTL.clicked.connect(self.btnAdd9)
		self.lblRM.clicked.connect(self.btnAdd8)
		self.lblCMR.clicked.connect(self.btnAdd7)
		self.lblCML.clicked.connect(self.btnAdd6)
		self.lblLM.clicked.connect(self.btnAdd5)
		self.lblRB.clicked.connect(self.btnAdd4)
		self.lblCBR.clicked.connect(self.btnAdd3)
		self.lblCBL.clicked.connect(self.btnAdd2)
		self.lblLB.clicked.connect(self.btnAdd1)
		self.lblGK.clicked.connect(self.btnAdd0)
	
	def Home(self):
		self.parent.show()
		self.close()
	
	def Clear(self):
		player_list = g_teamlayout.player_assigned
		for count, list_item in enumerate(player_list):
			g_teamlayout.player_assigned[count] = None
		self.refresh()
		
	def btnAdd0(self):
		self.btnAdd(0)
	def btnAdd1(self):
		self.btnAdd(1)
	def btnAdd2(self):
		self.btnAdd(2)
	def btnAdd3(self):
		self.btnAdd(3)
	def btnAdd4(self):
		self.btnAdd(4)
	def btnAdd5(self):
		self.btnAdd(5)
	def btnAdd6(self):
		self.btnAdd(6)
	def btnAdd7(self):
		self.btnAdd(7)
	def btnAdd8(self):
		self.btnAdd(8)
	def btnAdd9(self):
		self.btnAdd(9)
	def btnAdd10(self):
		self.btnAdd(10)
	
	
		
	def btnAdd(self, teamindex):
		self.PlayerAdd = PlayerSelect(self, teamindex)
		self.PlayerAdd.show()
		self.PlayerAdd.raise_()
		self.hide()

	def GetPlayer(self, teamsheetIndex):

		if g_teamlayout.player_assigned[teamsheetIndex] == None:
			return g_teamlayout.position[teamsheetIndex]
		else:
			return g_teamlayout.player_assigned[teamsheetIndex][2]
		
			
	def refresh(self):
		self.lblSTR.setText(self.GetPlayer(10))
		self.lblSTL.setText(self.GetPlayer(9))
		self.lblRM.setText(self.GetPlayer(8))
		self.lblCMR.setText(self.GetPlayer(7))
		self.lblCML.setText(self.GetPlayer(6))
		self.lblLM.setText(self.GetPlayer(5))
		self.lblRB.setText(self.GetPlayer(4))
		self.lblCBR.setText(self.GetPlayer(3))
		self.lblCBL.setText(self.GetPlayer(2))
		self.lblLB.setText(self.GetPlayer(1))
		self.lblGK.setText(self.GetPlayer(0))
		