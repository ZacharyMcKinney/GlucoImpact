## Copyright 2025, Zachary McKinney

import sqlite3

# Note to Self: Implement crud? create, retrieve, update, delete functions
class BGL_Analyzer:


    def __init__(self, user, db):
        """
        Initiate an Analyzer object with a dedicated user and uses the database
        associated with the user
        User is a string ID, and DB is a filename to a Sqlite file or new file

        Args:
            user (str): user_id to be used in the database
            db (str): filename to Sqlite database
        """
        
        self.db_filename = db
        self._user = user
        self.connection = sqlite3.connection(self.db_filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()
        self.cursor.commit()
        
    def close_cursor(self):
        """
        Closes database cursor connection.
        Init doesn't close it after intiating the cursor
        """
        self.cursor.close()
        
    
    def _create_tables(self):
        """
        Creates tables if they don't exist int the database.
        Has four tables in the database.
        users, meal_consumed, food, and meal_items.
        """
        
        self.cursor.execute("""
                           CREATE TABLE IF NOT EXISTS users(
                               user_id INTEGER PRIMARY KEY, 
                               name TEXT)
                           """)
        self.cursor.execute("""
                           CREATE TABLE IF NOT EXISTS meal_consumed(
                               meal_id INTEGER PRIMARY KEY, 
                               user_id INTEGER, 
                               bgl_delta REAL, 
                               date TEXT, 
                               time_of_day TEXT,
                               FOREIGN KEY (user_id) REFERENCES users(user_id))
                           """)
        self.cursor.execute("""
                           CREATE TABLE IF NOT EXISTS food(
                               food_id INTEGER PRIMARY KEY,
                               food TEXT,
                               carbs REAL,
                               protein REAL,
                               fat REAL)
                           """)
        self.cursor.execute("""
                           CREATE TABLE IF NOT EXISTS meal_items(
                               meal_id INTEGER, 
                               food_id INTEGER, 
                               portion INTEGER DEFAULT 1,
                               PRIMARY KEY (meal_id, food_id),
                               FOREIGN KEY (meal_id) REFERENCES meal_consumed(meal_id),
                               FOREIGN KEY (food_id) REFERENCES food(food_id))
                           """)
    
    #select the file location for food
    def get_foods(self):
        pass

    #manually input foods which is a set    
    def get_foods(self, foods):
        pass
    
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
            Exception: _description_
        """
        if len(foods) <= 0:
            raise Exception("Set of foods can't be empty")
        pass
    
    #either use a library for this to do it automatically
    #or calculate manually?
    def calculate_correlation(self, food):
        pass
    
    #add a food to the database if it is not found
    def _db_add_food(self, food):
        pass
    
    #display the blood glucose as y axis with the time as the x axis.
    #shows whether your BGL is changing over a year, month, day, etc
    def display_avg_BGL(self):
        pass
    
    #use python pyplot (matplotlib)
    def display_graph(self):
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
    
    #logmeal api?
    #openai api?
    def _identify_food(picture):
        pass
    
    #update the all time average. Maybe include the date in the database avgerage. Could possibly display trend of BGL over time
    def _update_avg_BGL(self):
        pass
    
    def print_database(self):
        pass
    