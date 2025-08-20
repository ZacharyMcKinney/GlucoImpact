## Copyright 2025, Zachary McKinney

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QStackedLayout,
    QTabWidget,
    QSpinBox,
    QMessageBox
)
from bgl_analyzer import BGL_Analyzer
import food_id as FID

class GlucoImpactGUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GlucoImpact")
        
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.stacklayout = QStackedLayout()
        
        tabs.addTab(self.make_widget_login(), "Login")
        tabs.addTab(self.make_widget_identify_pic(), "Add Food Entry By Picture")
        tabs.addTab(self.make_widget_add_entry(), "Add Food Entry")
        tabs.addTab(self.make_widget_remove_entry(), "Remove Food Entry")
        tabs.addTab(self.make_widget_view_impact(), "View Food Impact")
        tabs.addTab(self.make_widget_graph(), "Graph Overall Food Impact")
        
        self.setCentralWidget(tabs) 
    
    def make_widget_login(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        user_label = QLabel()
        user_label.setText("Enter in user name")
        self.widget_user_name = QLineEdit()
        self.widget_user_name.setMaximumSize(150, 50)
        self.widget_user_name.setPlaceholderText("Login")
        self.widget_login_submit = QPushButton()
        self.widget_login_submit.clicked.connect(self.login)
        self.widget_login_submit.setMaximumSize(200, 50)
        self.widget_login_submit.setText("Submit")
        self.login_status = QLabel()
        layout.addWidget(user_label)
        layout.addWidget(self.widget_user_name)
        layout.addWidget(self.widget_login_submit)
        layout.addWidget(self.login_status)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def make_widget_identify_pic(self):
        pass
    
    def make_widget_add_entry(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        food_label = QLabel()
        food_label.setText("Enter in the food you ate.")
        widget_food = QLineEdit()
        widget_food.setMaximumSize(150, 50)
        widget_food.setPlaceholderText("Food")
        
        bgl_label = QLabel()
        bgl_label.setText("Enter the change in blood glucose levels experienced (The BGL spike).")
        widget_bgl = QSpinBox()
        widget_bgl.setMinimum(0)
        widget_bgl.setMaximum(350)
        widget_bgl.setMaximumSize(150, 50)
        
        widget_submit = QPushButton()
        widget_submit.clicked.connect(lambda: self.add_food(widget_food.text().strip().lower(), widget_bgl.value()))
        widget_submit.setMaximumSize(200, 50)
        widget_submit.setText("Submit")
        
        self.entry_label = QLabel()
        
        layout.addWidget(food_label)
        layout.addWidget(widget_food)
        layout.addWidget(bgl_label)
        layout.addWidget(widget_bgl)
        layout.addWidget(widget_submit)
        layout.addWidget(self.entry_label)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def make_widget_remove_entry(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        entry_id_label = QLabel()
        entry_id_label.setText("Enter in the entry ID you want to remove.")
        widget_entry_id = QSpinBox()
        widget_entry_id.setMinimum(0)
        widget_entry_id.setMaximum(99999)
        widget_entry_id.setMaximumSize(150, 50)
        
        widget_submit = QPushButton()
        widget_submit.clicked.connect(lambda: self.remove_entry(widget_entry_id.text()))
        widget_submit.setMaximumSize(200, 50)
        widget_submit.setText("Submit")
        
        refresh_btt = QPushButton()
        refresh_btt.clicked.connect(self.refresh_entries_label)
        refresh_btt.setMaximumSize(200, 50)
        refresh_btt.setText("Refresh")
        
        self.remove_entry_label = QLabel()
        self.entries = QLabel()
        
        layout.addWidget(entry_id_label)
        layout.addWidget(widget_entry_id)
        layout.addWidget(widget_submit)
        layout.addWidget(refresh_btt)
        layout.addWidget(self.remove_entry_label)
        layout.addWidget(self.entries)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def refresh_entries_label(self):
        if hasattr(self, "bgl_analyzer"):
            entries = self.bgl_analyzer.db_manager.get_entries_by_user(self.user_id)
            log = ""
            # entry = {entry_id, user_id, food_id, bgl_delta}
            for entry in entries:
                food = self.bgl_analyzer.db_manager.get_food_by_id(entry[2])[1]
                log += (f"Entry ID: {entry[0]}      Food: {food}       BGL: {entry[3]}\n")
            self.entries.setText(log)
        
    
    def make_widget_view_impact(self):
        pass
    
    def make_widget_graph(self):
        pass
        
    def login(self):
        user_name = self.widget_user_name.text().strip().lower()
        if not hasattr(self, "bgl_analyzer") or user_name != self.bgl_analyzer.user:
            self.user_name = user_name
            self.bgl_analyzer = BGL_Analyzer(self.user_name)
            self.user_id = self.bgl_analyzer.db_manager.get_user_by_name(self.user_name)[0]
            self.login_status.setText(f"Logged in as {self.user_name} and ID: {self.user_id}")

    def add_food(self, food: str, bgl_delta: int):
        if hasattr(self, "bgl_analyzer"):
            self.bgl_analyzer.add_bgl(food, bgl_delta)
            self.entry_label.setText(f"Added food: {food} to database with BGL: {bgl_delta}")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("GlucoImpact: Error")
            msg.setText("Please login to add foods")
            msg.exec()
    
    def remove_entry(self, entry_id: int):
        if hasattr(self, "bgl_analyzer"):
            self.bgl_analyzer.db_manager.delete_food_entry(entry_id)
            self.remove_entry_label.setText(f"Removed Entry ID #{entry_id}")
            self.refresh_entries_label()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("GlucoImpact: Error")
            msg.setText("Please login to delete an entry")
            msg.exec()
            
    def get_food_impact(self):
        # shows graphs
        # show avg bgl change after consuming food
        # select food from list or search for food
        # see optional notes?
        pass
        
    def graph_foods(self):
        # bgl of all foods
        # filters
        # toggle between line and bar chart
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = GlucoImpactGUI()  
    window.resize(1280, 720)  
    window.show()
    app.exec()