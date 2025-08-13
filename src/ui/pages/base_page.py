from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url, timeout=15):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def go(self, path=""):        
        self.driver.get(self.base_url.rstrip("/") + "/" + path.lstrip("/"))

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
