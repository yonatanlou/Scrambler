from scraper import Scraper
from surfers.googleSurfer import GoogleSurfer

COOKIE_FILE = "cookies.pkl"


if __name__ == '__main__':

    # suppuse to be the topics that the scraper should generate
    topics = ["dress", "shoes", "berlin"]

    surfer = GoogleSurfer()
    scraper = Scraper(surfer.get_target_name())
    scraper.search_keywords(topics)
    cookies = scraper.load_cookies()

