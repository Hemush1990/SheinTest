from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#Create basic attributes for pages

class Page(object):
    def __init__(self, driver, base_url = 'https://www.shein.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 20

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, base_url):
        self.driver.get(base_url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def invisible_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.invisibility_of_element(locator))
        return element

    def located_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def click_element(self, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.visibility_of_element_located((locator)))
        return element








