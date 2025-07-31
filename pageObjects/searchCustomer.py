#Search using email and name. Validate if present in table search successfully.
from selenium.webdriver.common.by import By


class SearchCustomer:
    
    #Write the locators for the elements in the Add New Customer page
    home_Customers_menu_xpath = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]'
    home_Customers_menuitem_xpath = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]/ul/li[1]'
    email_textbox_id = 'SearchEmail'
    fname_textbox_id = 'SearchFirstName'
    lname_textbox_id = 'SearchLastName'
    regDateFrom_textbox_id = 'SearchRegistrationDateFrom'
    regDateTo_textbox_id = 'SearchRegistrationDateTo'
    custRole_dropdown_xpath = '//input[@class="select2-search__field"]'
    search_button_id = 'search-customers'
    name_xpath_table = '//table[@class="table table-bordered table-hover table-striped dataTable"]/tbody/tr[1]/td[3]'
    email = "steve_gates@nopCommerce.com"
    email_xpath_table = '//table[@class="table table-bordered table-hover table-striped dataTable"]/tbody/tr[1]/td[2]'

    def __init__(self, driver):
        self.driver = driver

    def searchByEmail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(self.email)

    def clickSearchButton(self):
        self.driver.find_element(By.ID, self.search_button_id).click()

    def captureName(self):
        return self.driver.find_element(By.XPATH, self.name_xpath_table).text
    
    def searchByName(self, first_name):
        self.driver.find_element(By.ID, self.fname_textbox_id).send_keys(first_name)

    def captureEmail(self):
        return self.driver.find_element(By.XPATH, self.email_xpath_table).text 
    
