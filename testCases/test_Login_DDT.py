from pydoc import text
import time
from utilities.excelUtils import ReadWriteExcel
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
from pageObjects.loginPage import LoginPage

class Test_TC02_Login_DDT:

    #create the variables for the data to be used in the test case
    base_url = ReadConfig.getBaseUrl()
    path_data_file = ".//TestData/Login_TestData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_DDT(self, setup_driver: WebDriver):

        self.logger.info("********** Test_TC02_Login_DDT **********")
        self.logger.info("********** Verifying Login DDT **********")
        self.driver = setup_driver
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        
        # Create an instance of the LoginPage class, create an object of the LoginPage class
        self.lp = LoginPage(self.driver)

        # Get the row count from the Excel file
        self.row_count = ReadWriteExcel.get_row_count(self.path_data_file, "Sheet1")
        self.logger.info(f"Total number of rows in the Excel file: {self.row_count}")
        self.col_count = ReadWriteExcel.get_col_count(self.path_data_file, "Sheet1")
        self.logger.info(f"Total number of columns in the Excel file: {self.col_count}")
        # Iterate through each row in the Excel file

        for i in range(2, self.row_count + 1):  # Start from row 2 to skip header
            self.username = ReadWriteExcel.read_data(self.path_data_file, "Sheet1", i, 1)
            self.password = ReadWriteExcel.read_data(self.path_data_file, "Sheet1", i, 2)
            self.result = ReadWriteExcel.read_data(self.path_data_file, "Sheet1", i, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            if self.result == "fail":
                if self.driver.find_element(By.XPATH, '//div[@class="message-error validation-summary-errors"]').is_displayed():
                    assert True
                    self.logger.info(f"********** Login Failed as expected for username: {self.username} and {self.password} **********")
            else:
                if self.result == "pass":       # Click the login button
                    #time.sleep(17)
                   # input("Complete Captcha if prompted, then press Enter to continue...")
                    time.sleep(5)
                # Verify if the user is logged in by checking the presence of the logout link
                    if self.driver.find_element(By.LINK_TEXT, self.lp.logout_linktext).is_displayed():
                        assert True
                        self.logger.info("********** Login Successful **********")
                    else:
                        self.driver.save_screenshot("./Screenshots/" + "test_Login.png")
                        self.logger.error("********** Login Failed: Logout link not found **********")
                        assert False, "Login failed, Logout link not found"
            
       




