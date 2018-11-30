
import unittest
import api

class TestApi(unittest.TestCase):

    def test_api_is_valid_date(self):
        self.assertTrue(api.is_valid_date("2018-11-28"))

    def test_api_is_valid_date_1(self):
        self.assertFalse(api.is_valid_date("2018-28"))

    def test_api_is_behavior(self):
        self.assertFalse(api.is_behavior("texto"))

    def test_api_is_behavior_1(self):
        self.assertTrue(api.is_behavior("text"))
