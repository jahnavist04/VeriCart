def test_checkout_required_fields(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add a product
    page.locator(".inventory_item button").first.click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    # Proceed to checkout
    page.locator("#checkout").click()

    # Continue without entering customer details
    page.locator("#continue").click()

    # Verify required field error
    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert "First Name is required" in error_message.inner_text()
