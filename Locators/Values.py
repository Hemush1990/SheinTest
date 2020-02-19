from selenium.webdriver.common.by import By

class MainpageLocators(object):
    Logo = (By.XPATH, "//*[@class = 'iconfont-critical icon-sheinlogo']")
    Account = (By.XPATH, "//*[@class= 'iconfont-critical icon-yonghuicon-']")
    Sign_in = (By.XPATH, "//*[@class = 'j-header-username header-username ga_login_btn']")
    Search = (By.NAME, "header-search")
    Search_button = (By.CLASS_NAME, 'search-btn she-btn-black j-search-btn')

class LoginpageLocators(object):
    Email = (By.CSS_SELECTOR, '[data-login-source="loginPage"] [name="email"]')
    Password = (By.CSS_SELECTOR, '[data-login-source="loginPage"] [name="password"]')
    Sign = (By.CSS_SELECTOR, '[data-login-source="loginPage"] [class="she-btn-black she-btn-l she-btn-block"]')


