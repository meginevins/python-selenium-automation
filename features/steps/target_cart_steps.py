from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify "{message}” message is shown')
def cart_empty(context, message):
    context.app.target_cart_page.verify_cart_empty(message)
