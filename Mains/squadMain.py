from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

from squadGUI import *

        
if __name__ == "__main__":
    ##Create new application
    app = QApplication(sys.argv)
    ##instantiate window
    window = SquadList()
    window.show()
    window.raise_()
    app.exec_()
