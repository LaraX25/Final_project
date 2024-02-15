from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"
        print("Basket is empty")

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCT), \
           "Basket is not empty, but should be"
        print("Basket is empty")
