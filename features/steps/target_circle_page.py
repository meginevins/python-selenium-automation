from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_BOXES = (By.CSS_SELECTOR, 'li.styles__BenefitCard-sc-9mx6dj-2')

@given('open target circle page')
def open_target_page(context):
    context.driver.get('https://www.target.com/circle')
@then('verify 5 benefit boxes')
def verify_benefit_boxes(context):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == 5, f'expected 5 but got {len(benefit_boxes)}'

