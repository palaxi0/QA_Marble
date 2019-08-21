Feature: Google Search

  Scenario Outline: Correct the incorrect google search
    Given The word "<wrongword>"
    When I search that word in google
    And Google returns the word "<correctword>" as suggestion
    And I click on correct word "<correctword>"
    Then I should see more than "<n>" results
    Examples:
      | wrongword | correctword | n |
      | pruebaz   | pruebas     | 6 |
