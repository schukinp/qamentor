from helper import check_if_current_url_is, check_page_title_is
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from locators.checkoutpage_locators import CheckoutpageLocators
from selene.api import be
import pytest
from helper import generate_email


@pytest.mark.usefixtures('open_base_url')
class TestScheduleAnAppointment(object):
    # BST- Verify Schedule Appointment link on Home page
    def test_verify_schedule_appointment_link_on_homepage(self, set_base_url):
        check_if_current_url_is(set_base_url)
        HomePage().open_schedule_an_appointment_page()
        CheckoutpageLocators.sign_in.should(be.visible)
        CheckoutpageLocators.continue_as_guest.should(be.visible)
        CheckoutpageLocators.create_an_account.should(be.visible)
        CheckoutPage().check_form_header_is('NEW CUSTOMERS')

    # BST - Verify Schedule Appointment - Create Account (item 1)
    def test_cannot_register_without_mandatory_fields(self, set_base_url):
        check_if_current_url_is(set_base_url + 'brgtconsumerstorefront/checkout/interstitial')
        CheckoutpageLocators.create_an_account.click()
        CheckoutpageLocators.agree_tos.click()
        CheckoutpageLocators.create_an_account_and_continue.should(be.enabled).click()
        CheckoutPage().check_errors_are('Please enter your first name.',
                                        'Please enter your last name.',
                                        'Please enter a valid email.',
                                        'Your password must be at least 8 characters and contain at least 1 number, '
                                        '1 upper case letter, 1 lower case letter, and 1 special character (# not '
                                        'allowed)')
        CheckoutpageLocators.cancel.click()

    # BST - Verify Schedule Appointment - Create Account (item 2)
    def test_cannot_register_with_existing_email(self, set_base_url):
        check_if_current_url_is(set_base_url + 'brgtconsumerstorefront/checkout/interstitial')
        CheckoutpageLocators.create_an_account.click()
        CheckoutPage().create_new_account('test', 'test', 'test@example.com', '!Qwer4321')
        CheckoutPage().check_errors_are('An account has already been created with this email address.')

    # BST - Verify Schedule Appointment - Create Account (item 3)
    def test_terms_of_use_and_privacy_policy_pages_clickable(self, set_base_url):
        check_if_current_url_is(set_base_url + 'brgtconsumerstorefront/checkout/interstitial')
        CheckoutpageLocators.tos_link.should(be.clickable)
        CheckoutpageLocators.policy_link.should(be.clickable)

    # BST - Verify Schedule Appointment - Create Account (item 4)
    def test_create_account_success(self, set_base_url):
        check_if_current_url_is(set_base_url + 'brgtconsumerstorefront/checkout/interstitial')
        CheckoutPage().create_new_account('test', 'test', generate_email(), '!Qwer4321')
        check_page_title_is('FIND A STORE')
