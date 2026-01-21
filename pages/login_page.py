from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def open(self, base_url: str):
        super().open(f"{base_url}{self.URL}")

    def login(self, username: str, password: str):
        self.type_text(*self.USERNAME, text=username)
        self.type_text(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_flash_message(self) -> str:
        return self.get_text(*self.FLASH)
