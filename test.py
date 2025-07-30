import unittest
import logging

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger("food_id").setLevel(logging.DEBUG)
    logging.getLogger("test_food_id").setLevel(logging.DEBUG)
    
    unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.discover("tests")
    )