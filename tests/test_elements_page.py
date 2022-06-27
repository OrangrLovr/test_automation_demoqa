import allure

from configuration import URL_DEMOQA
from src.pages.check_box_page import ElementsCheckBoxPage
from src.pages.text_box_page import ElementsTextBoxPage
from src.pages.radio_button_page import \
    CheckElementsRadioButtonPage, YesElementRadioButtonPage, ImpressiveElementRadioButtonPage, NoElementRadioButtonPage

import pytest


@allure.step
@pytest.mark.new
def test_should_be_enter_data_user_into_the_text_field_box_page(driver):
    """
    The test enters user data into a text block.
    """
    link = f"{URL_DEMOQA}text-box"
    page = ElementsTextBoxPage(driver, link)
    page.open()
    page.should_be_text_box_page_input_fields()
    page.should_be_enter_user_data_into_the_text_field_box_page()
    page.should_be_click_submit_in_btn_text_box_page()
    page.should_be_check_data_user_output()


@allure.step
@pytest.mark.new
def test_should_be_click_all_check_boxes(driver):
    """
    The test finds and checks the checkbox.
    """
    link = f"{URL_DEMOQA}checkbox"
    page = ElementsCheckBoxPage(driver, link)
    page.open()
    page.should_be_check_box_page()
    page.should_be_success_click_all_check_box_via_rct_home()


@allure.step
@pytest.mark.xfail(reason="A dropped test going into x fail, to fix it, "
                          "you need to change the locator to the correct one")
def test_should_be_check_each_element_by_the_names_of_the_checkboxes(driver):
    """
    The test is initially a failure for demonstration.
    """
    link = f"{URL_DEMOQA}checkbox"
    page = ElementsCheckBoxPage(driver, link)
    page.open()
    page.should_be_check_box_page()
    # dropped test
    page.should_be_click_rct_icon_expand_all_form_error()


@allure.story('full_check_the_radio_button_no')
@allure.description("""
The test includes checking the radio button elements.
Elements: "Yes" button, "Impressive" button, "No" button, block with successful text output.
""")
@pytest.mark.general_tests
def test_should_be_check_the_existence_all_radio_buttons(driver):
    """
    Check exists:

    - link address is correct;
    - is there a radio button 'yes';
    - is there a radio button 'impressive';
    - is there a radio button 'no';
    - is there a block with a successful text has appeared (it shouldn't be).
    """
    link = f"{URL_DEMOQA}radio-button"
    page = CheckElementsRadioButtonPage(driver, link)
    page.open()
    page.should_be_check_elements_radio_button_page()


@pytest.mark.single_element_tests
def test_should_be_success_click_on_the_yes_radio_button(driver):
    """
    Check exists:

    - the operation of the radio button;
    - click on an element;
    - the elements is selected;
    - the output result 'yes' of the "successful message".
    """
    link = f"{URL_DEMOQA}radio-button"
    page = YesElementRadioButtonPage(driver, link)
    page.open()
    page.should_be_success_click_on_the_yes_radio_button()


@allure.title("Test to check a successful click on the impressive radio button.")
@pytest.mark.single_element_tests
def test_should_be_success_click_on_the_impressive_radio_button(driver):
    """
    Check exists:

    - the operation of the radio button;
    - click on an element;
    - the elements is selected;
    - the output result 'impressive' of the "successful message".
    """
    link = f"{URL_DEMOQA}radio-button"
    page = ImpressiveElementRadioButtonPage(driver, link)
    page.open()
    page.should_be_success_click_on_the_impressive_radio_button()


@allure.step
@allure.story('full_check_the_radio_button_no')
@allure.link('https://demoqa.com/radio-button', name='Link with inactive radio button "no"')
@pytest.mark.single_element_tests
def test_should_be_not_success_click_on_the_no_radio_button(driver):
    """
    Check exists:

    - the operation of the radio button;
    - the element is not selected.
    """
    link = f"{URL_DEMOQA}radio-button"
    page = NoElementRadioButtonPage(driver, link)
    page.open()
    page.should_be_not_success_click_on_the_no_radio_button()
