import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Alerts(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Popup-Alerts/index.html")

    def test_js_alert(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        btn = self.driver.find_element(By.ID, "button1")
        # when
        btn.click()
        wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        # then
        self.assertEqual(alert.text, "I am an alert box!")

    def test_modal_popup(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        btn = self.driver.find_element(By.ID, "button2")
        modal = self.driver.find_element(By.ID, "myModal")
        # when
        btn.click()
        wait.until(EC.visibility_of_element_located((By.ID, "myModal")))
        # then
        self.assertEqual(modal.value_of_css_property("display"), "block")

    def tearDown(self) -> None:
        self.driver.quit()
