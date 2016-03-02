from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

from HomeScreenGUI import *

#Runs the HomeScreen class        
if __name__ == "__main__":
    ##Create new applicatin
    app = QApplication(sys.argv)
    ##instantiate window
    window = HomeScreen()
    window.show()
    window.raise_()
    app.exec_()
