from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, by, value, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def find_clickable(self, by, value, timeout=None):
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.element_to_be_clickable((by, value)))

    def click(self, by, value):
        elem = self.find_clickable(by, value)
        elem.click()

    def type_text(self, by, value, text):
        elem = self.find_element(by, value)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, by, value):
        try:
            return self.find_element(by, value).text
        except TimeoutException:
            return ""
