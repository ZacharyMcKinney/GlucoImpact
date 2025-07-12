from dataclasses import dataclass

@dataclass
class Food_Item:
    """Class for keeping track of a food's ID, name, and macros per serving"""
    food_id: int
    food: str
    carbs: float
    protein: float
    fat: float
    
@dataclass
class Meal:
    meal_id: int
    user_id: int
    food_items: list
    
@dataclass
class User:
    user_id: int
    name: str
    