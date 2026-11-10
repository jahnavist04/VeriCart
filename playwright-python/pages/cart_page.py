
class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def get_cart_items_count(self):
        return self.cart_items.count()

    def remove_product(self, product_id):
        self.page.locator(f"#{product_id}").click()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
