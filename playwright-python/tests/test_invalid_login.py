def test_invalid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("wrong_user")
    page.locator("#password").fill("wrong_password")

    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")

    assert error_message.is_visible()
    assert "Username and password do not match" in error_message.inner_text()
