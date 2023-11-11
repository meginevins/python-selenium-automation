from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(5)
# click hello sign-in
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
# click on creat your amazon account
driver.find_element(By.ID, "createAccountSubmit").click()
# amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')
# create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# click on your name
driver.find_element(By.ID, "ap_customer_name")
# mobile number or email
driver.find_element(By.ID, 'ap_email')
# password
driver.find_element(By.ID, 'ap_password')
# password check
driver.find_element(By.ID, 'ap_password_check')
# click on continue
driver.find_element(By.ID, 'continue')
# conditions of use
driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_condition_of_use"]')
# privacy notice
driver.find_element(By.CSS_SELECTOR, 'a[href*="ap_register_notification_privacy_notice"]')
# sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')


print('Test Passed')

driver.quit()

