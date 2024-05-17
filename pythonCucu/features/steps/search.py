import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I got navigated to Home page')
def step_impl(context):
   context.driver = webdriver.Chrome()
   context.driver.maximize_window()
   context.driver.get("https://tutorialsninja.com/demo/")
   time.sleep(4)


@when('I enter valid product into the Search')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@type='text']").send_keys("HP")
    time.sleep(3)


@when('I click on Search button')
def step_impl(context):
        context.driver.find_element(By.XPATH,"//span[@class='input-group-btn']").click()


@then('Valid product should get displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()


@when('I enter invalid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("HONDA")
    time.sleep(3)


@then('Proper message should be displayed in Search results')
def step_impl(context):
    context.driver.find_element(By.XPATH)
    expected_Text = "Warning: No match for E-Mail Address and/or Password."
    output=context.driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')").text
    assert output == expected_Text



@when('I dont enter anything into Search box field')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(" ")
    time.sleep(3)

