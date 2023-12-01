from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class CartPage(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    CART_EMPTY_HEADER = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0")

    def click_cart_icon(self):
        sleep(5)
        self.click(*self.CART_ICON)

    def verify_cart_empty(self, message):
        sleep(5)
        actual_text = self.find_element(*self.CART_EMPTY_HEADER).text
        assert actual_text == message, f"Expected {message}, but got {actual_text}"
