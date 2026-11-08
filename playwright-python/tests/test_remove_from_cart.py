def test_remove_product_from_cart(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add first product
    page.locator(".inventory_item button").first.click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    # Remove product
    page.locator(".cart_item button").click()

    # Verify cart is empty
    assert page.locator(".cart_item").count() == 0
    assert page.locator(".shopping_cart_badge").count() == 0
