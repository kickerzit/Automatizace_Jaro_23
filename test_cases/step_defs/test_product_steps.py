from pytest_bdd import given, when, then, scenarios
import pytest
from page_objects.ProductPage import ProductPage
from time import sleep
from conftest import product_page

scenarios("../features/products.feature")

@given("I am logged in")
def I_am_logged_in(product_page):
    
    # No code here, we are using a fixture from conftest.py to get logged in the page, so we just verify that we are on the "Products" page
    title = product_page.get_title_text()

    if title == "Products":
        assert True
    
    else: 
        print("Test Failed!")
        assert False

@when("I click on t-shirt")
def click_on_t_shirt(product_page):
    
    product_page.click_on_t_shirt()

@then("I see the correct description")
def verify_t_shirt_desc(product_page):
    
    desc = product_page.get_t_shirt_description()

    sleep(2)

    if desc == "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.":
        assert True

    else: 
        print("Test Failed!")
        assert False

@when("I add shirt to cart")
def add_t_shirt_to_cart():

    t_shirt_price = driver.find_element(By.CLASS_NAME, "inventory_details_price").text
    sleep(1)

    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    sleep(1)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    sleep(1)

    your_cart_text = driver.find_element(By.CLASS_NAME, "title").text
    sleep(1)

    cart_item1_text = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    sleep(1)

    assert your_cart_text == "Your Cart"
    assert t_shirt_price == "$15.99"
    assert cart_item1_text == "Test.allTheThings() T-Shirt (Red)"

@then("I can complete the checkout")
def complete_checkout():

    driver.find_element(By.ID, "checkout").click()
    sleep(1)

    driver.find_element(By.ID, "first-name").clear()
    driver.find_element(By.ID, "first-name").send_keys("First_Name_Test")

    driver.find_element(By.ID, "last-name").clear()
    driver.find_element(By.ID, "last-name").send_keys("Last_Name_Test")

    driver.find_element(By.ID, "postal-code").clear()
    driver.find_element(By.ID, "postal-code").send_keys("60200")
    sleep(1)

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    thank_you_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    sleep(1)

    assert thank_you_message == "Thank you for your order!"
 