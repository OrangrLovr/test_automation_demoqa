from src.baseclasses.action_bot import ActionBot
from src.locators.locators import RadioButtonLocators


class CheckElementsRadioButtonPage(ActionBot):

    def should_be_check_elements_radio_button_page(self):
        self.should_be_radio_button_url()
        self.should_be_radio_button_yes_form()
        self.should_be_radio_button_impressive_form()
        self.should_be_radio_button_no_form()
        self.should_not_be_radio_button_text_success_form()

    def should_be_radio_button_url(self):
        """Check if the link address is correct."""
        assert "radio-button" in self.driver.current_url, \
            "'radio-button' not in current url"

    def should_be_radio_button_yes_form(self):
        """Check if there is a radio button 'yes'."""
        assert self.is_element_present(*RadioButtonLocators.RADIO_BUTTON_YES), \
            "radio btn 'yes' form not found"

    def should_be_radio_button_impressive_form(self):
        """Check if there is a radio button 'impressive'."""
        assert self.is_element_present(*RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE), \
            "radio btn 'impressive' form not found"

    def should_be_radio_button_no_form(self):
        """Check if there is a radio button 'no'."""
        assert self.is_element_present(*RadioButtonLocators.RADIO_BUTTON_NO), \
            "radio btn 'no' form not found"

    def should_not_be_radio_button_text_success_form(self):
        """Check if a block with a successful text has appeared."""
        assert self.is_not_element_present(*RadioButtonLocators.RADIO_BUTTON_TEXT_SUCCESS_FORM), \
            "text success form found"


class YesElementRadioButtonPage(ActionBot):

    def should_be_success_click_on_the_yes_radio_button(self):
        self.should_be_check_able_radio_button_yes_form()
        self.should_be_click_radio_button_yes_form()
        self.should_be_check_is_selected_radio_button_yes_form()
        self.should_be_radio_button_yes_text_success_form()

    def should_be_check_able_radio_button_yes_form(self):
        """ Check the operation of the radio button:

            - 'disabled' is False # the button is functional
            - 'disabled' is True # the button is not functional

            Radio button 'yes' must be False.
        """
        assert self.driver.execute_script("return document.getElementById('yesRadio').disabled") is False, \
            "radio button 'yes' form is not False"

    def should_be_click_radio_button_yes_form(self):
        """ Click on an element."""
        assert self.is_element_click(*RadioButtonLocators.RADIO_BUTTON_YES), \
            "radio button 'yes' form don't click"

    def should_be_check_is_selected_radio_button_yes_form(self):
        """ Check if the element is selected.

            Radio button select 'yes' must be True.
        """
        assert self.driver.find_element(*RadioButtonLocators.RADIO_BUTTON_YES).is_selected() is True, \
            "radio button 'yes' form is not selected"

    def should_be_radio_button_yes_text_success_form(self):
        """ Check the output result of the "successful message"."""
        assert self.is_equal_to_the_text_in_the_block_element(*RadioButtonLocators.RADIO_BUTTON_TEXT_SUCCESS_FORM,
                                                              "YES"), "Success text not equal 'yes'"


class ImpressiveElementRadioButtonPage(ActionBot):

    def should_be_success_click_on_the_impressive_radio_button(self):
        self.should_be_check_able_radio_button_impressive_form()
        self.should_be_click_radio_button_impressive_form()
        self.should_be_check_is_selected_radio_button_impressive_form()
        self.should_be_radio_button_impressive_text_success_form()

    def should_be_check_able_radio_button_impressive_form(self):
        """ Check the operation of the radio button:

            - 'disabled' is False # the button is functional
            - 'disabled' is True # the button is not functional

            Radio button 'impressive' must be False.
        """
        assert self.driver.execute_script("return document.getElementById('impressiveRadio').disabled") is False, \
            "radio button 'impressive' form is not False"

    def should_be_click_radio_button_impressive_form(self):
        """ Click on an element."""
        assert self.is_element_click(*RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE), \
            "radio button 'impressive' form don't click"

    def should_be_check_is_selected_radio_button_impressive_form(self):
        """ Check if the element is selected.

            Radio button select 'impressive' must be True.
        """
        assert self.driver.find_element(*RadioButtonLocators.RADIO_BUTTON_IMPRESSIVE).is_selected() is True, \
            "radio button 'impressive' form is not selected"

    def should_be_radio_button_impressive_text_success_form(self):
        """ Check the output result of the "successful message"."""
        assert self.is_equal_to_the_text_in_the_block_element(*RadioButtonLocators.RADIO_BUTTON_TEXT_SUCCESS_FORM,
                                                              "IMPRESSIVE"), "Success text not equal 'impressive'"


class NoElementRadioButtonPage(ActionBot):

    def should_be_not_success_click_on_the_no_radio_button(self):
        self.should_be_check_disable_radio_button_no_form()
        self.should_be_check_is_not_selected_radio_button_no_form()

    def should_be_check_disable_radio_button_no_form(self):
        """Check the operation of the radio button:

            - 'disabled' is False # the button is functional
            - 'disabled' is True # the button is not functional

            Radio button 'no' must be True.
        """
        assert self.driver.execute_script("return document.getElementById('noRadio').disabled") is True, \
            "radio button 'no' form is not True"

    def should_be_check_is_not_selected_radio_button_no_form(self):
        """ The dropped test.
            The radio button "No" is not active!

            Radio button select 'no' must be True.
        """
        assert self.driver.find_element(*RadioButtonLocators.RADIO_BUTTON_NO).is_selected() is True, \
            "radio button 'no' form is not selected"
