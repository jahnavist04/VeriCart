
from pages.login_page import LoginPage


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.get_error_message()
