from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

from AddGoalGUI import *

        
if __name__ == "__main__":
    ##Create new application
    app = QApplication(sys.argv)
    ##instantiate window
    window = AddPlayer()
    window.show()
    window.raise_()
    app.exec_()
