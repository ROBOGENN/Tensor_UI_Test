from .base_page import BasePage
from .locators import ImagePageLocators


class ImagePage(BasePage):
    def should_be_correct_url(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        assert "https://yandex.ru/images/" in self.browser.current_url, "This URL is not 'https://yandex.ru/images/'"

    def click_to_first_category(self):
        first_category = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY)
        first_category.click()

    def should_be_source_image_request(self):
        assert self.browser.find_element(*ImagePageLocators.CATEGORY_NAME), "This category is not presented in search-line"

    def go_to_first_picture(self):
        first_picture = self.browser.find_element(*ImagePageLocators.FIRST_IMAGE)
        first_picture.click()

    def should_be_image_open(self):
        assert self.browser.find_element(*ImagePageLocators.IMAGE_OPENED), "Image is not presented"

    def click_to_forward_icon(self):
        forward_icon = self.browser.find_element(*ImagePageLocators.FORWARD_ICON)
        forward_icon.click()

    def remember_picture(self):
        picture = self.browser.find_element(*ImagePageLocators.IMAGE_OPENED)
        picture_src = picture.get_attribute("src")
        return picture_src

    def should_be_different_pictures(self, first_picture, second_picture):
        assert first_picture != second_picture, "Pictures are not different"

    def click_to_backward_icon(self):
        backward_icon = self.browser.find_element(*ImagePageLocators.BACKWARD_ICON)
        backward_icon.click()

    def should_be_same_pictures(self, firs_picture, second_picture):
        """
        ДОДЕЛАТЬ СЕЙЧАС!!!
        """
        assert firs_picture == second_picture, "Pictures are not same"
