
class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.page_title = page.locator(".title")
        self.cart_link = page.locator(".shopping_cart_link")
        self.products = page.locator(".inventory_item")

    def get_page_title(self):
        return self.page_title.inner_text()

    def add_product_to_cart(self, product_id):
        self.page.locator(f"#{product_id}").click()

    def open_cart(self):
        self.cart_link.click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()

    def get_first_product_name(self):
        return self.page.locator(".inventory_item_name").first.inner_text()

    def get_first_product_price(self):
        return self.page.locator(".inventory_item_price").first.inner_text()
