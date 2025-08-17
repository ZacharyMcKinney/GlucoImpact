# GlucoImpact

This project allows a user to take a picture of their food and associate those foods with an increase in Blood Glucose Levels (BGL). 
Users can understand how a particular food may affect them, and if they should avoid it.
The purpose is streamline the process for monitoring how a food affects a person's BGL.

## Features
- Helps a user know if a food could cause a blood glucose spike
- SQLite to store data locally
- OpenAI for image identification
- Python for easier data visualization
- Data visualization to display how foods may spike BGL
- Track BGL deltas for each food item or meal

## Usage
1. **Start the program** by running 'main.py'.
2. **Enter in a food entry** with two options. Then add the BGL delta.
   - Select a photo. An OpenAI API key will need to be set in Food_ID
   - Manually enter in food.
3. **Input BGL data** with spreadsheet data of BGL and time.
4. The app will:
   - Store the food and BGL delta in a local SQLite database 
   - Graph a food and it's BGL data
   - Graph all foods and their averages 


## Data Structure

**Database schema includes:**
- `users`: user_id, user_name
- `food`: food_id, food_name
- `food_entry`: entry_id, user_id, food_id, bgl_delta

## Requirements
- `Python 3.10+`
- `matplotlib`
- `numpy`
- `openai`
- `pandas`
- `pillow`
- `PyQt6`
- `python-dotenv`

## Future Prospects
- Creating downloadable app for the store (main goal afterwards)
- Replace SQLite with a cloud-based storage
- Secure way of logging in
- Connect to CGM devices so users don't manually enter in BGL delta

## Author
- Zachary McKinney
- Github: https://github.com/ZacharyMcKinney
- Email me at zachary.mckinney04@gmail.com

