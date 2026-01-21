import json
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.home_page import HomePage

def load_credentials():
    with open("data/test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def test_login(driver):
    creds = load_credentials()["valid_user"]
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(creds["username"], creds["password"])

    flash = login.get_flash_message()
    assert "You logged into a secure area!" in flash

    home = HomePage(driver)
    assert "Secure Area" == home.get_header()
