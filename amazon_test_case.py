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
#Click Signin Button
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
# Amazon logo
driver.find_element(By.XPATH, "//i[contains(@class, 'a-icon-logo')]")
#Email field
driver.find_element(By.ID, 'ap_email')
#Continue button
driver.find_element(By.ID, 'continue')
#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")
#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")
#need help
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help')]")
#Forgot your password link
driver.find_element(By.XPATH,"//a[contains(text(), 'Forgot your password?')]")
#Other issues with Sign-In link
driver.find_element(By.XPATH,"//a[contains(text(), 'Other issues with Sign-In')]")
#  Create your Amazon account button
driver.find_element(By.ID,"createAccountSubmit").click()

print('Test Passed')

driver.quit()
