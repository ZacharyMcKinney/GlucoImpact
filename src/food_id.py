## Copyright 2025, Zachary McKinney

import os
import base64
from io import BytesIO
from collections import namedtuple

from dotenv import load_dotenv
from PIL import Image
import openai
import tkinter as tk

# --- SETUP ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise openai.APIConnectionError("Was not able to load OpenAI API key. Value is None or blank")

# --- Constant and Defintions ---
_IMG_FORMATS = {"jpeg", "jpg", "png", "webp"}
_CONVERSION_FORMATS = {"PNG", "JPEG", "WEBP"}
OpenAI_Prompts = namedtuple('Prompts', ['system', 'assistant', 'user'])

# --- GET IMAGE ---
    
def get_img_location() -> str:
    """
    Prompts the user to select a photo of their food

    Returns:
        str: Picture file location that's selected
    """
    root = tk.Tk()
    root.withdraw()
    img_location = tk.filedialog.askopenfilename(
        title="Select a food photo",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *webp")]
    )
    return img_location

def get_img(file_location: str) -> Image:
    """
    Returns a Pillow Image if it's found and able to be loaded in
    
    Args:
        file_location (string): Path to any of the acceptable image file types
        
    Raises:
        FileNotFoundError: File doesn't exist
        UnidentifiedImageError: Image format isn't able to be loaded by Pillow
        
    Returns:
        Image: A Pillow Image from the file_location
    """
    try:
        return Image.open(file_location)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file location {file_location} was not able to be opened")
    except Image.UnidentifiedImageError:
        raise Image.UnidentifiedImageError(f"File in {file_location} isn't a supported type: {os.path.splitext(file_location)[1]}")

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

    Raises:
        TypeError: If the format is not in the supported conversion formats

    Returns:
        Image: Returns a new Pillow Image of the type format
    """
    if format not in _IMG_FORMATS or format is "JPG":
        raise TypeError(f"Convert convert given Image to {format}. Supported formats are: {_CONVERSION_FORMATS}")
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

def identify_food(file_location: str) -> str:
    """
    Takes a file_location gets an img and verifies that it is in acceptable format.
    Then the img is sent the OpenAI API. It returns the meal including the foods
    and macro nutrients in the foods.

    Args:
        file_location (str): Takes a file_location string that is read into a Pillow Image

    Returns:
        str: Text formatted with meals and food_items. Formatted like in the assistant files.
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
    """
    Takes three files locations for system, assistant, and user paths.
    The files are read and returned as a named tuple with each variable.
    Private function _read_file for reading each file

    Args:
        system_path (str, optional): Text file to system prompt. Defaults to "./prompts/openai_system1.txt".
        assistant_path (str, optional): Text file to assistant prompt. Defaults to "./prompts/openai_assistant1.txt".
        user_path (str, optional): Text file to user prompt. Defaults to "./prompts/openai_user1.txt".

    Returns:
        namedtuple: Tuple named Prompts with system, assistant, and user values.
    """
    
    def _read_file(path: str) -> str:
        with open(path, 'r') as prompt:
            return prompt.read()
        
    return OpenAI_Prompts(_read_file(system_path), _read_file(assistant_path), _read_file(user_path))
