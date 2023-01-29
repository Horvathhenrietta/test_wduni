import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ActionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Actions/index.html#")

    def test_dropping(self):
        # given
        draggable_el = self.driver.find_element(By.ID, "draggable")
        droppable_el = self.driver.find_element(By.XPATH, "//div[@id='droppable']/p")
        a = ActionChains(self.driver)
        # when
        a.drag_and_drop(draggable_el, droppable_el)
        a.perform()
        # then
        self.assertEqual(droppable_el.value_of_css_property("background-color"), "rgba(244, 89, 80, 1)")

    def test_double_click(self):
        # given
        el = self.driver.find_element(By.ID, "double-click")
        a = ActionChains(self.driver)
        # when
        a.double_click(el)
        a.perform()
        # then
        self.assertIn("double", el.get_attribute("class"))
        self.assertEqual(el.value_of_css_property("background-color"), "rgba(147, 203, 90, 1)")

    def tearDown(self) -> None:
        self.driver.quit()
