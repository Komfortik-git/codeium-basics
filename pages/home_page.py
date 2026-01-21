from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SECURE_HEADER = (By.CSS_SELECTOR, "div.example h2")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button")

    def get_header(self) -> str:
        return self.get_text(*self.SECURE_HEADER).strip()

    def logout(self):
        self.click(*self.LOGOUT_BUTTON)
