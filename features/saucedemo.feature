Feature: SauceDemo Login Functionality

  Scenario: Successful Login - UI
    Given I am on the SauceDemo login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to Home Page

  Scenario: Invalid Login
    Given I am on the SauceDemo login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message "username and password do not match any user in this service"

  Scenario: Successful Logout
    Given I am on the SauceDemo login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to Home Page
    When I click "react-burger-menu-btn"
    And I click "logout_sidebar_link"
    Then I should be redirected to SauceDemo login page

  Scenario: Navigate to the cart
    Given I am on the SauceDemo login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to Home Page
    When I click "shopping_cart_container"
    Then I should be taken to the "cart" page

  Scenario: Navigate to Products List "Continue Shopping" from cart
    Given I am already a logged user
    When I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click "continue-shopping"
    Then I should be taken to the "inventory" page

  Scenario Outline: The user can add and remove items on Swag Labs Page
    Given I am on the SauceDemo login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to Home Page
    And I have a list of <items> to order
    When I click 'Add to cart' for each item
    When I click 'Remove' for each item
    Examples:
      | items                                      |
      | Sauce Labs Backpack, Sauce Labs Bike Light |

  Scenario Outline: The user can add a number of items to their cart
    Given I am on the SauceDemo login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to Home Page
    And I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    Then I should see <items> in the cart
    Examples:
      | items                                      |
      | Sauce Labs Backpack, Sauce Labs Bike Light |

  Scenario Outline: The user can remove all items from the cart
    Given I am already a logged user
    Then I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click 'Remove' for each item
    Then the cart is empty
    Examples:
      | items                                       |
      | Sauce Labs Fleece Jacket, Sauce Labs Onesie |

  Scenario Outline: The user can navigate to Checkout Page
    Given I am already a logged user
    Then I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click "checkout"
    Then I should be taken to the "checkout-step-one" page
    Examples:
      | items             |
      | Sauce Labs Onesie |


  Scenario Outline: The user can check the Personal Data required on Checkout Page
    Given I am already a logged user
    Then I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click "checkout"
    Then I should be taken to the "checkout-step-one" page
    When I click "continue"
    Then I should see an error message "Error: First Name is required"

    Examples:
      | items             |
      | Sauce Labs Onesie |

  Scenario Outline: The user can enter Personal Data on Checkout Page
    Given I am already a logged user
    Then I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click "checkout"
    Then I should be taken to the "checkout-step-one" page
    And I enter personal data
    When I click "continue"
    Then I should be taken to the "checkout-step-two" page
    Examples:
      | items             |
      | Sauce Labs Onesie |

  Scenario Outline: The user can complete an order - E2E test
    Given I am already a logged user
    Then I have a list of <items> to order
    When I click 'Add to cart' for each item
    And I click "shopping_cart_container"
    Then I should be taken to the "cart" page
    When I click "checkout"
    Then I should be taken to the "checkout-step-one" page
    And I enter personal data
    When I click "continue"
    Then I should be taken to the "checkout-step-two" page
    When I click "finish"
    Then I should be taken to the "checkout-complete" page
    Examples:
      | items             |
      | Sauce Labs Onesie |
