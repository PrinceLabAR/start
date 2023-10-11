import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to initialize the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Module: User Management
@allure.feature("User Management")

# User Registration
@allure.story("User Registration")
class TestUserRegistration:
    # Test Case 1: Verify that a new user can successfully register with valid information.
    def test_user_registration_success(self, driver):
        with allure.step("User Registration: Successful Registration"):
            driver.get("https://shop.hishabee.business/register")
            # Your registration code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="registration_success_screenshot", attachment_type=allure.attachment_type.PNG)

    # Test Case 2: Verify that registration fails when using an already registered email.
    def test_user_registration_failure_existing_email(self, driver):
        with allure.step("User Registration: Registration Failure (Existing Email)"):
            driver.get("https://shop.hishabee.business/register")
            # Your registration code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="registration_failure_screenshot", attachment_type=allure.attachment_type.PNG)

# User Login
@allure.story("User Login")
class TestUserLogin:
    # Test Case 3: Ensure a registered user can log in successfully with correct credentials.
    def test_user_login_success(self, driver):
        email = "prince.roy.bauet@gmail.com"
        password = "P@123456789"
        with allure.step("User Login: Successful Login"):
            driver.get("https://shop.hishabee.business/login")
            # Your login code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="login_success_screenshot", attachment_type=allure.attachment_type.PNG)

    # Test Case 4: Ensure login fails with incorrect credentials.
    def test_user_login_failure_incorrect_credentials(self, driver):
        email = "prince.roy.bauet@gmail.com"
        password = "P@113456789"
        with allure.step("User Login: Login Failure (Incorrect Credentials)"):
            driver.get("https://shop.hishabee.business/login")
            # Your login code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="login_failure_screenshot", attachment_type=allure.attachment_type.PNG)

# User Profile Update
@allure.story("User Profile Update")
class TestUserProfileUpdate:
    # Test Case 5: Confirm that a user can update their profile information (e.g., name, email, phone).
    def test_user_profile_update_success(self, driver):
        with allure.step("User Profile Update: Successful Update"):
            driver.get("https://shop.hishabee.business/dashboard/profile")
            # Your profile update code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="profile_update_success_screenshot", attachment_type=allure.attachment_type.PNG)

    # Test Case 6: Check if the user profile update fails with invalid data.
    def test_user_profile_update_failure_invalid_data(self, driver):
        with allure.step("User Profile Update: Update Failure (Invalid Data)"):
            driver.get("https://shop.hishabee.business/dashboard/profile")
            # Your profile update code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="profile_update_failure_screenshot", attachment_type=allure.attachment_type.PNG)

# User Account Deactivation
@allure.story("User Account Deactivation")
class TestUserAccountDeactivation:
    # Test Case 7: Verify that a user can deactivate their account successfully.
    def test_user_account_deactivation_success(self, driver):
        with allure.step("User Account Deactivation: Successful Deactivation"):
            driver.get("https://shop.hishabee.business/dashboard/profile")
            # Your account deactivation code here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="account_deactivation_success_screenshot", attachment_type=allure.attachment_type.PNG)

    # Test Case 8: Verify that a deactivated account cannot log in.
    def test_deactivated_account_login_failure(self, driver):
        email = "prince.roy.bauet@gmail.com"
        password = "P@113456789"
        with allure.step("User Account Deactivation: Deactivated Account Login Failure"):
            driver.get("https://shop.hishabee.business/login")
            # Your login code for a deactivated account here

            # Capture and attach a screenshot to the Allure report
            allure.attach(driver.get_screenshot_as_png(), name="deactivated_account_login_failure_screenshot", attachment_type=allure.attachment_type.PNG)
# Module: Product Management
@allure.feature("Product Management")

# Create Product
@allure.story("Create Product")
class TestCreateProduct:
    # Test Case 9: Ensure a user can create a new product with valid information.
    def test_create_product_success(self, driver):
        with allure.step("Create a new product with valid information"):
            # Your product creation code here
            pass

    # Test Case 10: Verify that product creation fails with incomplete or invalid data.
    def test_create_product_failure_invalid_data(self, driver):
        with allure.step("https://shop.hishabee.business/product/150"):
            # Your product creation code here
            pass

# View Product
@allure.story("View Product")
class TestViewProduct:
    # Test Case 11: Confirm that users can view a list of available products.
    def test_view_product_list(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to view the product list here
            pass

    # Test Case 12: Check if product details are displayed correctly.
    def test_view_product_details(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to view product details here
            pass

# Update Product
@allure.story("Update Product")
class TestUpdateProduct:
    # Test Case 13: Verify that a user can update product information.
    def test_update_product_success(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to update product information here
            pass

    # Test Case 14: Ensure product update fails with invalid data.
    def test_update_product_failure_invalid_data(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to update product information here
            pass

# Delete Product
@allure.story("Delete Product")
class TestDeleteProduct:
    # Test Case 15: Ensure a user can delete a product.
    def test_delete_product_success(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to delete a product here
            pass

    # Test Case 16: Confirm that a deleted product is no longer accessible.
    def test_deleted_product_inaccessibility(self, driver):
        with allure.step("https://shop.hishabee.business/cart"):
            # Your code to check product accessibility here
            pass

# Module: Order Management
@allure.feature("Order Management")

# Place an Order
@allure.story("Place an Order")
class TestPlaceOrder:
    # Test Case 17: Ensure a user can place an order successfully.
    def test_place_order_success(self, driver):
        with allure.step("https://shop.hishabee.business/checkout"):
            # Your code to place an order here
            pass

    # Test Case 18: Verify that order placement fails with invalid product selection.
    def test_place_order_failure_invalid_product(self, driver):
        with allure.step("https://shop.hishabee.business/checkout"):
            # Your code to place an order here
            pass

# View Order History
@allure.story("View Order History")
class TestViewOrderHistory:
    # Test Case 19: Confirm that a user can view their order history.
    def test_view_order_history(self, driver):
        with allure.step("https://shop.hishabee.business/checkout"):
            # Your code to view order history here
            pass

    # Test Case 20: Check if order history displays accurate information.
    def test_order_history_accuracy(self, driver):
        with allure.step("https://shop.hishabee.business/checkout"):
            # Your code to verify order history information here
            pass

if __name__ == "__main__":
    # Run the test with Pytest and Allure
    pytest.main(["-s", "-v", "--alluredir=./allure-results"])
