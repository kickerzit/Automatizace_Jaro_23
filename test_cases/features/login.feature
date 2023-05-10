@allure.feature
Feature: Login

Scenario: OK Login
Given I am on the Login Page
When I enter correct username and password
And I click on Login button
Then I see that I am logged in

Scenario: Non OK Login
Given I am on the Login Page
When I enter incorrect username and password
And I click on Login button
Then I see that I am not logged in