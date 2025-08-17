## Copyright 2025, Zachary McKinney

from dataclasses import dataclass

@dataclass
class Food:
    food_id: int
    food: str
    
@dataclass
class Food_Entry:
    entry_id: int
    user_id: int
    food_id: int
    bgl_delta: int
    
@dataclass
class User:
    user_id: int
    name: str
    