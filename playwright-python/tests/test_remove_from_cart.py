
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.remove_product("remove-sauce-labs-backpack")

    assert cart_page.get_cart_items_count() == 0
    assert page.locator(".shopping_cart_badge").count() == 0

