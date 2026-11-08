def test_successful_checkout(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add product to cart
    page.locator(".inventory_item button").first.click()

    # Open cart and checkout
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    # Enter customer information
    page.locator("#first-name").fill("Jahnavi")
    page.locator("#last-name").fill("ST")
    page.locator("#postal-code").fill("560001")

    page.locator("#continue").click()

    # Finish order
    page.locator("#finish").click()

    # Verify order confirmation
    confirmation = page.locator(".complete-header")
    confirmation.wait_for(state="visible", timeout=10000)

    assert confirmation.inner_text() == "Thank you for your order!"
