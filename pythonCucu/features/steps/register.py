from behave import *

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I navigate to Register Page')
def step_impl(context):
    context.driver =webdriver.Chrome()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.maximize_window()
    context.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH,
                                "//ul[contains(@class,'dropdown-menu dropdown-menu-right')]/li/a[contains(text(),'Register')]").click()
    time.sleep(5)


@when('I enter details into mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID,"input-firstname").send_keys("Rajini")
    context.driver.find_element(By.ID,"input-lastname").send_keys("kanth")
    context.driver.find_element(By.ID,"input-email").send_keys("ranjinikanth@gmail.com")
    context.driver.find_element(By.ID,"input-telephone").send_keys("9876543210")
    context.driver.find_element(By.ID,"input-password").send_keys("Rajini@00")
    context.driver.find_element(By.ID,"input-confirm").send_keys("Rajini@00")
    time.sleep(5)



@when("I select privacy policy option")
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "//input[@type='checkbox']").click()
    time.sleep(1000)


@when('I click on Continue')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Continue']").click()


@then('Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created"
    actual_output = context.driver.find_element(By.XPATH,"//div[@id='content']/h1").text()
    assert actual_output == expected_text


@when('I enter existing accounts email into email fieldsA')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Rajini")
    context.driver.find_element(By.ID, "input-lastname").send_keys("kanth")
    context.driver.find_element(By.ID, "input-email").send_keys("ranjinikanth@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
    context.driver.find_element(By.ID, "input-password").send_keys("Rajini@00")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Rajini@00")


@then('Proper warning message information about duplicate account should be displayed')
def step_impl(context):
    expected_output = "Warning: E-Mail Address is already registered"
    actual_output = context.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text()
    assert expected_output == actual_output


@when('I dont enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")



@then('Proper warning messages for every mandotary fields should be displayed')
def step_impl(context):
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning = "First Name must be between 1 and 32 characters!"
    expected_last_name_warning =  "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warnirng = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    actual_privacy_policy_warning = context.driver.find_element(By.XPATH,"//div[contains(@class,'alert alert-danger alert-dismissible')]").text()
    actual_first_name_warning = context.driver.find_element(By.XPATH,"(//div[contains(@class,'text-danger')])[1]").text()
    actual_last_name_warning = context.driver.find_element(By.XPATH,"(//div[contains(@class,'text-danger')])[2]").text()
    actual_email_warning = context.driver.find_element(By.XPATH,"(//div[contains(@class,'text-danger')])[3]").text()
    actual_telephone_warning = context.driver.find_element(By.XPATH,"(//div[contains(@class,'text-danger')])[4]").text()
    actual_password_warning = context.driver.find_element(By.XPATH,"(//div[contains(@class,'text-danger')])[5]").text()

    assert expected_privacy_policy_warning == actual_privacy_policy_warning
    assert expected_first_name_warning == actual_first_name_warning
    assert expected_last_name_warning == actual_last_name_warning
    assert expected_email_warning == actual_email_warning
    assert expected_telephone_warnirng == actual_telephone_warning
    assert expected_password_warning == actual_password_warning