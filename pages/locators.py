from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@value='Add to basket']")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,'.col-sm-6>.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR,'.alert-info .alertinner strong')
