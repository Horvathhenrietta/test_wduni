import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Accordion(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Accordion/index.html")

    def test_accordions(self):
        # given
        btn_manual = self.driver.find_element(By.ID, "manual-testing-accordion")
        el_manual = self.driver.find_element(By.ID, "manual-testing-description")
        btn_cucumber = self.driver.find_element(By.ID, "cucumber-accordion")
        el_cucumber = self.driver.find_element(By.ID, "cucumber-testing-description")
        btn_automation = self.driver.find_element(By.ID, "automation-accordion")
        el_automation = self.driver.find_element(By.ID, "automation-testing-description")
        btn_click = self.driver.find_element(By.ID, "click-accordion")
        el_click = self.driver.find_element(By.ID, "timeout")
        # when
        btn_manual.click()
        btn_cucumber.click()
        btn_automation.click()
        btn_click.click()
        # then
        self.assertIn("active", btn_manual.get_attribute("class"))
        self.assertGreaterEqual("70px", el_manual.value_of_css_property("max-height"))
        self.assertIn("active", btn_cucumber.get_attribute("class"))
        self.assertGreaterEqual("50px", el_cucumber.value_of_css_property("max-height"))
        self.assertIn("active", btn_automation.get_attribute("class"))
        self.assertGreaterEqual("90px", el_automation.value_of_css_property("max-height"))
        time.sleep(5)
        self.assertIn("active", btn_click.get_attribute("class"))
        self.assertGreaterEqual("20px", el_click.value_of_css_property("max-height"))

    def tearDown(self) -> None:
        self.driver.quit()
