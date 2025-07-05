## Copyright 2025, Zachary McKinney

import tkinter as tk
from tkinter import filedialog
import os
import openai
from dotenv import load_dotenv

class Food_ID:
    
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # if not api_key:
        #     raise ValueError("OPENAI_API_KEY is not set in environment variables")
    
# --- GET PICTURE ---
    
    def get_picture(self):
        """
        Prompts the user to select a photo of their food

        Returns:
            jpg, jpeg, png, bmp, webp: Picture file that's selected
        """
        root = tk.Tk()
        root.withdraw()
        picture = filedialog.askopenfilename(
            title="Select a food photo",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *webp")]
        )
        return picture


    #mainly for testing, but file location
    def get_picture(self, file_location: str):
        """_summary_

        Args:
            file_location (string): Path to any of the acceptable image file types
        """
        # if not os.path.exist(file_location):
        #     raise FileNotFoundError("Location {file_location} was not found")
        pass
    
# --- OPENAI IDENTIFICATION ---    

    def _identify_food(picture):
        # system_command = ""
        # assistant_command = ""
        request = """
            Identify the foods in this picture. If this is a typical meal food,
            put the common meal name
            """
        chat_completion = openai.ChatCompletions.create(
            model="gpt-4o",
            messages=[
                    # {"role": "system", "content": system_command},
                    # {"role": "assistant", "content": assistant_command},
                    {"role": "user", "content": [
                        {"type": "text", "text": request},
                        {
                            "type": "image_url", 
                            "image_url": {"url": picture}
                        }
                    ]}
            ],
            max_tokens = 300,
            temperature = 0
        )

        return chat_completion.choices[0].message.content