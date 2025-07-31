from selenium.webdriver.common.by import By

class AddNewCustomer:

    # Locators for the elements in the Add New Customer page
    home_Customers_menu_xpath = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]'
    customers_menuitem_xpath = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]/ul/li[1]'
    addNew_button_xpath = '//a[@href="/Admin/Customer/Create"]'

    email_textbox_id = 'Email'
    password_textbox_id = 'Password'
    fname_textbox_id = 'FirstName'
    lname_textbox_id = 'LastName'
    gMale_optbtn_xpath = '//div[@class="raw"]/div[1]/input'
    gFemale_optbtn_xpath = '//div[@class="raw"]/div[2]/input'
    company_textbox_xpath = '//input[@name="Company"]'
    tax_checkbox_xpath = '//input[@id="IsTaxExempt"]'
    custRole_dropdown_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--below select2-container--focus']//input[@role='searchbox']"
    custRole_delete_xpath = '//li[@title="Registered"]/span[@class="select2-selection__choice__remove"]'
    custRole_DD_Options_xpath = '//div[@class="select2-blue"]/select[@name="SelectedCustomerRoleIds"]/option[3]'
    vendor_dropdown_xpath = '//select[@id="VendorId"]'
    vendor_DD_Options_xpath = '//select[@id="VendorId"]/option'
    admincomment_textarea_xpath = '//div/textarea[@name="AdminComment"]'
    save_button_xpath = '//div/button[@name="save"]'
    save_message_xpath = '//div[@class="alert alert-success alert-dismissable"]'

    # Initialize the AddNewCustomer with a WebDriver instance, Constructor
    def __init__(self, driver):    
        self.driver = driver
    
    #Methods to interact with the elements in the Add New Customer page

    def clickHomeCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.home_Customers_menu_xpath).click()

    def clickCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.customers_menuitem_xpath).click()

    def clickAddNewButton(self):
        self.driver.find_element(By.XPATH, self.addNew_button_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
    
    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.fname_textbox_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.lname_textbox_id).send_keys(lname)

    def selectGender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.XPATH, self.gMale_optbtn_xpath).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.XPATH, self.gFemale_optbtn_xpath).click()
        
    def setCompany(self, company):
        self.driver.find_element(By.XPATH, self.company_textbox_xpath).send_keys(company)

    def setTaxExempt(self, is_tax_exempt):
        if is_tax_exempt.lower() == "yes":
            self.driver.find_element(By.XPATH, self.tax_checkbox_xpath).click()
        else:
            checkbox = self.driver.find_element(By.XPATH, self.tax_checkbox_xpath)
            if checkbox.is_selected():
                checkbox.click()

    def selectCustomerRole(self, role):
        textbox = self.driver.find_element(By.XPATH, self.custRole_delete_xpath) #On del field is focused no other click needed.
        self.driver.execute_script("arguments[0].click();", textbox)  # Clear the existing role
        option = self.driver.find_element(By.XPATH, self.custRole_DD_Options_xpath)
        self.driver.execute_script("arguments[0].click();", option)
        #self.driver.find_element(By.XPATH, self.custRole_dropdown_xpath).click()
        # Wait for the dropdown options to be visible
        options = self.driver.find_elements(By.XPATH, self.custRole_DD_Options_xpath)
        #for option in options:
         #   if option.text.lower() == role.lower():
          #      self.driver.execute_script("arguments[0].click();", option)  # Click the desired role
                #execute_script is used to avoid issues with Selenium not being able to click on the element
                # when the dropdown is open. This is a javascript workaround.
                # This is a workaround for Selenium's limitations with certain dropdowns.
          #      break
    
    def selectVendor(self, vendor):
        textbox = self.driver.find_element(By.XPATH, self.vendor_dropdown_xpath)
        self.driver.execute_script("arguments[0].click();", textbox)
        # Wait for the dropdown options to be visible
        options = self.driver.find_elements(By.XPATH, self.vendor_DD_Options_xpath)
        for option in options:
            if option.text.lower() == vendor.lower():
                self.driver.execute_script("arguments[0].click();", option)
                break

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.admincomment_textarea_xpath).send_keys(comment)

    def clickSaveButton(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def getSuccessMessage(self):
        return self.driver.find_element(By.XPATH, self.save_message_xpath).text
    
    