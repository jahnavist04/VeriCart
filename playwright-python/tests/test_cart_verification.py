def test_cart_contains_added_product(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Wait for products to load
    page.locator(".inventory_item").first.wait_for()

    # Capture first product details
    product_name = page.locator(".inventory_item_name").first.inner_text()
    product_price = page.locator(".inventory_item_price").first.inner_text()

    # Add product to cart
    page.locator(".inventory_item button").first.click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    # Select product specifically inside cart
    cart_product = page.locator(".cart_item .inventory_item_name")
    cart_price = page.locator(".cart_item .inventory_item_price")

    assert cart_product.inner_text() == product_name
    assert cart_price.inner_text() == product_price
