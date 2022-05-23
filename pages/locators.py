from selenium.webdriver.common.by import By


class SourcePageLocators():
    SOURCE_LINE = (By.CLASS_NAME, "input__control.input__input.mini-suggest__input")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    SOURCE_RESULT = (By.ID, "search-result")
    FIRST_LINK = (By.LINK_TEXT, "tensor.ru")

    IMAGES_LINK = (By.CLASS_NAME, "services-new__icon.services-new__icon_images")


class ImagePageLocators():
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item.PopularRequestList-Item_pos_0")
    CATEGORY_NAME = (By.XPATH, "//div/div[1]/a/div[2]")
    IMAGE_SOURCE_LINE = (By.CLASS_NAME, "mini-suggest__item.mini-suggest__item_type_fulltext.mini-suggest__item_personal_yes.mini-suggest__item_with-button")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item__thumb.justifier__thumb")
