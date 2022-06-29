from selenium.webdriver import Keys

from src.baseclasses.action_bot import ActionBot
from src.locators.locators import FormPageLocators
from src.generator.user_form_generator import generated_person, generated_file


class FormPage(ActionBot):

    def fill_fields_and_submit_form_page(self):
        person = generated_person()
        path = generated_file()

        # remove footer
        self.remove_footer()

        # first name
        self.is_element_visible(*FormPageLocators.FIRST_NAME)
        self.is_element_send_keys(*FormPageLocators.FIRST_NAME, person.first_name)

        # last name
        self.is_element_visible(*FormPageLocators.LAST_NAME)
        self.is_element_send_keys(*FormPageLocators.LAST_NAME, person.last_name)

        # email
        self.is_element_visible(*FormPageLocators.EMAIL)
        self.is_element_send_keys(*FormPageLocators.EMAIL, person.email)

        # gender
        self.is_element_visible(*FormPageLocators.GENDER)
        self.is_element_click(*FormPageLocators.GENDER)

        # mobile
        self.is_element_visible(*FormPageLocators.MOBILE)
        self.is_element_send_keys(*FormPageLocators.MOBILE, person.mobile)

        # hobbies
        self.is_element_visible(*FormPageLocators.HOBBIES)
        self.is_element_click(*FormPageLocators.HOBBIES)

        # file input
        self.is_element_visible(*FormPageLocators.FILE_INPUT)
        self.is_element_send_keys(*FormPageLocators.FILE_INPUT, path)

        # current address
        self.is_element_visible(*FormPageLocators.CURRENT_ADDRESS)
        self.is_element_send_keys(*FormPageLocators.CURRENT_ADDRESS, person.current_address)

        # state
        self.is_element_click(*FormPageLocators.STATE)
        self.is_element_key_down_and_key_up(Keys.ENTER)

        # city
        self.is_element_click(*FormPageLocators.CITY)
        self.is_element_key_down_and_key_up(Keys.ENTER)

        # submit
        self.is_element_click(*FormPageLocators.SUBMIT)

        return person

    def result_form_page(self):

        # elements from the right column
        result_list = self.are_elements_visible(*FormPageLocators.RESULT_TABLES)

        # adding items to the list
        result_text = [i.text for i in result_list]
        # for i in result_list:
        #     result_text.append(i.text)

        return result_text
