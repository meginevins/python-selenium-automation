# Created by me361 at 12/1/2023
Feature: tests for target cart page
  # Enter feature description here

  Scenario: “Your cart is empty” message is shown for empty cart
    Given open target main page
    When click cart icon
    Then Verify "Your cart is empty” message is shown


