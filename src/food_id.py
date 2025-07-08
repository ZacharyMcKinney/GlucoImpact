## Copyright 2025, Zachary McKinney

import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv
from PIL import Image
import os
import openai
import base64
from io import BytesIO
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
_IMG_FORMATS = {"jpeg", "jpg", "png", "webp"}


# TODO: Add in exception for incorret api key
# TODO: Add my API key into my environment variables
# TODO: Move openai request into another text file where it's loaded in


# --- GET PICTURE ---
    
def get_img_location() -> str:
    """
    Prompts the user to select a photo of their food

    Returns:
        jpg, jpeg, png, bmp, webp: Picture file that's selected
    """
    root = tk.Tk()
    root.withdraw()
    img_location = filedialog.askopenfilename(
        title="Select a food photo",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *webp")]
    )
    return img_location

def get_img(file_location: str) -> Image:
    """_summary_

    Args:
        file_location (string): Path to any of the acceptable image file types
    """
    return Image.open(file_location)
    # if not os.path.exist(file_location):
    #     raise FileNotFoundError("Location {file_location} was not found")
    # return convert_picture(picture)

def is_supported(img: Image) -> bool:
    """
    Returns whether an image is supported
    Args:
        picture (Image): Image loaded by pillow
    Returns:
        bool: Whether or not image is a jpeg, jpg, png, or webp
    """
    return img.format not in _IMG_FORMATS

def convert_img(img: Image, format: str = "PNG") -> Image:
    """
    Converts a Pillow Image into a PNG or specified type.

    Args:
        img (Image): Image to be copied and converted to format
        format (str, optional): New Image format. Defaults to "png".

    Returns:
        Image: Returns a new Pillow Image of the type format
    """
    buffer = BytesIO()
    img.save(buffer, format=format)
    buffer.seek(0)
    new_img = Image.open(buffer)
    new_img.format = format
    return new_img

def convert_pil_to_base64(img: Image) -> str:
    """
    Converts a Pillow Image to a base64 string

    Args:
        img (Image): Pillow Image that's supported for the API

    Raises:
        TypeError: Image format isn't a jpg, jpeg, webp, or png

    Returns:
        str: Base64-encoded image usable for OpenAI API vision
    """
    if not is_supported(img):
        raise TypeError("Pillow image format is unsupported: {img.format}")
    
    buffer = BytesIO()
    img_format = img.format.upper()
    img.save(buffer, format=img_format)
    base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return f"data:image/{img_format.lower()};base64,{base64_str}"

# --- OPENAI IDENTIFICATION ---    

def identify_food(file_location: str):
    """
    Takes a file_location gets an img and verifies that it is in acceptable format.
    Then the img is sent the OpenAI API. It returns the meal including the foods
    and macro nutrients in the foods.

    Args:
        file_location (str): Takes a file_location string that is read into a Pillow Image

    Returns:
        str: _description_
    """
    img = get_img(file_location)
    if not is_supported(img):
        img = convert_img(img)
    b64_str = convert_pil_to_base64(img)
    request = """
        You are identifying foods present in an image for blood glucose tracking.

        Only include foods and drinks visually present. Do not infer extras.

        If multiple distinct meals or food groups appear, list each meal separately.

        The first output section:
        - First line is labeled "meals"
        - Each line corresponds to one meal.
        - Each line contains the common meal name followed by food items in that meal, all comma-separated.

        For example:
        meals
        Eggs and Toast, Scrambled Eggs, Toast
        Orange Juice, Orange Juice

        After listing all the meals, make one line that says "food_items"
        After that, list macronutrients per food item (carbs, protein, fats) as floats in grams, one food per line.
        
        For example:
        food_items
        Scrambled Eggs, 1.0, 12.0, 10.0
        Toast, 15.0, 3.0, 1.0
        Orange Juice, 25.0, 2.0, 0.0

        Avoid listing individual ingredients like sugar, or pepper, unless served separately.
        Include it in the meal and as an ingredient if it will have a major effect on the food.
        For example, include frosting in a frosted donut and as an ingredient. However, don't include it
        in a cake. Instead if a cake, which almost always has frosting, is plain, say that it is a plain cake.
        The main difference is that a donut is usually customized, while a cake is less customized.
        Therefore, the donut will have more variation (from frosting, custard, etc) in how it'll affect someone's blood glucose levels or diet.
        

        If nothing recognizable is present, output:
        None
        
        Completed Example:
        meals
        Eggs and Toast, Scrambled Eggs, Toast
        Orange Juice, Orange Juice
        food_items
        Scrambled Eggs, 1.0, 12.0, 10.0
        Toast, 15.0, 3.0, 1.0
        Orange Juice, 25.0, 2.0, 0.0
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
                        "image_url": {"url": b64_str}
                    }
                ]}
        ],
        max_tokens = 300,
        temperature = 0
    )
    return chat_completion.choices[0].message.content