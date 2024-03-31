from behave import given, when, then
import time
from src.pages.SauceDemoPage import SauceDemoPage
from src.utility.WebDriver import WebDriver
from src.utility.Constants import Constants


@given('I am on the SauceDemo login page')
def step_impl(context):
    context.driver = WebDriver().get_driver()
    context.SauceDemoPage = SauceDemoPage(context.driver)
    context.driver.get(Constants.BASE_URL)


@when('I enter valid credentials')
def step_impl(context):
    context.SauceDemoPage.login(Constants.USERNAME, Constants.PASSWORD)


@when('I click the login button')
def step_impl(context):
    pass  # No action needed, since login_page.login() already clicks the login button


@then('I should be redirected to Home Page')
def step_impl(context):
    time.sleep(1)
    assert context.SauceDemoPage.is_user_redirect_home_screen(), "User is not logged in successfully."


@then('I should be redirected to SauceDemo login page')
def step_impl(context):
    time.sleep(1)
    assert context.SauceDemoPage.is_user_redirect_login_screen(), "User is not logged on login page."


@given('I am already a logged user')
def step_impl(context):
    context.driver = WebDriver().get_driver()
    context.SauceDemoPage = SauceDemoPage(context.driver)
    context.driver.get(Constants.BASE_URL)
    context.SauceDemoPage.login(Constants.USERNAME, Constants.PASSWORD)
    time.sleep(1)
    assert context.SauceDemoPage.is_user_redirect_home_screen(), "User is not logged in successfully."


@when('I enter invalid credentials')
def step_impl(context):
    context.SauceDemoPage.login("invalid_username", "invalid_password")


@then('I should see an error message "{error_displayed}"')
def step_impl(context, error_displayed):
    time.sleep(1)
    error_message = context.SauceDemoPage.get_error_message()
    assert error_displayed.lower() in error_message.lower()


# ******************* Item steps *************

@then('I have a list of {items} to order')
def step_impl(context, items):
    context.items = [item.strip() for item in items.split(',')]


@when("I click 'Add to cart' for each item")
def step_impl(context):
    context.SauceDemoPage.add_items_to_cart(context.items)
    time.sleep(1)


@when("I click 'Remove' for each item")
def step_impl(context):
    context.SauceDemoPage.simple_remove_items(context.items)
    time.sleep(1)


@when('I click "{element_id}"')
def step_impl(context, element_id):
    context.SauceDemoPage.clickById(element_id)
    time.sleep(1)


@then('I should be taken to the "{page_name}" page')
def step_impl(context, page_name):
    expected_url = f"{Constants.BASE_URL}{page_name}.html"
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
    time.sleep(1)


@then('I should see {items} in the cart')
def step_impl(context, items):
    assert context.SauceDemoPage.item_is_in_cart(items), "No items are displayed in the cart."
    time.sleep(1)


@then('the cart is empty')
def step_impl(context):
    assert not context.SauceDemoPage.item_is_in_cart(context.items), "Items are displayed in the cart."
    (time.sleep(1))


# ******************* Checkout steps *************

@then('I enter personal data')
def step_impl(context):
    context.SauceDemoPage.enter_personal_data()
    (time.sleep(1))
