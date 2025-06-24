## Copyright 2025, Zachary McKinney

import tkinter as tk
import db_manager as DB
from tkinter import filedialog
class BGL_Analyzer:


    def __init__(self, user, database_name):
        """
        Initiate an Analyzer object with a dedicated user and uses the database
        associated with the user
        User is a string ID, and DB is a filename to a Sqlite file or new file

        Args:
            user (str): user_id to be used in the database
            db (str): filename to Sqlite database
        """
        
        ########
        #rework this, no time right now
        self.db_filename = database_name
        self._user = user
        self.connection = DB.sqlite3.connection(self.db_filename)
        self.cursor = DB.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()
        self.cursor.commit()
        ########
    
    #mainly for testing, but file location
    def get_foods(self, file_location):
        pass
    
    def get_bgl_spike(self, time):
        pass
    
    #use lambda to make it easier to read and complete
    #set={}
    def add_foods(self, foods, bgl_spike):
        """
        Enters in a bgl spike for set of foods given into the local database
        
        Args:
            foods (set of strings): Identified foods consumed at a bgl spike
            bgl_spike (int or double): Max bgl after food - avg bgl for the day

        Raises:
            Exception: Needs at least one food to be added
        """
        if len(foods) <= 0:
            raise Exception("Set of foods can't be empty")
        
    
    #either use a library for this to do it automatically
    #or calculate manually?
    def calculate_correlation(self, food):
        pass
    
    def add_meal_consumed(self, bgl_delta, date, time_of_day):
        pass
    
    def link_food_to_meal(self, meal_id, food_id, portion=1):
        pass
    
    #blood glucose for all time. For use if you can connect to
    #a glucose monitoring app or device
    def get_avg_alltime_BGL(self):
        pass
    
    #Blood glucose level for the day
    def get_avg_BGL(self):
        pass
    
    #return the BGl for a food (only values, no dates) 
    def _get_food_BGL_data(self, food):
        pass
    
    #update the all time average. Maybe include the date in the database avgerage. Could possibly display trend of BGL over time
    def _update_avg_BGL(self):
        pass
    
    def print_database(self):
        pass
    