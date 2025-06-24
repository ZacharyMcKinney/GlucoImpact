## Copyright 2025, Zachary McKinney
import sqlite3


# Note to Self: Implement crud? create, retrieve, update, delete functions

#This class will be the only one allowed to access the database
#bgl_analyzer will put these functions together into one

class DB_Manager:
    
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
        
    #manually input foods which is a set    
    def add_foods(self, foods):
        for food in foods:
            self._db_add_food(food)
            
    #add a food to the database if it is not found
    def _db_add_food(self, food):
        self.cursor.execute("""
                            INSERT INTO food({food}, {carbs}, {protein}, {fat})
                            VALUES
                            """)
        pass