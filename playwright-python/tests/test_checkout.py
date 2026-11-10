
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_required_fields(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(page)
    cart_page.checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.continue_checkout()

    assert checkout_page.error_message.is_visible()
    assert "First Name is required" in checkout_page.get_error_message()
