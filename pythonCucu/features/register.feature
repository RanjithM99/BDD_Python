Feature: Register Account functionality

  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter details into mandatory fields
    When I select privacy policy option
    And I click on Continue
    Then Account should get created


  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter existing accounts email into email fieldsA
    When I select privacy policy option
    And I click on Continue
    Then Proper warning message information about duplicate account should be displayed


  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    When I select privacy policy option
    And I click on Continue
    Then Proper warning messages for every mandotary fields should be displayed


