# Created by me361 at 11/17/2023
Feature: test case for target main page

  Scenario: verify that product is added to cart
    Given open target main page
    When search for coffee
    And click search button
    And click on coffee
    And click add to cart
    And click view cart and check out
    Then verify Coffee is in the cart