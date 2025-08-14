## Copyright 2025, Zachary McKinney

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QMainWindow,
    QHBoxLayout
)

class GlucoImpactGUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GlucoImpact")
        
        
        window_layout = QVBoxLayout()
        
        # -- TOP --
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Blood Glucose Impact"))
        header_layout.addWidget(QLabel("Details here about what to do"))
        window_layout.addLayout(header_layout, 2)
        
        middle_layout = QHBoxLayout()
        # -- BUTTON SIDEBAR --
        vert_left_layout = QVBoxLayout()
        vert_left_layout.addWidget(add_food_button := QPushButton("Login"))
        add_food_button.clicked.connect(self.login)
        vert_left_layout.addWidget(add_food_button := QPushButton("Add Food Entry by Picture"))
        add_food_button.clicked.connect(self.add_food_picture)
        vert_left_layout.addWidget(add_food_button := QPushButton("Add Food Entry"))
        add_food_button.clicked.connect(self.add_food_manually)
        vert_left_layout.addWidget(update_food_button := QPushButton("Update Food Entry"))
        update_food_button.clicked.connect(self.update_food)
        vert_left_layout.addWidget(remove_food_button := QPushButton("Remove Food Entry"))
        remove_food_button.clicked.connect(self.remove_food)
        vert_left_layout.addWidget(get_food_button :=QPushButton("View Food Impact"))
        get_food_button.clicked.connect(self.get_food_impact)
        vert_left_layout.addWidget(graph_button := QPushButton("Graph Overall Food Impact"))
        graph_button.clicked.connect(self.graph_foods)
        vert_left_layout.addWidget(quit_button := QPushButton("Exit"))
        quit_button.clicked.connect(self.quit)
        
        middle_layout.addLayout(vert_left_layout, 1)
        # -- MAIN CONTENT --
        vert_right_layout = QVBoxLayout()
        vert_right_layout.addWidget(QLabel("Main Content"))
        
        middle_layout.addLayout(vert_right_layout, 3)
        
        window_layout.addLayout(middle_layout, 7)
        # -- BOTTOM STATUS BAR --
        status_layout =  QHBoxLayout()
        status_layout.addWidget(QLabel("Status 1"))
        status_layout.addWidget(QLabel("Status 2"))

        window_layout.addLayout(status_layout, 1)
        
        widget = QWidget()
        widget.setLayout(window_layout)
        self.setCentralWidget(widget) 
        
    def login(self):
        # self.user_label.setText(f"User:{self.user_name} User ID:{self.user_id}")
        pass
    
    def add_food_picture(self):
        pass

    def add_food_manually(self):
        # dialogue prompt?
        # enter in food name, date, bgl change
        # need to hit a save button or back button
        pass
    
    def get_food_impact(self):
        # shows graphs
        # show avg bgl change after consuming food
        # select food from list or search for food
        # see optional notes?
        pass
   
    def remove_food(self):
        pass
    
    def update_food(self):
        pass
        
    def graph_foods(self):
        # bgl of all foods
        # filters
        # toggle between line and bar chart
        pass
    
    # def export_user_data(self):
        # pass
    
    def quit(self):
        QApplication.instance().quit()
        #exit application
        pass
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = GlucoImpactGUI()    
    window.show()
    app.exec()
    