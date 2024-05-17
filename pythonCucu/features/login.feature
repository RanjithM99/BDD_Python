Feature: Login Functionality


  Scenario: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address and valid password into the fields
    And I click on Login button
    Then I should get logged in

  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password into the fields
    And I click on Login button
    Then I should get a proper warning message


  Scenario: Login with valid email and invalid password
    Given I navigated to Login Page
    When I enter valid email and invalid password into the fields
    And I click on Login button
    Then I should get a proper warning message

  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email and invalid password
    And I click on Login button
    Then I should get a proper warning message

  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anyting into the fields
    And I click on Login button
    Then I should get a proper warning message



