"""These functions intends to make easier the automation process"""
from selenium.webdriver.common.keys import Keys
import re


def navigate_to_google(self):
    self.driver.implicitly_wait(30)
    self.driver.get("www.google.com")

def google_search(self, word_to_search):
    self.driver.implicitly_wait(30)
    self.word_to_search = word_to_search
    searchbox = self.driver.find_element_by_name(self.search_bar)
    searchbox.click()
    searchbox.clear()
    searchbox.send_keys(word_to_search)
    searchbox.send_keys(Keys.RETURN)

def correct_search(self):
    "function search correction"
    correctsearch = self.driver.find_element_by_id("fprsl")
    correctsearch.click()

def verify_results(self, number_results):
    "function verify results number"
    resultslabel = self.driver.find_element_by_id("resultStats").text
    resultsgroup = re.search(r"(\d|,)+", resultslabel)
    finalresult = int(str(resultsgroup.group()).replace(",", ""))
    assert number_results < finalresult
    return True
