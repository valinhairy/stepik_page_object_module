from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_items(self):
        assert self.is_not_presented(*BasketPageLocators.ITEMS_IN_BASKET), \
            "items in basket presented, but shouldn't be"

    def should_be_empy_basket_message(self):
        self.is_element_presented(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert True, "empy basket message isn't presented"
