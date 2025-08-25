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
    QHBoxLayout,
    QMainWindow,
    QStackedLayout,
    QTabWidget,
    QSpinBox,
    QMessageBox
)
from bgl_analyzer import BGL_Analyzer
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
import food_id as FID
import numpy as NP


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
        self.username_widget = QLineEdit()
        self.username_widget.setMaximumSize(150, 50)
        self.username_widget.setPlaceholderText("Login")
        login_button = QPushButton()
        login_button.clicked.connect(self.login)
        login_button.setMaximumSize(200, 50)
        login_button.setText("Submit")
        self.login_status = QLabel()
        layout.addWidget(user_label)
        layout.addWidget(self.username_widget)
        layout.addWidget(login_button)
        layout.addWidget(self.login_status)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def make_widget_identify_pic(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        prompt_label1 = QLabel()
        prompt_label1.setText("Select the photo of the food(s) you want to add")
        
        file_button = QPushButton()
        file_button.setText("Select Photo")
        file_button.clicked.connect(self.set_picture_location)
        
        prompt_label2 = QLabel()
        prompt_label2.setText("Submit picture for food identification")
        
        self.fid_status = QLabel()
        
        fid_button = QPushButton()
        fid_button.setText("Submit")
        fid_button.clicked.connect(self.refresh_fid_details)
        
        bgl_label = QLabel()
        bgl_label.setText("Enter the change in blood glucose levels experienced (The BGL spike).")
        bgl_spinbox = QSpinBox()
        bgl_spinbox.setMinimum(0)
        bgl_spinbox.setMaximum(250)
        bgl_spinbox.setMaximumSize(150, 50)
        
        submit_widget = QPushButton()
        submit_widget.clicked.connect(lambda: self.add_foods(self.fid_details, bgl_spinbox.text()))
        submit_widget.setMaximumSize(200, 50)
        submit_widget.setText("Submit foods to add to logs")
        
        layout.addWidget(prompt_label1)
        layout.addWidget(file_button)
        layout.addWidget(prompt_label2)
        layout.addWidget(fid_button)
        layout.addWidget(self.fid_status)
        layout.addWidget(bgl_label)
        layout.addWidget(bgl_spinbox)
        layout.addWidget(submit_widget)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def set_picture_location(self):
        self.picture_location = FID.get_img_location()
        
    def refresh_fid_details(self):
        self.fid_details: str = FID.identify_food(self.picture_location)
        self.fid_status.setText(self.fid_details)
    
    def add_foods(self, lines, bgl_delta):
        if lines == "":
            msg = QMessageBox()
            msg.setWindowTitle("GlucoImpact: Error")
            msg.setText("Please make sure foods were identified")
            msg.exec()
        if bgl_delta is None:
            msg = QMessageBox()
            msg.setWindowTitle("GlucoImpact: Error")
            msg.setText("Please select a Blood Glucose Change")
            msg.exec()
        foods = lines.split("\n")
        for food in foods[1:]:
            self.add_food(food, bgl_delta)
    
    def make_widget_add_entry(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        food_prompt = QLabel()
        food_prompt.setText("Enter in the food you ate.")
        food_lineedit = QLineEdit()
        food_lineedit.setMaximumSize(150, 50)
        food_lineedit.setPlaceholderText("Food")
        
        bgl_prompt = QLabel()
        bgl_prompt.setText("Enter the change in blood glucose levels experienced (The BGL spike).")
        bgl_spinbox = QSpinBox()
        bgl_spinbox.setMinimum(0)
        bgl_spinbox.setMaximum(250)
        bgl_spinbox.setMaximumSize(150, 50)
        
        submit_button = QPushButton()
        submit_button.clicked.connect(lambda: self.add_food(food_lineedit.text().strip().lower(), bgl_spinbox.value()))
        submit_button.setMaximumSize(200, 50)
        submit_button.setText("Submit")
        
        self.entry_label = QLabel()
        
        layout.addWidget(food_prompt)
        layout.addWidget(food_lineedit)
        layout.addWidget(bgl_prompt)
        layout.addWidget(bgl_spinbox)
        layout.addWidget(submit_button)
        layout.addWidget(self.entry_label)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def make_widget_remove_entry(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        entry_id_prompt = QLabel()
        entry_id_prompt.setText("Enter in the entry ID you want to remove.")
        entry_id_spinbox = QSpinBox()
        entry_id_spinbox.setMinimum(0)
        entry_id_spinbox.setMaximum(99999)
        entry_id_spinbox.setMaximumSize(150, 50)
        
        submit_button = QPushButton()
        submit_button.clicked.connect(lambda: self.remove_entry(entry_id_spinbox.text()))
        submit_button.setMaximumSize(200, 50)
        submit_button.setText("Submit")
        
        entries_label = QLabel()
        
        refresh_button = QPushButton()
        refresh_button.clicked.connect(lambda: self.refresh_entries_label(entries_label))
        refresh_button.setMaximumSize(200, 50)
        refresh_button.setText("Refresh")
        
        self.remove_entry_label = QLabel()
        
        layout.addWidget(entry_id_prompt)
        layout.addWidget(entry_id_spinbox)
        layout.addWidget(submit_button)
        layout.addWidget(refresh_button)
        layout.addWidget(self.remove_entry_label)
        layout.addWidget(entries_label)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
    
    def refresh_entries_label(self, entries_label):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        entries = self.bgl_analyzer.db_manager.get_entries_by_user(self.user_id)
        log = ""
        # entry = {entry_id, user_id, food_id, bgl_delta}
        for entry in entries:
            food = self.bgl_analyzer.db_manager.get_food_by_id(entry[2])[1]
            log += (f"Entry ID: {entry[0]}      Food: {food}       BGL: {entry[3]}\n")
        entries_label.setText(log)
        
    
    def make_widget_view_impact(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        prompt_label1 = QLabel()
        prompt_label1.setText("Type the food to see impact you want to view")
        
        impact_input = QLineEdit()
        impact_input.setMaximumSize(150, 50)
        impact_input.setPlaceholderText("Food")
        
        prompt_label2 = QLabel()
        prompt_label2.setText("Foods are below")
        
        list_of_foods = QLabel()
        
        refresh_button = QPushButton()
        refresh_button.setText("Refresh")
        refresh_button.clicked.connect(lambda: self.refresh_list_of_foods(list_of_foods))
        
        fig = Figure()
        data_output = QLabel()
        canvas = FigureCanvas(fig)
        canvas.setMaximumSize(800, 600)
        submit_widget = QPushButton()
        submit_widget.clicked.connect(lambda: self.show_food_impact(impact_input.text(), fig, canvas, data_output))
        submit_widget.setMaximumSize(200, 50)
        submit_widget.setText("Submit food view impact")
        
        layout.addWidget(prompt_label1)
        layout.addWidget(impact_input)
        layout.addWidget(prompt_label2)
        layout.addWidget(refresh_button)
        layout.addWidget(list_of_foods)
        layout.addWidget(submit_widget)
        layout.addWidget(data_output)
        layoutoutside = QHBoxLayout()
        layoutoutside.addLayout(layout)
        layoutoutside.addWidget(canvas)
        widget = QWidget()
        widget.setLayout(layoutoutside)
        return widget
    
    def refresh_list_of_foods(self, widget):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        foods = self.bgl_analyzer.db_manager.get_unique_foods_by_user(self.user_id)
        text = ""
        for food in foods:
            text += food[0] +"\n"
        widget.setText(text)
    
    def make_widget_graph(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        prompt_label1 = QLabel()
        prompt_label1.setText("Refresh to see food impact graph")

        fig = Figure()
        data_output = QLabel()
        canvas = FigureCanvas(fig)
        submit_widget = QPushButton()
        submit_widget.clicked.connect(lambda: self.graph_foods(fig, canvas))
        submit_widget.setMaximumSize(200, 50)
        submit_widget.setText("Refresh")
        
        layout.addWidget(prompt_label1)
        layout.addWidget(submit_widget)
        layout.addWidget(data_output)
        layout.addWidget(canvas)
        widget = QWidget()
        widget.setLayout(layout)
        return widget
        
    def graph_foods(self, fig, canvas):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        fig.clear()
        ax = fig.add_subplot(111)
        entries = self.bgl_analyzer.db_manager.get_entries_by_user(self.user_id)
        food_data = {}
        for entry in entries:
            food_id = entry[2]
            bgl_delta: int = entry[3]
            food_name: str = self.bgl_analyzer.db_manager.get_food_by_id(food_id)[1]
            if food_name not in food_data:
                food_data[food_name] = []
            food_data[food_name].append(int(bgl_delta))
             
        foods = list(food_data.keys())
        medians = []
        stds = []
        for val in food_data.values():
            medians.append(NP.median(val))
            stds.append(NP.std(val))
            
        ax.bar(foods, medians, yerr=stds, capsize=5)
        ax.set_ylabel("Median Blood Glucose Change (mg/dL)")
        ax.set_title("BGL Impact Comparison Across Foods")
        ax.set_xticklabels(foods, rotation=45, ha="right")
        canvas.draw()
    
    def is_logged_in(self):
        return hasattr(self, "bgl_analyzer")
    
    def throw_login_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("GlucoImpact: Error")
        msg.setText("Please login to view foods")
        msg.exec()
    
    def login(self):
        user_name = self.username_widget.text().strip().lower()
        if not hasattr(self, "bgl_analyzer") or user_name != self.bgl_analyzer.user:
            self.user_name = user_name
            self.bgl_analyzer = BGL_Analyzer(self.user_name)
            self.user_id = self.bgl_analyzer.db_manager.get_user_by_name(self.user_name)[0]
            self.login_status.setText(f"Logged in as {self.user_name} and ID: {self.user_id}")

    def add_food(self, food: str, bgl_delta: int):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        self.bgl_analyzer.add_bgl(food, bgl_delta)
        self.entry_label.setText(f"Added food: {food} to database with BGL: {bgl_delta}")
    
    def remove_entry(self, entry_id: int):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        self.bgl_analyzer.db_manager.delete_food_entry(entry_id)
        self.remove_entry_label.setText(f"Removed Entry ID #{entry_id}")
        self.refresh_entries_label()
            
    def show_food_impact(self, food, fig: Figure, canvas, data_output: QLabel):
        if not self.is_logged_in():
            self.throw_login_message()
            return
        food_id = self.bgl_analyzer.db_manager.get_food_by_name(food)[0]
        entries = (self.bgl_analyzer.db_manager.get_entries_by_user_and_food(self.user_id, food_id))
        bgl_data = [entry[3] for entry in entries]
        fig.clear()
        ax = fig.add_subplot()
        ax.boxplot(bgl_data, vert=False)
        ax.set_title(f"Box plot for food {food}")
        ax.set_xlabel("Blood glucose in (mg/dL)")
        
        data_output.setText(self.bgl_analyzer.get_describe_bgl(food_id).to_string())
        canvas.draw()
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = GlucoImpactGUI()  
    window.resize(1280, 720)  
    window.show()
    app.exec()