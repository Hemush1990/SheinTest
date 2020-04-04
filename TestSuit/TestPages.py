import unittest
from selenium import webdriver
from Pages.MainPage import MainPage
from .testCase import test_cases
from Locators.Users import users


class Mainpage(object):
    pass



class TestPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.shein.com/')

    def test_loadpage(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.page_loaded())

    def test_search_item(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        search_result = page.search_item('dress')
        self.assertIn("dress", search_result)

    def test_sign_in(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        SignInpage = page.open_sign_up_button()
        self.assertIn("login", SignInpage.get_url())

    def test_sign_in_with_valid_user(self):
        print("\n" + str(test_cases(3)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.open_sign_up_button()
        result = loginPage.valid_user(users)
        self.assertIn("user", result.get_url())

    def test_invalid_user(self):
        print("\n" + str(test_cases(3)))
        mainPage = MainPage(self.driver)
        loginPage = mainPage.open_sign_up_button()
        result = loginPage.valid_user(users[2])
        self.assertNotIn("user", result.get_url())

    def tearDown(self):
        self.driver.close()

if __name__ =="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)
