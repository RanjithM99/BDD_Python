from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def step_impl(context):
     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     context.driver.find_element_by_xpath(By.XPATH,"(//p[@class='oxd-text oxd-text--p'])[1]")


@when(u'Enter username "admin" and password "admin123"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Enter username "admin" and password "admin123"')


@when(u'Click on login button')
def step_impl(context):


 @when(u'Click on login button')
 def step_impl(context):
    raise NotImplementedError(u'STEP: When Click on login button')


@then(u'User must successfully login to the Dashboard Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must successfully login to the Dashboard Page')
