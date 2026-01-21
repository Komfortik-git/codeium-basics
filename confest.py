# conftest.py (в корне проекта!)
import sys
from pathlib import Path
import pytest
import os

# ✅ ПРАВИЛЬНЫЙ путь к корню проекта
project_root = Path(__file__).parent.resolve()  # /workspaces/codeium-basics
sys.path.insert(0, str(project_root))

from utils.driver_setup import create_driver

@pytest.fixture(scope="function")
def driver():
    headless = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
    driver = create_driver(headless=headless)
    driver.maximize_window()
    yield driver
    try:
        driver.quit()
    except:
        pass
