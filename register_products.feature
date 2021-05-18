Feature: Register Product
  In order to know if a Product is successfully registered
  As a user
  I want to view the registered Products

  Background: There are 2 Productes registered
    Given Exists a user "user" with password "password321"
    And Exists 2 Products registered by "user"
      | Product name    | Company         |
      | Airpods         | Apple           |
      | Motocicleta     | Scalextric      |

  Scenario: View Product list
    Given I login as user "user" with password "password321"
    When I register Product 
      | Product name    | Company         |
      | Teclat          | Microsoft       |
    Then I'm viewing Product list
      | Product name    | 
      | Airpods         |
      | Motocicleta     |
      | Teclat          |
