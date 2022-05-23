from .pages.source_page import SourcePage
from .pages.image_page import ImagePage


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
    image_page.should_be_image_open()
    first_picture = image_page.remember_picture()
    image_page.click_to_forward_icon()
    second_picture = image_page.remember_picture()
    image_page.should_be_different_pictures(first_picture, second_picture)
    image_page.click_to_backward_icon()
    first_picture_repeat = image_page.remember_picture()
    image_page.should_be_same_pictures(first_picture_repeat, first_picture)
