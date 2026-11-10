
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")

    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"
