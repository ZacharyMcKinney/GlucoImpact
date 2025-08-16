## Copyright 2025, Zachary McKinney

import db_manager as DB
import food_id as FID
import pandas as pd
class BGL_Analyzer:


    def __init__(self, user: str, database_loc: str):
        """
        Initiate an Analyzer object with a dedicated user and uses the database
        associated with the user
        User is a int ID, and DB is a filename to a Sqlite file or new file

        Args:
            user (str): user_name to be used in the database
            db (str): filename to Sqlite database
        """

        self.db_manager = DB(database_loc)
        if not self.db_manager.get_user_by_name(user):
            self.db_manager.add_user(user)
        self.user = user
        self.user_id = self.db_manager.get_user_name(self.user)[0]

    def add_bgl(self, food, bgl_delta: int):
        """
        Enters in a bgl spike for set of foods given into the local database
        
        Args:
            foods (set of strings): Identified foods consumed at a bgl spike
            bgl_spike (int): Max bgl after food - avg bgl for the day

        Raises:
            Exception: Needs at least one food to be added
        """
        if not self.db_manager.get_food_by_name(food):
            self.db_manager.add_food(food)
        food_id = self.db_manager.get_food_by_name(food)[0]
        self.db_manager.add_food_entry(self.user_id, food_id, bgl_delta)
        
    def add_bgl_picture(self, picture_location, bgl_delta: int):
        response = FID.identify_food(picture_location)
        for food in response[1:]:
            self.add_bgl(food, bgl_delta)

    def get_describe_bgl(self, food_id: int) -> dict:
        entries = self.db_manager.get_entries_by_user_and_food(self.user_id, food_id)
        bgl_deltas = []
        # {entry_id, user_id, food_id, bgl_delta}
        for entry in entries:
            bgl_deltas.append(entry[3])
        df = pd.DataFrame(bgl_deltas, columns=["bgl_delta"])
        return df.describe()
        