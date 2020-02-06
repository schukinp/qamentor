from selene.api import s, browser, by


class CheckoutpageLocators(object):

        sign_in = s('button[class*="LoginBTN"]')
        new_customer = s('.title_underline.margin-bottom-medium')
        create_an_account = s('.create-account-btn.button-medium-solid-bst-blue')
        continue_as_guest = s('button[class*="guest-continue-btn"]')
        first_name = s('#firstName')
        last_name = s('#lastName')
        email = s('#email')
        password = s('#createPassword')
        agree_tos = s('label[for="agreeTermsAndConditions"]')
        create_an_account_and_continue = s('a[class*="registrationBTN"]')
        form_errors = browser.all('.parsley-required')
        tos_link = s(by.partial_text('Terms of Use'))
        policy_link = s(by.partial_text('Privacy Policy'))
        cancel = s('.cancel-btn.button-large-transparent-bst-blue.cancel')
