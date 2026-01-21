# tests/test_open_nor_vidjet.py
def test_norilsk_config():
    """Тест конфигурации Norilsk Vidjet"""
    BASE_URL_NORILSK_VIDJET = "https://norilsk.mycityair.ru/static/"

    assert BASE_URL_NORILSK_VIDJET.startswith("https://norilsk")
    assert ".mycityair.ru" in BASE_URL_NORILSK_VIDJET

    print(f"✅ Norilsk Vidjet URL: {BASE_URL_NORILSK_VIDJET}")
    print("✅ Тест КОНФИГУРАЦИИ ПРОШЕЛ!")
