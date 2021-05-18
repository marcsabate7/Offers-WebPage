Feature: Delete Offers
    In order to no longer see the deleted Offers in myOffers
    As a user
    I want to list three registered Offers without the deleted one

    Background: There are instances of Offers registered
        Given Exists a user "user" with password "password"
        And Exists offer "Airpods" registered by "user"
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |

    Scenario: Delete offer as user
        Given I login as user "user" with password "password321"
        When I register an offer with name "Airpods"
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        Then I'm viewing the details page for offer "Airpods" by the user "user"
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        And There is "Delete" link available
        And There is "Update" link available

    Scenario: Delete offer as different user
        Given I login as user "user2" with password "password321"
        When I'm in the details page for offer "Airpods" registered by the user "user" 
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        Then I'm viewing the details page for offer "Airpods" registered by the user "user"
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        And There is no "Delete" link available
        And There is no "Update" link available

    Scenario: Try to delete offer but not logged in
        Given I'm not logged in
        When I'm in the details page for offer "Airpods" registered by the user "user" 
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        Then I'm viewing the details page for offer "Airpods" registered by the user "user"
        | Product name    | New Price   | Old Price   |
        | Airpods         | 50          | 100         |
        And There is no "Delete" link available
        And There is no "Update" link available