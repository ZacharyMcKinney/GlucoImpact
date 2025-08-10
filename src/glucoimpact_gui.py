from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout
)

class GlucoImpact_GUI:
    
    def __init__(self, app):
        self.app = app
        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)
        self._init_ui()
        self.app.exec()
    
    def _init_ui(self):
        win = self.window
        win.setWindowTitle("GlucoImpact")
        self.label = QLabel("<h1>This is my label</h1>", parent=win)
        self.button = QPushButton("Click me", parent=win)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        

        win.show() 
        
           
    
if __name__ == "__main__":
    gui = GlucoImpact_GUI(QApplication([]))
    