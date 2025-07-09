## Copyright 2025, Zachary McKinney

import tkinter as tk
# from tkinter import filedialog
from dotenv import load_dotenv
from PIL import Image
import os
import openai
import base64
from io import BytesIO
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
_IMG_FORMATS = {"jpeg", "jpg", "png", "webp"}
_OPENAI_PROMPT_FILE = "./prompts/openai_prompt1.txt"


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
    img_location = tk.filedialog.askopenfilename(
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
    with open(_OPENAI_PROMPT_FILE, 'r') as prompt:
        request = prompt.read()
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