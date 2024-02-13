from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_to_cart(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException):
            return False
        return True

    def should_be_added_to_cart(self):
        assert self.add_to_cart(*ProductPageLocators.CART_BUTTON), "Product is not added to cart"
        print("Product is added to cart")

    def should_be_add_to_cart_notification(self):
        assert self.is_element_present(*ProductPageLocators.NOTIFICATION), "Add to cart notification is not present"
        print("Add to cart notification is present")

    def should_be_matching_product_names(self):
        assert self.browser.find_element(*ProductPageLocators.NOTIFICATION).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, "Product names do not match"
        print("Product names match")

    def should_be_matching_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.CART_COST).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, "Product price does not match the cart cost"
        print("Product price matches the cart cost")

    def should_not_be_success_message_after_time(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
        print("Success message is not presented")

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"
        print("Success message disappears")
