from locators.checkoutpage_locators import CheckoutpageLocators
from selene.api import have, be, browser, s, by

# methods for Checkout page

class CheckoutPage(object):

    def check_form_header_is(self, text):
        CheckoutpageLocators.new_customer.should(have.text(text))

    def create_new_account(self, first_name, last_name, email, password):
        CheckoutpageLocators.agree_tos.click()
        CheckoutpageLocators.first_name.set(first_name)
        CheckoutpageLocators.last_name.set(last_name)
        CheckoutpageLocators.email.set(email)
        CheckoutpageLocators.password.set(password)
        CheckoutpageLocators.agree_tos.click()
        CheckoutpageLocators.create_an_account_and_continue.should(be.clickable).click()

    def check_errors_are(self, *errors):
        for el in list(zip(CheckoutpageLocators.form_errors, errors)):
            assert el[0].text == el[1]

    def check_tos_link_opens(self):
        CheckoutpageLocators.tos_link.click()
        browser.driver().switch_to.window(browser.driver().window_handles[1])
        assert 'about/terms-of-use' in browser.driver().current_url
        s(by.partial_text('TERMS OF USE')).should(be.visible)
        browser.driver().switch_to.window(browser.driver().window_handles[0])

    def check_policy_link_opens(self):
        CheckoutpageLocators.policy_link.click()
        browser.driver().switch_to.window(browser.driver().window_handles[2])
        assert 'about/privacy' in browser.driver().current_url
        browser.driver().switch_to.window(browser.driver().window_handles[0])