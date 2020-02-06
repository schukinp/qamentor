from selene.api import s, by, browser, have
import uuid


def element_with_text(text):
    return s(by.text(text))

def check_if_current_url_is(url):
    if browser.driver().current_url == url:
        pass
    else:
        browser.open_url(url)

def generate_email():
    return "{}".format(str(uuid.uuid4()))[:10] + '@example.com'

def check_page_title_is(title):
    s('h1').should(have.text(title))
