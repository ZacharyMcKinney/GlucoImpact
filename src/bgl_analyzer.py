## Copyright 2025, Zachary McKinney

import db_manager as DB
import pandas as pd
from datetime import date
class BGL_Analyzer:


    def __init__(self, user: str, database_name: str):
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

# --- Database Related ---   

    #use lambda to make it easier to read and complete
    #set={}
    def add_food_bgl(self, foods, bgl_spike: float):
        """
        Enters in a bgl spike for set of foods given into the local database
        
        Args:
            foods (set of strings): Identified foods consumed at a bgl spike
            bgl_spike (int or float): Max bgl after food - avg bgl for the day

        Raises:
            Exception: Needs at least one food to be added
        """
        if len(foods) <= 0:
            raise Exception("Set of foods can't be empty")
        
# --- Calculations ---
        
    # def calculate_correlation(self, food_id: int, data) -> Type:
    def calculate_correlation(self, food_id: int):
        df = pd.DataFrame()
        X = df[]
        Y = df[]
        pass
