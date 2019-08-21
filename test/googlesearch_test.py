from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import re

class Testing_search_google_correction(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("../driver/chromedriver")
        cls.driver.maximize_window()

    def test_1_google_search_verification(self):
        driver = self.driver
        "en funcion searchboxfill"
        searchbox = driver.find_element_by_name("q")
        searchbox.click()
        searchbox.clear()
        searchbox.send_keys("pruebaz")
        searchbox.send_keys(Keys.RETURN)
        "function searchcorrection"
        correctsearch = driver.find_element_by_id("fprsl")
        correctsearch.click()

        "function verify results number"
        resultslabel = driver.find_element_by_id("resultStats").text
        resultsgroup = re.search(r"(\d|,)+", resultslabel)
        finalresult = int(str(resultsgroup.group()).replace(",", ""))
        assert 6 < finalresult
        print(resultslabel)
        print(resultsgroup.group())


    @classmethod
    def tearDown(cls):
        cls.driver.quit()