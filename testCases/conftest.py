import pytest
import pytest_html
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup_driver(browser):
    
    options = Options()
    options.add_argument("--start-maximized")  # Start the browser maximized
    options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation control
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    if browser == "chrome":
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options =options)
    yield driver
    driver.quit()

#Method to run test on multiple browsers
def pytest_addoption(parser): # This method is used to add command line options for pytest
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser to run tests on")

@pytest.fixture()
def browser(request):    # This fixture retrieves the browser type from command line option
    return request.config.getoption("--browser")

# ***Generate Pytest HTML Report*** to do so we add hooks to conftest.py file.
# It is hook for adding environment information to the HTML report.

#Old menethod now updated in new version hence use the below in its place
# def pytest_configure(config):
#   config._metadata['Project Name'] = 'NopCommerce Application'
#   config._metadata['Module Name'] = 'Login Module'
#  config._metadata['Tester'] = 'Rits'

def pytest_html_metadata(metadata):
    metadata['Project Name'] = 'NopCommerce Application'
    metadata['Module Name'] = 'Login Module'
    metadata['Tester'] = 'Rits'

# It is hook for modify//delete environment information in the HTML report.
@pytest.mark.optionalhook
def pytest_html_metadata(metadata):
   metadata.pop('JAVA_HOME', None)  # Remove JAVA_HOME from metadata
   metadata.pop('Plugins', None)  # Remove Plugins from metadata
    
   