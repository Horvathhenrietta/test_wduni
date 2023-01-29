import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CheckboxesRadioButtonsDropdowns(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

    def test_dropdowns(self):
        # given
        el_dropdown = list(
            map(Select, self.driver.find_elements(By.XPATH, "//div[2]//div[@class='section-title']/select")))
        # when
        el_dropdown[0].select_by_visible_text("Python")
        el_dropdown[1].select_by_visible_text("Maven")
        el_dropdown[2].select_by_visible_text("JavaScript")
        # then

    def test_checkboxes(self):
        # given
        options = self.driver.find_elements(By.XPATH, "//div[@id='checkboxes']//input")
        for check in options:
            check.click()

    def test_radio_buttons(self):
        btns = self.driver.find_elements(By.XPATH, "//form[@id='radio-buttons']/input")
        for btn in btns:
            btn.click()

    def tearDown(self) -> None:
        self.driver.quit()
