@allure.feature
Feature: Products

Scenario: Check t-shirt description
Given I am logged in
When I click on t-shirt
Then I see the correct description
