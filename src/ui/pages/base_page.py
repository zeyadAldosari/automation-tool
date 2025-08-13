from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.utils.config import config as cfg
import random
import string

import logging

logger = logging.getLogger(__name__)


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver


    def click(self, locator, locator_provided):
        if locator_provided:
            self.wait.until(EC.presence_of_element_located((By.XPATH,cfg["locators"][locator]))).click()
        else:
            self.wait.until(EC.presence_of_element_located((By.XPATH,locator))).click()
        logger.info("clicking")


    def type(self, locator, value):
        field = self.wait.until(EC.presence_of_element_located((By.XPATH,cfg["locators"][locator])))
        field.send_keys(value)


    def get_browser_logs(self):
        return self.driver.get_log('browser')


    def generate_random_string(slef, length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string

    def validate_no_elements(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, cfg["locators"][locator])))
            return True
        except TimeoutException:
            return False

    def get_elements_list(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, cfg["locators"][locator])))

    def get_singular_and_plural(self, term):
        if term.endswith("s"):
            return [term, term[:-1]]
        else:
            return [term, term + "s"]