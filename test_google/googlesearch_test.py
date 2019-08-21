from selenium import webdriver
import unittest
from QA_Marble.core import googlesearch

class Testing_search_google_correction(unittest.TestCase):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Testing_search_google_correction()
        return cls.instance

    def setUp(self):
        self.driver = webdriver.Chrome("../driver/chromedriver")
        self.driver.maximize_window()

    def test_1_navigate_to_google(self):
        googlesearch.navigate_to_google(self)

    def test_2_google_search(self, word_to_search):
        self.word_to_search = word_to_search
        googlesearch.google_search(self.word_to_search)

    def test_3_google_correct_search(self):
        googlesearch.correct_search(self)

    def test_4_google_verify_results(self, number):
        self.number = number
        googlesearch.verify_results(self, self.number)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

testing_google = Testing_search_google_correction.get_instance()