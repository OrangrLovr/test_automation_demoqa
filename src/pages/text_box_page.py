from src.generator.data_user import TextBoxDataUser
from src.locators.locators import TextBoxLocators
from src.baseclasses.action_bot import ActionBot


class ElementsTextBoxPage(ActionBot):

    def should_be_check_data_user_output(self):
        self.should_be_output_full_name_the_text_box_page()
        self.should_be_output_email_the_text_box_page()
        self.should_be_output_current_address_the_text_box_page()
        self.should_be_output_permanent_address_the_text_box_page()

    def should_be_output_full_name_the_text_box_page(self):
        msg = self.driver.find_element(*TextBoxLocators.REGISTERED_FULL_NAME_FORM).text
        assert len(msg) != 0, "The user's data full name has not been registered"
        assert TextBoxDataUser.FULL_NAME_DATA_USER in msg, "Full name not registered"

    def should_be_output_email_the_text_box_page(self):
        msg = self.driver.find_element(*TextBoxLocators.REGISTERED_EMAIL_FORM).text
        assert len(msg) != 0, "The user's data email has not been registered"
        assert TextBoxDataUser.EMAIL_DATA_USER in msg, "Email not registered"

    def should_be_output_current_address_the_text_box_page(self):
        msg = self.driver.find_element(*TextBoxLocators.REGISTERED_CURRENT_ADDRESS_FORM).text
        assert len(msg) != 0, "The user's data current address has not been registered"
        assert TextBoxDataUser.CURRENT_ADDRESS_DATA_USER in msg, "Current address not registered"

    def should_be_output_permanent_address_the_text_box_page(self):
        msg = self.driver.find_element(*TextBoxLocators.REGISTERED_PERMANENT_ADDRESS_FORM).text
        assert len(msg) != 0, "The user's data permanent address has not been registered"
        assert TextBoxDataUser.PERMANENT_ADDRESS_DATA_USER in msg, "Permanent address not registered"

    def should_be_click_submit_in_btn_text_box_page(self):
        self.is_element_click(*TextBoxLocators.SUBMIT_TEXT_BOX_BTN), "Do not button click submit"

    def should_be_enter_user_data_into_the_text_field_box_page(self):
        self.should_be_enter_full_name_into_the_text_field_box_page()
        self.should_be_enter_email_into_the_text_field_box_page()
        self.should_be_enter_current_address_into_the_text_field_box_page()
        self.should_be_enter_permanent_address_into_the_text_field_box_page()

    def should_be_enter_full_name_into_the_text_field_box_page(self):
        assert self.is_element_send_keys(*TextBoxLocators.FULL_NAME_FORM, TextBoxDataUser.FULL_NAME_DATA_USER), \
            "Do not enter user data into the full name field"

    def should_be_enter_email_into_the_text_field_box_page(self):
        assert self.is_element_send_keys(*TextBoxLocators.EMAIL_FORM, TextBoxDataUser.EMAIL_DATA_USER), \
            "Do not enter user data into the email field"

    def should_be_enter_current_address_into_the_text_field_box_page(self):
        assert self.is_element_send_keys(*TextBoxLocators.CURRENT_ADDRESS_FORM, TextBoxDataUser.CURRENT_ADDRESS_DATA_USER), \
            "Do not enter user data into the current address field"

    def should_be_enter_permanent_address_into_the_text_field_box_page(self):
        assert self.is_element_send_keys(*TextBoxLocators.PERMANENT_ADDRESS_FORM, TextBoxDataUser.PERMANENT_ADDRESS_DATA_USER), \
            "Do not enter user data into the permanent address field"

    def should_be_text_box_page_input_fields(self):
        self.should_be_text_box_url()
        self.should_be_full_name_form()
        self.should_be_email_form()
        self.should_be_current_address_form()
        self.should_be_permanent_address_form()
        self.should_be_submit_text_box_btn()

    def should_be_text_box_url(self):
        assert "text-box" in self.driver.current_url, "'text_box' not in current url"

    def should_be_full_name_form(self):
        assert self.is_element_present(*TextBoxLocators.FULL_NAME_FORM), "Full name form not found"

    def should_be_email_form(self):
        assert self.is_element_present(*TextBoxLocators.EMAIL_FORM), "Email form not found"

    def should_be_current_address_form(self):
        assert self.is_element_present(*TextBoxLocators.CURRENT_ADDRESS_FORM), "Current address form not found"

    def should_be_permanent_address_form(self):
        assert self.is_element_present(*TextBoxLocators.PERMANENT_ADDRESS_FORM), "Permanent address form not found"

    def should_be_submit_text_box_btn(self):
        assert self.is_element_present(*TextBoxLocators.SUBMIT_TEXT_BOX_BTN), "Submit text box btn not found"
