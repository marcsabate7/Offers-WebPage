Feature: Register Product
    In order to know if a Product is successfully registered
    As a user
    I want to view the registered Products

    Background: There are 2 Productes registered
        Given Exists a user "user" with password "password321"
        And Exists a product registered by "user"
          | Product name    | Company         |
          | Motocicleta     | Scalextric      |

    Scenario: View Product list
        Given I login as user "user" with password "password321"
        When I register Product
            | Product name    | Company         |
            | Teclat          | Microsoft       |
        Then I'm viewing the details page for products by "user"
            | Product name    |
            | Motocicleta     |
            | Teclat          |
        And There are 2 products
