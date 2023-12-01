from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")

    def verify_search_result(self, product):
        search_results_header = self.find_element(*self.SEARCH_RESULT_TXT).text
        assert product in search_results_header, \
            f'Expected text {product} not in {search_results_header}'

    def verify_search_url(self, expected_keyword):
        assert expected_keyword in self.driver.current_url, \
            f'Expected {expected_keyword} not in {self.driver.current_url}'

    def name_and_image_are_shown(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        all_products = self.find_elements(*self.LISTINGS)
        #print(all_products)
        for product in all_products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            print(title)
            assert title, 'Product title not shown'
            product.find_element(*self.PRODUCT_IMG)
