import random
import string
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pageObjects.addNewCustomer import AddNewCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
import pytest
from pageObjects.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions

class Test_TC03_AddNewCustomer:

    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    base_url = ReadConfig.getBaseUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_AddNewCustomer(self, setup_driver):
        try:
            self.logger.info("********** Test_TC03_AddNewCustomer **********")
            self.logger.info("********** Test_TC03_AddNewCustomer **********")
            self.logger.info("********** Adding New Customer **********")

            self.driver = setup_driver

            self.logger.info("********** Logging in to the application **********")
            self.driver.get(ReadConfig.getBaseUrl())
            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            #input("Complete Captcha if prompted, then press Enter to continue...")  
            time.sleep(3)
            self.logger.info("********** Login Successful **********")
            self.logger.info("********** Navigating to Add New Customer page **********")
            
            # Create an instance of the AddNewCustomer class
            self.anc = AddNewCustomer(self.driver)

            # Click on the "Add New" button
            self.anc.clickHomeCustomersMenu()
            self.anc.clickCustomersMenuItem()
            self.anc.clickAddNewButton()
            self.logger.info("********** Filling in customer details **********")   
            # Fill in the customer details
            self.email = random_email_generator() + "@gmail.com"
            self.logger.info(f"Generated email: {self.email}")
            self.nPassword = random_email_generator()
            self.fname = random_email_generator()
            self.lname = "xyz78"
            self.gender = "Male"
            self.company = "XYZ Pvt Ltd"
            self.is_tax_exempt = "No"
            self.customer_role = "Registered"
            self.vendor = "Not a vendor"
            self.admin_comment = "This is a test comment"
            self.actual_message = "The new customer has been added successfully."

            self.anc.setEmail(self.email)
            self.anc.setPassword(self.nPassword)
            self.anc.setFirstName(self.fname)
            self.anc.setLastName(self.lname)
            self.anc.selectGender(self.gender)
            self.anc.setCompany(self.company)
            self.anc.setTaxExempt(self.is_tax_exempt)
            #self.anc.selectCustomerRole(self.customer_role)
            self.anc.selectVendor(self.vendor)
            self.anc.setAdminComment(self.admin_comment)
            self.anc.clickSaveButton()
            self.logger.info("********** Verify if the customer is added successfully **********")   
            # Verify if the customer was added successfully
            success_message = self.anc.getSuccessMessage()
            success_message = success_message.replace("×", "").strip()
            if success_message.lower() == self.actual_message.lower():
                self.logger.info("********** Customer added successfully **********")
                assert True
            else:
                self.logger.error(f"********** Customer addition failed: Expected '{self.actual_message}' but got '{success_message}' **********")
                self.driver.save_screenshot("Screenshots/" + "test_AddNewCustomer.png")
                assert False, f"Expected message is '{self.actual_message}' but got '{success_message}'"
                    
        except Exception as e:
            self.logger.error(f"********** An error occurred: {str(e)} **********")
            self.driver.save_screenshot("Screenshots/" + "test_AddNewCustomer_error.png")
            assert False, f"Test failed due to an error: {str(e)}"

#Random function to generate a random data.
def random_email_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

