from selenium.webdriver.common.by import By


class SourcePageLocators():
    SOURCE_LINE = (By.CLASS_NAME, "input__control.input__input.mini-suggest__input")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    SOURCE_RESULT = (By.ID, "search-result")
    FIRST_LINK = (By.LINK_TEXT, "tensor.ru")
