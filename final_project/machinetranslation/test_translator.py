from ibm_cloud_sdk_core import ApiException

from machinetranslation.translator import english_to_french, french_to_english
import unittest

class test_french_translation(unittest.TestCase):
    def test_french_to_english_assertNotEqual(self):
        self.assertNotEqual(french_to_english("Bonjour"), "")

    def test_french_to_english_assertEqual(self):
        self.assertEqual(french_to_english("Bonjour"), {'character_count': 7,
                            'translations': [{'translation': 'Hello'}],
                            'word_count': 1})

class test_english_translation(unittest.TestCase):
    def test_english_to_french_assertNotEqual(self):
        self.assertNotEqual(english_to_french("Hello"), "")

    def test_english_to_french_assertEqual(self):
        self.assertEqual(english_to_french("Hello"), {'character_count': 5,
                            'translations': [{'translation': 'Bonjour'}],
                            'word_count': 1})

if __name__ == "__main__":
    unittest.main()