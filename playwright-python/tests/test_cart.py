def test_add_product_to_cart(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add the first product to cart
    page.locator(".inventory_item button").first.click()

    # Verify cart badge
    cart_badge = page.locator(".shopping_cart_badge")

    assert cart_badge.is_visible()
    assert cart_badge.inner_text() == "1"
