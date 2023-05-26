Feature: Validate user is able to upload sample data

  Background: User logins into the application
    Given User is on url
    And I enter username and password
    And I click on login button
    And I should see Dashboard page

  Scenario: User is able to upload sample data
    Given I click on 'Upload Data' button
    When I click on 'Choose File' button
    And I click on 'Upload' button
    And I pause for "20" seconds
    Then I should see file uploaded successfully