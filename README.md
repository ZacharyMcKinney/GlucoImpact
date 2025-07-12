# GlucoImpact

This project allows a user to take a picture of their food and associate those foods with an increase in Blood Glucose Levels (BGL). 
Users can understand how a particular food may affect them, and if they should avoid it.

## Features
- Helps a user know if a food could cause a blood glucose spike
- SQLite to store data locally
- OpenAI for image identification
- Python for easier data visualization
- Data visualization to display how foods may spike BGL
- Track BGL deltas for each food item or meal

## Usage
1. **Start the program** and select a user_id.
2. **Capture or upload a photo** of a meal using the file dialog, file_location, or with manual input.
3. **Input BGL data** with spreadsheet data of BGL and time.
4. The app will:
   - Identify foods in the image using OpenAI vision tools (optional)
   - Store the meal and BGL delta in a local SQLite database
   - Associate individual foods with BGL changes
5. Use built-in visualizations to analyze which foods may consistently correlate with high BGL spikes.


## Data Structure

**Database schema includes:**
- `users`: user_id, name
- `food`: food_id, name, carbs, protein, fat
- `meal_consumed`: meal_id, user_id, bgl_delta, date, time_of_day
- `meal_items`: meal_id, food_id, portion

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
- Implementing a GUI for program (if there's no app)

## Author
- Zachary McKinney
- Github: https://github.com/ZacharyMcKinney
- Email me at zachary.mckinney04@gmail.com

