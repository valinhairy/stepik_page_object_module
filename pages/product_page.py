from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def is_product_in_success_message_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, f"added product name doesn't match,\
         got {added_product_name} instead of {product_name}"

    def is_price_in_success_message_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert product_price == added_product_price, f"added product price doesn't match\
         got {added_product_price} instead of {product_price}"

    def should_not_be_success_message(self):
        assert self.is_not_presented(*ProductPageLocators.SUCCESS_MESSAGE), \
            "success message presented, but shouldn't be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "success message hasn't disappeared"
