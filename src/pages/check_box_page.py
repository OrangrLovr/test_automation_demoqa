from src.baseclasses.action_bot import ActionBot
from src.locators.locators import CheckBoxLocators


class ElementsCheckBoxPage(ActionBot):
    result_rct_icons = []
    verified_result = [
        "home",  "desktop", "notes", "commands", "documents", "workspace", "react",
        "angular", "veu", "office", "public", "private", "classified", "general",
        "downloads", "wordFile", "excelFile"
    ]

    def should_be_success_click_all_check_box_via_rct_home(self):
        self.should_be_click_rct_icon_expand_all_form()
        self.should_be_click_rct_title_home()
        self.should_be_check_success_display_result()
        self.should_be_click_rct_icon_collapse_all_form()

    # A dropped test going into x fail, to fix it, you need to change the locator to the correct one
    def should_be_click_rct_icon_expand_all_form_error(self):
        assert self.is_element_click(*CheckBoxLocators.RCT_ICON_EXPAND_ALL_ERROR), "Dropped test going into x fail"

    def should_be_click_rct_icon_expand_all_form(self):
        assert self.is_element_click(*CheckBoxLocators.RCT_ICON_EXPAND_ALL), "RCT Expand all not found"

    def should_be_click_rct_icon_collapse_all_form(self):
        assert self.is_element_click(*CheckBoxLocators.RCT_ICON_COLLAPSE_ALL), "RCT Collapse all not found"

    def should_be_click_rct_title_home(self):
        assert self.is_text_in_get_attribute(*CheckBoxLocators.RCT_ICON_HOME, "uncheck", "class"), \
            "text not in get attr"
        assert self.is_element_click(*CheckBoxLocators.RCT_ICON_HOME), "rct title home not click"
        assert self.is_text_not_in_get_attribute(*CheckBoxLocators.RCT_ICON_HOME, "uncheck", "class"), \
            "text in get attr"

    def should_be_check_success_display_result(self):
        for result in range(17):
            result = self.driver.find_element(*CheckBoxLocators.RESULT_RCT_ICONS).text
            self.result_rct_icons.append(result)

        assert len(self.result_rct_icons) == 17, "Incorrect number of check boxes"
        assert self.verified_result.sort() == self.result_rct_icons.sort(), \
            "The verified list is not identical to the result"

    def should_be_check_box_page(self):
        self.should_be_check_box_url()
        self.should_be_rct_icon_collapse_all_form()
        self.should_be_rct_icon_expand_all_form()
        self.should_be_rct_icon_uncheck_form()
        self.should_be_rct_title_form()

    def should_be_check_box_url(self):
        assert "checkbox" in self.driver.current_url, "'checkbox' not in current url"

    def should_be_rct_icon_collapse_all_form(self):
        assert self.is_element_present(*CheckBoxLocators.RCT_ICON_COLLAPSE_ALL), "RCT icon collapse all form not found"

    def should_be_rct_icon_expand_all_form(self):
        assert self.is_element_present(*CheckBoxLocators.RCT_ICON_EXPAND_ALL), "RCT icon expand all form not found"

    def should_be_rct_icon_uncheck_form(self):
        assert self.is_element_present(*CheckBoxLocators.RCT_ICON_UNCHECK), "RCT icon uncheck form not found"

    def should_be_rct_title_form(self):
        assert self.is_element_present(*CheckBoxLocators.RCT_ICON_HOME), "RCT title form not found"
