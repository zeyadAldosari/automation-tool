Feature: Auth

  Scenario: Login succeeds
    Given I have valid credentials
    When I login
    Then I receive an access token

  Scenario: Login fails with invalid credentials
    Given I have invalid credentials
    When I login
    Then I see an authentication error
