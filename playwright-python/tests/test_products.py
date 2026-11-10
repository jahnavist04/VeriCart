
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_products_are_displayed(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)

    page.locator(".inventory_item").first.wait_for(state="visible")

    products = page.locator(".inventory_item")

    assert products.count() > 0
    assert page.locator(".inventory_item_name").first.is_visible()
    assert page.locator(".inventory_item_price").first.is_visible()
