"""These functions intends to make easier the automation process"""

def navigate_to_google(self):
    self.driver.implicitly_wait(30)
    self.driver.get("www.google.com")

def google_search(self, word_to_search):
    self.driver.implicitly_wait(30)
    self.word_to_search = word_to_search




