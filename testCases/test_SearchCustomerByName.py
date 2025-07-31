import pytest
from pageObjects.searchCustomer import SearchCustomer
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from pageObjects.addNewCustomer import AddNewCustomer
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time 

class Test_TC05_SearchCustomerByName:

    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    base_url = ReadConfig.getBaseUrl()
    search_name = "Steve"
    expected_email = "steve_gates@nopCommerce.com"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self, setup_driver):
        self.logger.info("********** Test_TC05_SearchCustomerByName **********")
        self.logger.info("********** Searching Customer by Name **********")

        self.driver = setup_driver
        
        # Login to the application
        self.logger.info("********** Logging in to the application **********")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver) # Initialize LoginPage / Object for LoginPage
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        #Create an instance of AddNewCustomer class
        self.logger.info("********** Login Successful **********")
        self.logger.info("********** Navigating to Search Customer page **********")
        self.anc = AddNewCustomer(self.driver)
        self.anc.clickHomeCustomersMenu()
        self.anc.clickCustomersMenuItem()
        time.sleep(4)

        # Create an instance of SearchCustomer class
        self.sc = SearchCustomer(self.driver)
        self.logger.info("********** Searching for customer by name **********")
        self.sc.searchByName(self.search_name)
        self.sc.clickSearchButton()
        time.sleep(3)
        # Capture and validate the email in the search results

        captured_email = self.sc.captureEmail()
        self.logger.info(f"Captured Email: {captured_email}")
        if captured_email == self.expected_email:
            assert True, "Customer found successfully"
            self.logger.info(f"Customer Found: {captured_email}")
        else:
            self.logger.error(f"Customer not found. Expected: {self.expected_email}, but got: {captured_email}")
            self.driver.save_screenshot("Screenshots/test_SearchCustomer.png")  
            assert False, f"Expected email is '{self.expected_email}' but got '{captured_email}'"

        self.logger.info("********** Search Customer by Name Test Passed **********")