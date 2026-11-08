def test_valid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    assert page.url.endswith("/inventory.html")
    assert page.locator(".title").inner_text() == "Products"
