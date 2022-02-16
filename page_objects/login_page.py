from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url,\
            f"wrong URL, expected /accounts/login/, got {self.browser.current_url} instead"

    def should_be_login_form(self):
        self.is_element_presented(*LoginPageLocators.LOGIN_FORM)
        assert True, "login form isn't presented"

    def should_be_register_form(self):
        self.is_element_presented(*LoginPageLocators.REGISTER_FORM)
        assert True, "register form isn't presented"
