from .pages.source_page import SourcePage


def test_go_to_yandex(browser):
    link = "https://yandex.ru/"
    page = SourcePage(browser, link)
    page.open()
    page.should_be_source_line()
    page.enter_query()
    page.should_be_suggest()
    page.send_request()
    page.should_be_search_result()
    page.should_correct_url()



