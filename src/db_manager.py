## Copyright 2025, Zachary McKinney

import sqlite3

class DB_Manager:
# --- Class tools and Initiation ---
       
    def __init__(self, database_name: str = "./databases/default.db"):
        self._connection = sqlite3.connect(database_name)
        self._cursor = self._connection.cursor()
        self.create_tables()
    
    def close_cursor(self) -> None:
        self._cursor.close()
    
    def create_tables(self) -> None:    
        self._cursor.execute("""
                           CREATE TABLE IF NOT EXISTS users(
                               user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                               user_name TEXT UNIQUE)
                           """)
        self._cursor.execute("""
                           CREATE TABLE IF NOT EXISTS food_entry(
                               entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id INTEGER,
                               food_id INTEGER, 
                               bgl_delta INTEGER)
                           """)
        self._cursor.execute("""
                           CREATE TABLE IF NOT EXISTS food(
                               food_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               food TEXT UNIQUE)
                           """)
        self._connection.commit()
        
# --- Add / Insert Functions ---

    def add_user(self, user_name: str) -> None:
        self._cursor.execute("INSERT INTO users (user_name) VALUES(?)", (user_name,))
        self._connection.commit()
        
    def add_food(self, food: str) -> None:
        self._cursor.execute("INSERT INTO food (food) VALUES(?)", (food,))
        self._connection.commit()
        
    def add_food_entry(self, user_id: int, food_id: int, bgl_delta: int):
        self._cursor.execute("INSERT INTO food_entry (user_id, food_id, bgl_delta) VALUES(?, ?, ?)", (user_id, food_id, bgl_delta))
        self._connection.commit()
        
# --- Read Functions --- 

    def get_user_by_id(self, user_id: int):
        self._cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return self._cursor.fetchone()

    def get_user_by_name(self, user_name: str):
        self._cursor.execute("SELECT * FROM users WHERE user_name = ?", (user_name,))
        return self._cursor.fetchone()

    def get_food_by_id(self, food_id: int):
        self._cursor.execute("SELECT * FROM food WHERE food_id = ?", (food_id,))
        return self._cursor.fetchone()

    def get_food_by_name(self, food: str):
        self._cursor.execute("SELECT * FROM food WHERE food = ?", (food,))
        return self._cursor.fetchone()

    def get_food_entry_by_id(self, entry_id: int):
        self._cursor.execute("SELECT * FROM food_entry WHERE entry_id = ?", (entry_id,))
        return self._cursor.fetchone()

    def get_entries_by_user_and_food(self, user_id:int, food_id: int):
        self._cursor.execute("SELECT * FROM food_entry WHERE user_id =? AND food_id = ?", (user_id, food_id,))
        return self._cursor.fetchall()

    def get_entries_by_user(self, user_id: int):
        self._cursor.execute("SELECT * FROM food_entry WHERE user_id = ?", (user_id,))
        return self._cursor.fetchall()
    
    def get_unique_foods_by_user(self, user_id: int):
        self._cursor.execute("""
                             SELECT DISTINCT food.food 
                             FROM food_entry 
                             JOIN food ON food_entry.food_id = food.food_id
                             WHERE user_id = ?""", (user_id,))
        return self._cursor.fetchall()
    
# --- Update Functions ---

    def update_user(self, user_id: int, user_name: str):
        self._cursor.execute("UPDATE users SET user_name = ? WHERE user_id = ?", (user_name, user_id))
        self._connection.commit()

    def update_food(self, food_id: int, food_name: str) -> None:
        self._cursor.execute("UPDATE food SET food_name = ? WHERE food_id = ?", (food_name, food_id))
        self._connection.commit()

    def update_food_entry(self, entry_id, user_id, food_id, bgl_delta) -> None:
        self._cursor.execute("UPDATE users SET user_id = ?, food_id = ?, bgl_delta = ? WHERE entry_id = ?", (user_id, food_id, bgl_delta, entry_id))
        self._connection.commit()

# --- Delete Functions ---

    def delete_user(self, user_id: int):
        self._cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        self._connection.commit()
    
    def delete_food(self, food_id: int):
        self._cursor.execute("DELETE FROM food WHERE food_id = ?", (food_id,))
        self._connection.commit()

    def delete_food_entry(self, entry_id: int):
        self._cursor.execute("DELETE FROM food_entry WHERE entry_id = ?", (entry_id,))
        self._connection.commit()
    