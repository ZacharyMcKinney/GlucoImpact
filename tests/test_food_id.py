import unittest
import src.food_id as fid
import hashlib
from PIL import Image

# --- TODO LIST ---
# Test a "None" picture that is unidentifiable 

class TestFoodID(unittest.TestCase):

    def setUp(self):
        img1 = "./images/single_foods/apple.jpg"
        img2 = "./images/single_foods/bagels.jpg"
        img3 = "./images/single_foods/yogurt.jpg"
        img4 = "./images/single_foods/mashed_potatoes.jpg"
        img5 = "./images/multiple_foods/bibimbap.jpg"
        img6 = "./images/multiple_foods/salmon_dinner.jpg"
        img7 = "./images/multiple_foods/yogurt_parfait.jpg"
        img9 = "./images/multiple_foods/turkey_sandwich.jpg"
        # false_path = "./images/multiple_foods/fake.jg"
        unsupported_path = "/test_assets/gif_image.gif"

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
    
    def test_is_supported_true(self):
        self.assertEqual(True, fid.is_supported(self.img1))
        self.assertEqual(True, fid.is_supported(self.img2))
        self.assertEqual(True, fid.is_supported(self.img3))
    
    def test_is_supported_false(self):
        self.assertEqual(False, fid.is_supported(fid.get_img(self.unsupported_path)))
    
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