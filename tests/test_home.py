import json
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.home_page import HomePage

def load_credentials(): # Здесь обращается к файлу в котором лежит логины и пароли
    with open("data/test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def test_home_after_login(driver):
    creds = load_credentials()["valid_user"]
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(creds["username"], creds["password"])

    home = HomePage(driver)
    assert "Secure Area" == home.get_header()
    home.logout()
    assert "You logged out of the secure area!" in login.get_flash_message()
