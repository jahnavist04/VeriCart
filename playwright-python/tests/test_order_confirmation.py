
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout(page):
    # Login
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.open_cart()

    # Checkout
    cart_page = CartPage(page)
    cart_page.checkout()

    # Enter customer information
    checkout_page = CheckoutPage(page)
    checkout_page.enter_customer_details(
        "Jahnavi", "ST", "560001"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    # Verify order confirmation
    checkout_page.confirmation_message.wait_for(
        state="visible", timeout=10000
    )

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"
