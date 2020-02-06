from locators.homepage_locators import HomepageLocators


class HomePage(object):

    def open_schedule_an_appointment_page(self):
        HomepageLocators.schedule_an_appointment.click()
