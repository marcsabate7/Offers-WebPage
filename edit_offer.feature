Feature: Edit Offer
    In order to keep updated my previous registers about offers
    As a user
    I want to edit an offer register I published

    Background: There are registered users and an offer published by one of them
        Given Exists a user "user1" with password "password"
        And Exists a user "user2" with password "password"
        And Exists an offer registered by "user1"
            | Product name  | Company name  | Url offer                                                                       | New price | Old price | Discount |
            | OneBlade Pro  | Philips       | https://www.amazon.es/dp/B0771WVJX3/ref=cm_sw_em_r_mt_dp_ZY2ATH8623PK9EQXP3D0   | 70        | 95        | 26       |

    Scenario: Try to edit an offer but not logged in
        Given I'm not logged in
        When I view the details for offer "OneBlade Pro"
        Then There is no "edit" link available

    Scenario: Try to edit an offer but not the owner
        Given I login as user "user2" with password "password"
        When I view the details for offer "OneBlade Pro"
        Then There is no "edit" link available

    Scenario: Edit owned offer registry New price
        Given I login as user "user1" with password "password"
        When I edit the offer with Product name "OneBlade Pro"
            | New price | Discount  |
            | 62        | 35        |
        Then I'm viewing the details page for an offer by "user1"
            | Product name  | Company name  | Url offer                                                                       | New price | Old price | Discount |
            | OneBlade Pro  | Philips       | https://www.amazon.es/dp/B0771WVJX3/ref=cm_sw_em_r_mt_dp_ZY2ATH8623PK9EQXP3D0   | 62        | 95        | 35       |
        And There are 1 offers

    Scenario: Force edit offer but not the owner permission exception
        Given I login as user "user2" with password "password"
        When I edit the offer with name "OneBlade Pro"
            | New price |
            | 1         |
        Then Server responds with page containing "403 Forbidden"
        When I view the details for the offer of "OneBlade Pro"
        Then I'm viewing the details page for offer by "user1"
            | Product name  | Company name  | Url offer                                                                       | New price | Old price | Discount |
            | OneBlade Pro  | Philips       | https://www.amazon.es/dp/B0771WVJX3/ref=cm_sw_em_r_mt_dp_ZY2ATH8623PK9EQXP3D0   | 70        | 95        | 26       |