## Copyright 2025, Zachary McKinney

class Food_ID:
    
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
    def get_picture(self, file_location):
        """_summary_

        Args:
            file_location (string): Path to any of the acceptable image file types
        """
        # if not os.path.exist(file_location):
        #     raise FileNotFoundError("Location {file_location} was not found")
        pass
    
    #logmeal api?
    #openai api?
    def _identify_food(picture):
        pass