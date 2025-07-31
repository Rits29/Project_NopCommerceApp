from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    # Declare the locators as class variables
    username_textbox_id = "Email"
    password_textbox_id = "Password"
    login_button_xpath = "//button[normalize-space()='Log in']"
    logout_linktext = "Logout"
    
    # Initialize the LoginPage with a WebDriver instance, Constructor
    def __init__(self, driver):    
        self.driver = driver
    
    # Method to set the username in the username textbox
    def setUserName(self, username):
        element = self.driver.find_element(By.ID, self.username_textbox_id)
        element.clear()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(username).perform()
    
    # Method to set the password in the password textbox
    def setPassword(self, password):
        element = self.driver.find_element(By.ID, self.password_textbox_id)
        element.clear()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(password).perform()
        
    # Method to click the login button
    def clickLogin(self):
        element = self.driver.find_element(By.XPATH, self.login_button_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    # Method to click the logout link
    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_linktext).click()
    
