Feature: search Feature

  Scenario Outline: Validating the search feature - happy path
    Given I navigate to SDAIA homepage
    When I click on search icon
    And I enter the search term "<search term>"
    And I click on the search button
    Then I validate search results

  Scenario: Validating the search feature - empty search field
    Given I navigate to SDAIA homepage
    When I click on search icon
    And I click on the search button
    Then I should not be able to search

  Scenario: Validating the search feature - keyboard smash
    Given I navigate to SDAIA homepage
    When I click on search icon
    And I enter a random search term
    And I click on the search button
    Then I should not get any results


  Scenario: Validating the search feature - suggestions
    Given I navigate to SDAIA homepage
    When I click on search icon
    And I enter a select a suggested search term
    Then I validate search results

  Scenario Outline: Validating the search feature - over characters limit
    Given I navigate to SDAIA homepage
    When I click on search icon
    And I enter an "<length>" characters long search term
    And I click on the search button
    Then I validate error page
