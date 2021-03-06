from .base_page import BasePage
from .locators import SourcePageLocators
from selenium.webdriver.common.keys import Keys


class SourcePage(BasePage):
    def should_be_source_line(self):
        assert self.is_element_present(*SourcePageLocators.SOURCE_LINE), "Source line is not presented"

    def enter_query(self):
        source_line = self.browser.find_element(*SourcePageLocators.SOURCE_LINE)
        source_line.send_keys("тензор")

    def should_be_suggest(self):
        assert self.browser.find_element(*SourcePageLocators.SUGGEST), "Suggest is not presented"

    def send_request(self):
        source_line = self.browser.find_element(*SourcePageLocators.SOURCE_LINE)
        source_line.send_keys(Keys.ENTER)

    def should_be_search_result(self):
        assert self.browser.find_element(*SourcePageLocators.SOURCE_RESULT), "Source results is not presented"

    def should_be_correct_url(self):
        assert self.browser.find_element(*SourcePageLocators.FIRST_LINK), "First URL is not 'tensor.ru'"

    def should_image_link(self):
        assert self.browser.find_element(*SourcePageLocators.IMAGES_LINK), "'Images' link is not presented"

    def click_to_image_link(self):
        image_link = self.browser.find_element(*SourcePageLocators.IMAGES_LINK)
        image_link.click()
