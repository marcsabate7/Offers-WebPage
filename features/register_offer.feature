Feature: Register Offer
    In order to keep track the offers I consult
    As a user
    I want to register an offer with their prices and their origin

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Try to register an offer but not logged in
        Given I'm not logged in
        When I register Offer
            | Product name  | Company name  | Url offer                                                                       | New price | Old price | Discount |
            | OneBlade Pro  | Philips       | https://www.amazon.es/dp/B0771WVJX3/ref=cm_sw_em_r_mt_dp_ZY2ATH8623PK9EQXP3D0   | 70        | 95        | 26       |
        Then I'm redirected to the login form
        And There are 0 offers

    Scenario: Register an offer
        Given I login as user "user" with password "password"
        When I register Offer
            | Product name  | Company name  | Url offer                                                                        | New price  | Old price  | Discount |
            | Airpods       | Apple         | https://www.fnac.es/Apple-Airpods-Auriculares-Auriculares-inalambricos/a1318455  | 129        | 180        | 15       | 
        Then I'm viewing the details page for offer by "user"
            | Author   | Product name   | Company name   | New price  | Old price  | Discount |
            | user     | Airpods        | Apple          | 129        | 180        | 15       |
        And There are 1 offers

    Scenario: Register just the product and url of an offer
        Given I login as user "user" with password "password"
        When I register Offer
            | Product name      | Company name  | Url offer                                                                                                 |
            | Mi Smart Band 6   | Xiaomi        | https://www.fnac.es/Xiaomi-Mi-Smart-Band-6-Producto-conectado-Pulsera-rastreador-de-actividad/a8214196    |
        Then I'm viewing the details page for offer by "user"
            | Author   | Product name      | Company name  |
            | user     | Mi Smart Band 6   | Xiaomi        |
        And There are 1 offers

    Scenario: Register an offer with picture
        Given I login as user "user" with password "password"
        When I register Offer
            | Product name      | Image                | Company name  | Url offer                                                                     | New price | Old price | Discount |
            | Maletín X-Line    | offers/download.png  | Bosch         | https://www.amazon.es/dp/B000P4IQF2/ref=cm_sw_em_r_mt_dp_0RBQJ0TR0KEH73PSWMC2 | 24        | 30        | 20       |
        Then I'm viewing the details page for offer by "user"
            | Author    | Product name      | Image                | Company name   | New price | Old price | Discount |
            | user      | Maletín X-Line    | offers/download.png  | Bosch          | 24        | 30        | 20       |
        And There are 1 offers



  
  
  
  
  
  
