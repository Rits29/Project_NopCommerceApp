import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
from pageObjects.loginPage import LoginPage

class Test_TC01_Login:

    #create the variables for the data to be used in the test case
    base_url = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self, setup_driver: WebDriver):

        self.logger.info("********** Test_TC01_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")

        self.driver = setup_driver
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page Title Verified Successfully **********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_HomePageTitle.png")
            self.logger.error(f"********** Home Page Title Verification Failed: Expected 'nopCommerce demo store. Login' but got '{actual_title}' **********")
            self.driver.close()
            assert False, f"Expected title is 'nopCommerce demo store. Login' but got '{actual_title}'"
            
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup_driver: WebDriver):

        self.logger.info("********** Verifying Login Functionality **********")

        self.driver = setup_driver
        self.driver.get(self.base_url)
        
        # Create an instance of the LoginPage class, create an object of the LoginPage class
        self.lp = LoginPage(self.driver)

        # Set username and password using the methods from LoginPage class
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        # Click the login button
        self.lp.clickLogin()
        time.sleep(5)
        #input("Complete Captcha if prompted, then press Enter to continue...")
        # Verify if the user is logged in by checking the presence of the logout link
        if self.driver.find_element(By.LINK_TEXT, self.lp.logout_linktext).is_displayed():
            assert True
            self.logger.info("********** Login Successful **********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_Login.png")
            self.logger.error("********** Login Failed: Logout link not found **********")
            assert False, "Login failed, Logout link not found"
        
        # Click the logout link to log out
        self.lp.clickLogout()




