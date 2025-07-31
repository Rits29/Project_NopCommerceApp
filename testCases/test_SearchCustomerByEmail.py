import pytest
from pageObjects.searchCustomer import SearchCustomer
from pageObjects.loginPage import LoginPage
from pageObjects.addNewCustomer import AddNewCustomer
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time 

class Test_TC04_SearchCustomerByEmail:

    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    base_url = ReadConfig.getBaseUrl()
    search_email = "steve_gates@nopCommerce.com"
    expected_name = "Steve Gates"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup_driver):
        self.logger.info("********** Test_TC04_SearchCustomerByEmail **********")
        self.logger.info("********** Searching Customer by Email **********")

        self.driver = setup_driver
        
        
        # Login to the application
        self.logger.info("********** Logging in to the application **********")
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver) # Initialize LoginPage / Object for LoginPage
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)

        #Create an instance of AddNewCustomer class
        self.logger.info("********** Login Successful **********")
        self.logger.info("********** Navigating to Search Customer page **********")
        self.anc = AddNewCustomer(self.driver)
        self.anc.clickHomeCustomersMenu()
        self.anc.clickCustomersMenuItem()
        time.sleep(3)

        # Create an instance of SearchCustomer class
        self.sc = SearchCustomer(self.driver)
        self.logger.info("********** Searching for customer by email **********")
        self.sc.searchByEmail(self.search_email)
        self.sc.clickSearchButton()
        time.sleep(3)
        
        # Capture and validate the name in the search results

        captured_name = self.sc.captureName()
        self.logger.info(f"Captured Name: {captured_name}")
        if captured_name == self.expected_name:
            assert True, "Customer found successfully"
            self.logger.info(f"Customer Found: {captured_name}")
        else:
            self.logger.error(f"Customer not found. Expected: {self.expected_name}, but got: {captured_name}")
            self.driver.save_screenshot("Screenshots/test_SearchCustomer.png")  
            assert False, f"Expected name is '{self.expected_name}' but got '{captured_name}'"
        self.logger.info("********** Search Customer by Email Test Passed **********")
