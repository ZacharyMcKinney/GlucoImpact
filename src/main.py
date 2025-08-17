## Copyright 2025, Zachary McKinney
import sys
import glucoimpactgui as gui
from PyQt6.QtWidgets import QApplication
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.GlucoImpactGUI()    
    window.show()
    app.exec()
    