from itertools import product
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def put_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click(), "No button"

    def should_be_same_book(self):
        item = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        assert item.text == item_in_basket.text, "Item not in the basket"
        print(f"{item_in_basket.text} in the basket")

    def should_be_same_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price.text == price_in_basket.text, "Price incorrect in the basket"
        print(f"Price {price_in_basket.text} is correct")
