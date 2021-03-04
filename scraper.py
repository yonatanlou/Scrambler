from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pickle


class Scraper:
    FILENAME = "cookies.pkl"

    def __init__(self, target_site):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.search = None
        self.set_target_site(target_site)

    def set_target_site(self, address):
        self.driver.get(address)
        self.search = self.driver.find_element_by_name("q")
        self.search.clear()

    def search_by_keyword(self, keyword):
        self.search.send_keys(keyword)
        self.search.submit()

    def search_keywords(self, keywords):
        for keyword in keywords:
            self.search_by_keyword(keyword)
            self.save_cookies()
        # todo - save cookies in loop or outside?

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open(Scraper.FILENAME, "wb"))

    def load_cookies(self):
        cookies = pickle.load(open(Scraper.FILENAME, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        return self.driver.get_cookies()

    def get_cookies(self):
        return self.driver.get_cookies()
