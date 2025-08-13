Feature: Protected Endpoint

  Scenario: Get current authenticated user
    Given I am logged in
    When I fetch current user data
    Then I receive user information
    And it includes a "username" field
