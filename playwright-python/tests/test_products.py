def test_products_are_displayed(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    products = page.locator(".inventory_item")

    assert products.count() > 0
    assert page.locator(".inventory_item_name").first.is_visible()
    assert page.locator(".inventory_item_price").first.is_visible()
