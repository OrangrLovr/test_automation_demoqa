from configuration import URL_DEMOQA
from src.pages.form_page import FormPage

import pytest
import allure


class TestFormPage:

    @allure.step
    @allure.title("!!!The test fills out the registration form (is under development).")
    @pytest.mark.general_tests
    def test_should_be_fill_fields_and_submit_form_page(self, driver):
        """The test is under development.

            Check exists:
            - there is an input field "first name";
            - there is an input field "last name";
            - there is an input field "email";
            - there is a radio button "gender";
            - there is an input field "mobile";
            - there is a check boxes "hobbies";
            - there is an input field "current address";
            - there is a selector "state and city"

            Not verified:
            - field "date of birth";
            - field "subjects";
            - field "select picture"
        """
        link = f"{URL_DEMOQA}automation-practice-form"
        form_page = FormPage(driver, link)
        form_page.open()
        person = form_page.fill_fields_and_submit_form_page()
        result = form_page.result_form_page()

        assert f'{person.first_name} {person.last_name}' == result[0], \
            'the first and last name form has not been filled'

        assert person.email == result[1], \
            'the email form has not been filled'

        assert len(result[3]) == 10, \
            'the mobile form has incorrect format'
        assert str(person.mobile) == result[3], \
            'the mobile form has not been filled'
