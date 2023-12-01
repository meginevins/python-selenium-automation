from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given('open target main page')
def open_target_main_page(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('search for {product_name}')
def search_item(context, product_name):
    #context.driver.find_element(By.ID, 'search').send_keys(product_name)
    context.app.main_page.search(product_name)


@when('click search button')
def click_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="search"]').click()
    sleep(3)


@when('click on {product_name}')
def click_product(context, product_name):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "picture[data-test='@web/ProductCard/ProductCardImage/primary']").click()


@when('click shipping')
def click_shipping(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label*="shipping"]').click()


@when('click add to cart')
def click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "button[id*='addToCartButton']").click()
    sleep(10)


@when('click view cart and check out')
def click_view_cart_and_check_out(context):
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()


@when('click cart icon')
def click_cart_icon(context):
    context.app.target_cart_page.click_cart_icon()


@then('verify {product_name} is in the cart')
def verify_mug_in_cart(context, product_name):
    actual_product_name = context.driver.find_element(By.CSS_SELECTOR, '[data-test="cartItem-title"]').text
    assert product_name in actual_product_name, f'Expected {product_name}  in {actual_product_name} but not found'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.search_results_page.name_and_image_are_shown()

