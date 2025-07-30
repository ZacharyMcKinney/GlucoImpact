import unittest
import src.food_id as fid
import hashlib
from PIL import Image
import logging
log = logging.getLogger("test_food_id")

# --- TODO LIST ---
# Test a "None" picture that is unidentifiable 
# Test OpenAI output for correct formatting
# Test OpenAI indentifcation of images

class TestFoodID(unittest.TestCase):

    def setUp(self):
        self.img1 = "./images/single_foods/apple.jpg"
        self.img2 = "./images/single_foods/bagels.jpg"
        self.img3 = "./images/single_foods/yogurt.jpg"
        self.img4 = "./images/single_foods/mashed_potatoes.jpg"
        self.img5 = "./images/multiple_foods/bibimbap.jpg"
        self.img6 = "./images/multiple_foods/salmon_dinner.jpg"
        self.img7 = "./images/multiple_foods/yogurt_parfait.webp"
        self.img9 = "./images/multiple_foods/turkey_sandwich.jpg"
        # false_path = "./images/multiple_foods/fake.jg"
        self.unsupported_path = "./tests/test_assets/gif_image.gif"

    # def test_get_img_location(self):
    #     pass
    
    def test_get_img_pass(self):
        expected_hash = self.image_hash(Image.open(self.img1))
        result_hash = self.image_hash(fid.get_img(self.img1))
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
        self.assertEqual("PNG", fid.convert_img(fid.get_img(self.img1)).format)
        self.assertEqual("JPEG", fid.convert_img(fid.get_img(self.img1), "JPEG").format)
        self.assertEqual("WEBP", fid.convert_img(fid.get_img(self.img1), "WEBP").format)
    
    def test_convert_pil_to_base64(self):
        AVG_PIX_DIF = 5
        MAX_PERCENTILE_DIF = 30
        
        imgs = [self.img1, self.img6, self.img7]
        for img in imgs:
            log.info(f"Test img {img} being converted")
            avg_diff, percentile_diff = self.b64_avg_and_percentile_diff(img)
            self.assertLessEqual(avg_diff, AVG_PIX_DIF)
            self.assertLessEqual(percentile_diff, MAX_PERCENTILE_DIF)
            log.info(f"Passed avg and percentile test for {img}")

    @staticmethod
    def b64_avg_and_percentile_diff(img) -> tuple:
        import base64
        import numpy as np
        from io import BytesIO
        
        ACCEPTABLE_PERCENTILE = 99.5

        expected_img_rgb = Image.open(img).convert("RGB")
        test_uri_str = fid.convert_pil_to_base64(fid.get_img(img))
        test_b64_encoding = test_uri_str.partition(",")[2]
        test_img_rgb = Image.open(BytesIO(base64.b64decode(test_b64_encoding))).convert("RGB")

        expected_pixel_arr = np.array(expected_img_rgb, dtype=np.int16)
        test_pixel_arr = np.array(test_img_rgb, dtype=np.int16)
        pixel_diffs = np.abs(expected_pixel_arr - test_pixel_arr)

        avg_diff = np.average(pixel_diffs)
        percentile_diff = np.percentile(pixel_diffs, ACCEPTABLE_PERCENTILE)
        return avg_diff, percentile_diff

    def test_identify_food(self):
        pass

    def test_identify_foods_data(self):
        pass

    # def test_load_openai_prompts(self) :
    #     pass

    @staticmethod
    def image_hash(img: Image.Image):
        return hashlib.md5(img.tobytes()).hexdigest()
    
    @staticmethod
    def get_text(file_loc: str):
        with open(file_loc, 'r') as file:
            text = file.read()
        return text

if __name__ == "__main__":
    unittest.main()