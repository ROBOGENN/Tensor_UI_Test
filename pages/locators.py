from selenium.webdriver.common.by import By


class SourcePageLocators:
    SOURCE_LINE = (By.CLASS_NAME, "input__control.input__input.mini-suggest__input")
    SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    SOURCE_RESULT = (By.ID, "search-result")
    FIRST_LINK = (By.LINK_TEXT, "tensor.ru")
    IMAGES_LINK = (By.CLASS_NAME, "services-new__icon.services-new__icon_images")


class ImagePageLocators:
    FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item.PopularRequestList-Item_pos_0")
    CATEGORY_NAME = (By.CLASS_NAME, "input__clear.mini-suggest__input-clear")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item__thumb.justifier__thumb")
    IMAGE_OPENED = (By.CLASS_NAME, "MMImage-Origin")
    FORWARD_ICON = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]")
    BACKWARD_ICON = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]")
