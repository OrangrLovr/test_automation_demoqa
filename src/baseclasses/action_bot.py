from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ActionBot:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_element_visible(self, how, what, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))

    def are_elements_visible(self, how, what, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((how, what)))

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script('document.getElementById("fixedban").style.display="none"')

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def is_element_dissappeared(self, how, what, timeout=6):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located(
                (how, what)))
        except TimeoutError:
            return False
        return True

    def is_alert_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present(),
                                                      'Timed out waiting for PA creation ' +
                                                      'confirmation popup to appear.')
        except TimeoutException:
            return False
        return True

    def is_element_click(self, how, what):
        try:
            elem = self.driver.find_element(how, what)
            ActionChains(self.driver).click(elem).perform()
        except NoSuchElementException:
            return False
        return True

    def is_element_key_down_and_send_keys(self, system_button, key):
        try:
            ActionChains(self.driver)\
                .key_down(system_button)\
                .send_keys(key)\
                .key_up(key)\
                .perform()
        except NoSuchElementException:
            return False
        return True

    def is_element_key_down_and_key_up(self, system_button):
        try:
            ActionChains(self.driver)\
                .key_down(system_button)\
                .key_up(system_button)\
                .perform()
        except NoSuchElementException:
            return False
        return True

    def is_element_select(self, how, what, select_option, value):
        try:
            elem = self.driver.find_element(how, what)
            select = Select(elem)
            if select_option == "text":
                select.select_by_visible_text(value)
            elif select_option == "value":
                select.select_by_value(value)
            elif select_option == "index":
                select.select_by_index(value)
        except NoSuchElementException:
            return False
        return True

    def is_element_context_click(self, how, what):
        try:
            elem = self.driver.find_element(how, what)
            ActionChains(self.driver).context_click(elem).perform()
        except NoSuchElementException:
            return False
        return True

    def is_element_double_click(self, how, what):
        try:
            elem = self.driver.find_element(how, what)
            ActionChains(self.driver).double_click(elem).perform()
        except NoSuchElementException:
            return False
        return True

    def is_move_to_element(self, how, what):
        try:
            elem = self.driver.find_element(how, what)
            ActionChains(self.driver).move_to_element(elem).perform()
        except NoSuchElementException:
            return False
        return True

    def is_element_send_keys(self, how, what, text):
        try:
            elem = self.driver.find_element(how, what)
            action = ActionChains(self.driver)
            action.click(on_element=elem)
            action.send_keys(text)
            action.perform()
        except NoSuchElementException:
            return False
        return True

    def is_text_in_get_attribute(self, how, what, text, attr):
        try:
            text in self.driver.find_element(how, what).get_attribute(attr)
        except NoSuchElementException:
            return False
        return True

    def is_text_not_in_get_attribute(self, how, what, text, attr):
        try:
            text not in self.driver.find_element(how, what).get_attribute(attr)
        except NoSuchElementException:
            return False
        return True

    def is_equal_to_the_text_in_the_block_element(self, how, what, text):
        try:
            result = self.driver.find_element(how, what).text
            if result.lower() == text.lower():
                return True
        except NoSuchElementException:
            return False
