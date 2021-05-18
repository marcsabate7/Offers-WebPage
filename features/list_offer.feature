Feature: List Offers
  In order to keep myself up to date about Offers registered in myOffers
  As a user
  I want to list the three registered Offers

  Background: There are four registered Offers by same user
    Given Exists a user "user" with password "password"
    And Exists an offer registered by "user"
      | Product name    | New Price   | Old Price   |
      | First           | 50          | 100         |
      | Second          | 60          | 120         |
      | Third           | 70          | 140         |

  Scenario: List the three
    When I list offers
    Then I'm viewing a list containing
      | Product name  |
      | Third         |
      | Second        |
      | First         |
    And The list contains 3 Offers

  Scenario: List the four
    Given Exists an offer registered by "user"
      | Product name    | New Price   | Old Price   |
      | Fourth          | 80          | 160         |
    When I list Offers
    Then I'm viewing a list containing
      | Product name  |
      | Fourth        |
      | Third         |
      | Second        |
      | First         |
    And The list contains 4 Offers