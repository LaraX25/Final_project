import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        print("all is correct")

    def should_be_login_url(self):
        assert self.url.find("login") != -1, "Login link is not presented"
        print("url is correct")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        print("login form is correct")

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        print("register form is correct")

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS), "Email address field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD), "Confirm password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        # print(self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).text)
        print("New user registration was successful")
