# InsulinApp

This project allows a user to take a picture of their food and associate those foods with an increase in BGL. 

## Features
- Helps a user know if a food could cause a blood glucose spike
- Uses SQLite to store data locally
- OpenAI for image identification
- Python for easier data visualization


## Usage


## Data Structure

**Database schema includes:**
- `users`: user_id, name
- `food`: food_id, name, carbs, protein, fat
- `meal_consumed`: meal_id, user_id, bgl_delta, date, time_of_day
- `meal_items`: meal_id, food_id, portion

## Requirements
- Python 3.7+
- `matplotlib`
- `numpy`
- `pandas`

## Future Prospects
- Creating downloadable app for the store (main goal afterwards)
- Replace SQLite with a cloud-based storage
- Implementing a GUI for program (if there's no app)

## Author
- Zachary McKinney
- Github: https://github.com/ZacharyMcKinney
- Email me at zachary.mckinney04@gmail.com

