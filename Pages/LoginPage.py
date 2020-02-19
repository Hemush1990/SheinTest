from selenium.webdriver.common.keys import Keys
from Pages.basescreen import Page
from Locators.Values import LoginpageLocators
from Locators import Users
from selenium.webdriver.support.ui import WebDriverWait
import time

class Loginpage(Page):
    def __init__(self, driver):
        self.locator = LoginpageLocators
        super(Loginpage, self).__init__(driver)

    def enter_email(self, user):
        wait = WebDriverWait(self.driver, 30)
        email_field = self.located_element(LoginpageLocators.Email)
        #email_field = self.located_element(self.locator.Email)
        email_field.send_keys(Users.get_user(user)['email'])

    def enter_password(self, user):
        self.find_element(*self.locator.Password).send_keys(Users.get_user(user)["password"])

    def click_login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        time.sleep(5)
        self.find_element(*self.locator.Sign).click()
        return Homepage(self.driver)

    def valid_user(self, user):
        self.click_login(user)
        return Homepage(self.driver)

    def invalid_user(self, user):
        self.click_login(user)
        print("Login isn't valid")

class Homepage(Page):
    pass