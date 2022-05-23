from .pages.source_page import SourcePage


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

