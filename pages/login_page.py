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

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
