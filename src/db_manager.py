## Copyright 2025, Zachary McKinney
import sqlite3
from food_item import Food_Item
from datetime import date


# Note to Self: Implement crud? create, retrieve, update, delete functions

#This class will be the only one allowed to access the database
#bgl_analyzer will put these functions together into one

class DB_Manager:
    
# --- Class tools and Initiation ---
       
    def __init__(self, database_name: str):
        """_summary_

        Args:
            database_name (_type_): _description_
        """
        self.db_filename = database_name
        self._connection = sqlite3.connection(self.db_filename)
        self._cursor = self._connection.cursor()
        self._cursor.execute("PRAGMA foreign_keys = ON;")
        self.create_tables()
        self.cursor.commit()
    
    def close_cursor(self) -> None:
        """
        Closes database cursor connection.
        __Init__ doesn't close it after intiating the cursor
        """
        self.cursor.close()
    
    def create_tables(self) -> None:
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
        
# --- Add / Insert Functions ---

    def add_user(self, user_id: int) -> None:
        pass
        
    def add_food(self, food: int) -> None:
        """_summary_

        Args:
            food (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(food, Food_Item):
            raise TypeError("Food data must be of type Food_Item")
        self._db_add_food(food)
            
    def _db_add_food(self, food: Food_Item) -> None:
        self.cursor.execute("""
                            INSERT INTO food({food}, {carbs}, {protein}, {fat})
                            VALUES (?, ?, ?, ?)
                            """, (food.food, food.carbs, food.protein, food.fat))
        self._db_connection.commit()   
        
    def _add_meal_items(self) -> None:
        pass
    
    def add_meal(self) -> None:
        pass
    
    def add_meal_consumed(self, bgl_delta: int, time: date) -> None:
        pass
    
        
# --- Read Functions --- 

    # - FOOD -
    def get_food_by_id(self, food_id: int) -> Food_Item:
        pass

    def get_all_food(self) -> tuple[Food_Item]:
        pass

    def get_food_by_name(self, food: str) -> Food_Item:
        pass

    # - MEAL CONSUMED
    def get_meal_by_id(self, meal_id: int) -> Meal:
        pass

    def get_meal_by_name(self, meal_name: str) -> Meal:
        pass

    def get_all_meals(self) -> tuple[Meal]:
        pass



    #return the BGl for a food (only values, no dates) 
    def _get_food_BGL_data(self, food_id: int) -> float:
        pass

    #blood glucose for all time. For use if you can connect to
    #a glucose monitoring app or device
    def get_avg_alltime_BGL(self) -> float:
        pass
    
    #Blood glucose level for the day
    def get_avg_BGL(self) -> float:
        pass

# --- Update Functions ---

    def update_food(self, food_id: int) -> None:
        pass

    def update_meal(self, meal_id: int) -> None:
        pass

# --- Delete Functions ---

    def delete_food(self, food_id: int) -> Food_Item:
        pass

    def delete_meal(self, meal_id: int) -> Meal:
        pass

# --- Utilities ---       
        
    def link_food_to_meal(self, meal_id: int, food_id: int, portion: float = 1) -> None:
        pass
    

    