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
- Streamline the process of logging food

## Usage
1. **Start the program** by running 'main.py'.
   - Sign in as user1 to get an account preloaded with food data
2. **Enter in a food entry** with two options. Then add the BGL delta.
   - Option 1: Manually enter in food.
   - Option 2: Select a photo. An OpenAI API key will need to be set in Food_ID
3. **Look at food Impact** with two options.
   - Option 1: Look up a single food and analyze its BGL impact
   - Option 2: Look at all the foods on a single graph
4. **Remove food entries if needed**
#### The app will:
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
- `openai`
- `pandas`
- `pillow`
- `PyQt6`
- `python-dotenv`

## To Do
- Polish PyQt6 interface
- Background and styling
- Interface asks for API key or has option (no need to enter into code manually)
- Scroll bar for food entry lists
- Autofill and search for foods
- Documentation for most functions and function hints
- Remove Magic numbers and magic list indexing (enum needed) in GUI
- Reduce GUI bloat and improve organization
- Separate usage between bgl_analzyer and db_manager
- Food filter (no blank spaces. capitlize food in gui)

## Future Prospects
- Replace SQLite with a cloud-based storage
- Secure way of logging in
- Connect to CGM devices so users don't manually enter in BGL delta
- Creating downloadable app for the store

## Author
- Zachary McKinney
- Github: https://github.com/ZacharyMcKinney
- Email me at zachary.mckinney04@gmail.com

