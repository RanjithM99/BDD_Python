import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

@given('I navigated to Login page')
def step_impl(context):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome()

    context.driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    context.driver.maximize_window()
    context.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//ul[contains(@class,'dropdown-menu dropdown-menu-right')]/li/a[contains(text(),'Login')]").click()
    time.sleep(5)


@when('I enter valid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-email").send_keys("95.ranjithkumar.m@gmail.com")
    context.driver.find_element(By.ID,"input-password").send_keys("Ranjith@00")
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()

@when('I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then('I should get logged in')
def step_impl(context):
     assert context.driver.find_element(By.XPATH,"//h2[contains(text(),'My Account')]").is_displayed()
     # context.driver.quit()


@when('I enter invalid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("abc@outlook.in")
    context.driver.find_element(By.ID, "input-password").send_keys("Ranjith@00")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then('I should get a proper warning message')
def step_impl(context):
    expected_result = "Warning: No match for E-Mail Address and/or Password."




@when('I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("95.ranjithkumar.m@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("1234567890")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@given('I navigate to Login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigate to Login page')


@when('I enter invalid email and invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("abc@outlook.in")
    context.driver.find_element(By.ID, "input-password").send_keys("1234567")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@when(u'I dont enter anyting into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys(" ")
    context.driver.find_element(By.ID, "input-password").send_keys(" ")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()

