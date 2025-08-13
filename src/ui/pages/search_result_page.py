from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def get_search_results(self):
        return self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//div[contains(@class,"ms-srch-item-summary")]')))


    def validate_search_results(self, results, term):
        search_words = term.split()
        if len(results) > 0:
            for result in results:
                expanded_search_words = []
                for word in search_words:
                    expanded_search_words.extend(self.get_singular_and_plural(word.lower()))

                if all(expanded_word.lower() not in result.text.lower() for expanded_word in expanded_search_words):
                    return False

            return True
        else:
            return False
        