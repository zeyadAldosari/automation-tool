from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import urllib.parse
import re


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 5)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.page_load()
        self.close_popup()

    def page_load(self):
        self.wait.until(
            lambda driverC: driverC.execute_script('return document.readyState') == 'complete')

    def close_popup(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "cookieApproveBtn")))
        approve_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "cookieApproveBtn")))
        if len(self.driver.find_elements(By.ID, "cookieApproveBtn")) > 0:
            approve_btn.click()


    def validate_search_error(self):
        logs = self.get_browser_logs()
        for entry in logs:
            if "PleaseEnterSearchTerm" in entry['message']:
                return True
        return False

    def select_suggestion(self):
        suggestions = self.get_elements_list("suggestions_XPATH")
        random_index = random.randint(0, len(suggestions) - 1)
        link = suggestions[random_index].get_attribute('href')

        encoded_search_term = (re.search(r'\?k=([^"]+)', link)).group(1)
        search_term = urllib.parse.unquote(encoded_search_term)
        self.click(
            f'//div[@class="overlayMenu"]/div//h4[text()="suggestions"]/../a[{random_index + 1}]', False)
        return search_term

    def validate_error_page(self):
        body = self.wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        if "The requested URL was rejected. Please consult with your administrator" in body.text:
            return True
        else:
            return False
