
class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.confirmation_message = page.locator(".complete-header")

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        return self.confirmation_message.inner_text()
