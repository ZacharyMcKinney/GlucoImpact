## Copyright 2025, Zachary McKinney

import db_manager as DB
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

        self.db_manager = DB(database_name)
        self._user = user
    
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
