from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_cart_page = CartPage(driver)
