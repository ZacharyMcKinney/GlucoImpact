import unittest
import src.food_id as fid
import hashlib
from PIL import Image

# --- TODO LIST ---
# Test a "None" picture that is unidentifiable 

class TestFoodID(unittest.TestCase):

    def setUp(self):
        img1_str = "./images/single_foods/apple.jpg"
        img1 = Image.open(img1_str)
        img2 = Image.open("./images/single_foods/bagels.jpg")
        img3 = Image.open("./images/single_foods/yogurt.jpg")
        img4 = Image.open("./images/single_foods/mashed_potatoes.jpg")
        img5 = Image.open("./images/multiple_foods/bibimbap.jpg")
        img6 = Image.open("./images/multiple_foods/salmon_dinner.jpg")
        img7 = Image.open("./images/multiple_foods/yogurt_parfait.jpg")
        img9 = Image.open("./images/multiple_foods/turkey_sandwich.jpg")

    # def test_get_img_location(self):
    #     pass
    
    def test_get_img_pass(self):
        expected_hash = self.image_hash(self.img1)
        result_hash = fid.get_img(self.img1_str)
        self.assertEqual(expected_hash, result_hash)
    
    def test_get_img_not_found(self):
        with self.assertRaises(FileNotFoundError):
            fid.get_img("fake_path")

    def test_get_img_unidentified(self):
        with self.assertRaises(Image.UnidentifiedImageError):
            fid.get_img("./requirements.txt")
    
    def test_is_supported(self):
        pass
    
    def test_convert_img(self):
        pass
    
    def test_convert_pil_to_base64(self):
        pass

    def test_identify_food(self):
        pass

    def test_identify_foods_data(self):
        pass

    def test_load_openai_prompts(self) :
        pass

    def image_hash(img: Image.Image):
        return hashlib.md5(img.tobytes()).hexdigest()

if __name__ == "__main__":
    unittest.main()