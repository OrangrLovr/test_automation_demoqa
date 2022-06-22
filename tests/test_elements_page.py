from src.pages.check_box_page import ElementsCheckBoxPage
from src.pages.text_box_page import ElementsTextBoxPage

import pytest


@pytest.mark.new
def test_should_be_enter_data_user_into_the_text_field_box_page(driver):
    """
    The test enters user data into a text block.
    """
    link = "https://demoqa.com/text-box"
    page = ElementsTextBoxPage(driver, link)
    page.open()
    page.should_be_text_box_page_input_fields()
    page.should_be_enter_user_data_into_the_text_field_box_page()
    page.should_be_click_submit_in_btn_text_box_page()
    page.should_be_check_data_user_output()


def test_should_be_click_all_check_boxes(driver):
    """
    The test finds and checks the checkbox.
    """
    link = "https://demoqa.com/checkbox"
    page = ElementsCheckBoxPage(driver, link)
    page.open()
    page.should_be_check_box_page()
    page.should_be_success_click_all_check_box_via_rct_home()


@pytest.mark.new
@pytest.mark.xfail(reason="A dropped test going into x fail, to fix it, "
                          "you need to change the locator to the correct one")
def test_should_be_check_each_element_by_the_names_of_the_checkboxes(driver):
    """
    The test is initially a failure for demonstration.
    """
    link = "https://demoqa.com/checkbox"
    page = ElementsCheckBoxPage(driver, link)
    page.open()
    page.should_be_check_box_page()
    # dropped test
    page.should_be_click_rct_icon_expand_all_form_error()
