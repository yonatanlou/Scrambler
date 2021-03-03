
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pickle

#suppuse to be the topics that the scraper should generate
topics = ["dress", "shoes", "berlin"]


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com")
search = driver.find_element_by_name("q")
search.clear()
search.send_keys(topics[0])
search.submit()

pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


