import time

from .pages.source_page import SourcePage, ImagePage

"""
def test_yandex_search(browser):
    link = "https://yandex.ru/"
    page = SourcePage(browser, link)
    page.open()
    page.should_be_source_line()
    page.enter_query()
    page.should_be_suggest()
    page.send_request()
    page.should_be_search_result()
    page.should_be_correct_url()

"""
def test_yandex_image(browser):
    link = "https://yandex.ru/"
    page = SourcePage(browser, link)
    page.open()
    page.should_image_link()
    page.click_to_image_link()
    image_page = ImagePage(browser, link)
    image_page.should_be_correct_url()
    image_page.click_to_first_category()
    image_page.should_be_source_image_request()
    image_page.go_to_first_picture()

    time.sleep(5)


