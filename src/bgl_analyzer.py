# Copyright 2025, Zachary McKinney
#

import sqlite3


class BGL_Analyzer:

    #Initiate an Analyzer object with a dedicated user and uses the database associated with the user
    #User is a string ID, and DB is a filename to a Sqlite file or new file
    def __init__(self, user, db):
        _user = user
        _db_connection = sqlite3.connection(db)
        _db_cursor = _db_connection.cursor()
        
    
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
    