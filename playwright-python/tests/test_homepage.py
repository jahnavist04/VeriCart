
from pages.login_page import LoginPage


def test_homepage_loads(page):
    login_page = LoginPage(page)
    login_page.open()

    assert page.title() == "Swag Labs"
