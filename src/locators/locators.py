from selenium.webdriver.common.by import By
from random import randint


class TextBoxLocators:
    # data user
    FULL_NAME_FORM = (By.CSS_SELECTOR, "#userName")
    EMAIL_FORM = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS_FORM = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS_FORM = (By.CSS_SELECTOR, "#permanentAddress")
    SUBMIT_TEXT_BOX_BTN = (By.CSS_SELECTOR, "#submit")

    # registered user data
    REGISTERED_FULL_NAME_FORM = (By.CSS_SELECTOR, "#name.mb-1")
    REGISTERED_EMAIL_FORM = (By.CSS_SELECTOR, "#email.mb-1")
    REGISTERED_CURRENT_ADDRESS_FORM = (By.CSS_SELECTOR, "#currentAddress.mb-1")
    REGISTERED_PERMANENT_ADDRESS_FORM = (By.CSS_SELECTOR, "#permanentAddress.mb-1")


class CheckBoxLocators:
    RCT_ICON_COLLAPSE_ALL = (By.CSS_SELECTOR, ".rct-icon.rct-icon-collapse-all")
    RCT_ICON_EXPAND_ALL = (By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-all")
    RCT_ICON_UNCHECK = (By.CSS_SELECTOR, ".rct-icon.rct-icon-uncheck")
    DISPLAY_RESULT = (By.CSS_SELECTOR, "#result")
    RCT_ICON_HOME = (By.CSS_SELECTOR, "label[for='tree-node-home']")
    RESULT_RCT_ICONS = (By.CSS_SELECTOR, ".text-success")

    # react icon expand with error
    RCT_ICON_EXPAND_ALL_ERROR = (By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-all-error")


class RadioButtonLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "input#yesRadio")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "input#impressiveRadio")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "input#noRadio")

    # emerge successful test
    RADIO_BUTTON_TEXT_SUCCESS_FORM = (By.CSS_SELECTOR, "span.text-success")


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, "input#userNumber")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input#dateOfBirthInput")
    SUBJECT = (By.XPATH, "//input[@id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "input#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    STATE = (By.CSS_SELECTOR, "div#state")
    CITY = (By.CSS_SELECTOR, "div#city")
    SUBMIT = (By.CSS_SELECTOR, "button#submit")

    # emerge results table
    RESULT_TABLES = (By.XPATH, "//div[@class='table-responsive']//td[2]")
