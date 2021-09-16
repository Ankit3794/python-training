Feature: Google Search

  Scenario: Validate Google search
    Given User is on Google home page
    When user enters "Selenium with Python" as search string
    And submit the form
    Then validate search
    Then close browser