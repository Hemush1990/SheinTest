from Pages.basescreen import Page
from selenium.webdriver.common.keys import Keys
from Locators.Values import MainpageLocators
from .LoginPage import Loginpage


class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainpageLocators
        super().__init__(driver)

    def page_loaded(self):
        return True if self.find_element(*self.locator.Logo) else False

    def search_item(self, item):
        self.find_element(*self.locator.Search).send_keys(item)
        self.find_element(*self.locator.Search).send_keys(Keys.ENTER)
        return item

    def open_sign_up_button(self):
        self.hover(*self.locator.Account)
        self.find_element(*self.locator.Sign_in).click()
        return Loginpage(self.driver)
