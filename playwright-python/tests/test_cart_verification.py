
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_contains_added_product(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    page.locator(".inventory_item").first.wait_for()

    product_name = inventory_page.get_first_product_name()
    product_price = inventory_page.get_first_product_price()

    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)

    assert cart_page.get_product_name() == product_name
    assert cart_page.get_product_price() == product_price
