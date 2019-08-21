Feature: Google Search

  Scenario Outline: Correct the incorrect google search
    Given Search in google
    When I search the word "<wrongword>"
    And I click on correct word suggestion "<correctword>"
    Then I should see more than "<n>" results
    Examples:
      | wrongword | correctword | n |
      | pruebaz   | pruebas     | 6 |
