## Copyright 2025, Zachary McKinney

import os
import base64
from io import BytesIO
from collections import namedtuple

from dotenv import load_dotenv
from PIL import Image
import openai
import tkinter as tk
# from tkinter import filedialog

# --- SETUP ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Constant and Defintions ---
_IMG_FORMATS = {"jpeg", "jpg", "png", "webp"}
OpenAI_Prompts = namedtuple('Prompts', ['system', 'assistant', 'user'])

# --- TODO list ---
# TODO: Add in exception for incorret api key
# TODO: Add my API key into my environment variables
# TODO: Finish documentation for every function

# --- GET IMAGE ---
    
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

# --- IMAGE UTILITIES --- 

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
    openai_prompts: namedtuple = _load_openai_prompts()
    chat_completion = openai.ChatCompletions.create(
        model="gpt-4o",
        messages=[
                {"role": "system", "content": openai_prompts.system},
                {"role": "assistant", "content": openai_prompts.assistant},
                {"role": "user", "content": [
                    {"type": "text", "text": openai_prompts.user},
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
        
def _load_openai_prompts(
    system_path: str = "./prompts/openai_system1.txt",
    assistant_path: str = "./prompts/openai_assistant1.txt",
    user_path: str = "./prompts/openai_user1.txt" 
) -> namedtuple:
    """_summary_

    Args:
        system_path (str, optional): _description_. Defaults to "./prompts/openai_system1.txt".
        assistant_path (str, optional): _description_. Defaults to "./prompts/openai_assistant1.txt".
        user_path (str, optional): _description_. Defaults to "./prompts/openai_user1.txt".

    Returns:
        namedtuple: _description_
    """
    def _read_file(path: str) -> str:
        with open(path, 'r') as prompt:
            return prompt.read()
        
    return OpenAI_Prompts(_read_file(system_path), _read_file(assistant_path), _read_file(user_path))
