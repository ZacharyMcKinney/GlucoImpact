import unittest
import src.food_id as fid
import hashlib

# --- TODO LIST ---
# Test a "None" picture that is unidentifiable 

class TestFoodID(unittest.TestCase):

    # def setUp(self):
    #     pass

    # def test_get_img_location(self):
    #     pass
    
    def test_get_img(self):
        pass
    
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

def _image_hash(img):
    return hashlib.md5(img.tobytes()).hexdigest()

if __name__ == "__main__":
    unittest.main()