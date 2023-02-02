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
        alert.accept()

    def test_modal_popup(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        btn = self.driver.find_element(By.ID, "button2")
        modal = self.driver.find_element(By.ID, "myModal")
        close_btn = self.driver.find_element(By.XPATH, "///button[@innertext='Close']")
        # when
        btn.click()
        wait.until(EC.visibility_of_element_located((By.ID, "myModal")))
        # then
        self.assertEqual(modal.value_of_css_property("display"), "block")
        close_btn.click()

    def test_js_confirm_box_accept(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        btn = self.driver.find_element(By.ID, "button4")
        confirm_alert_p = self.driver.find_element(By.ID, "confirm-alert-text")
        # when
        btn.click()
        wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert.accept()
        # then
        self.assertEqual(confirm_alert_p.text, "You pressed OK!")

    def test_js_confirm_box_cancel(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        btn = self.driver.find_element(By.ID, "button4")
        confirm_alert_p = self.driver.find_element(By.ID, "confirm-alert-text")
        # when
        btn.click()
        wait.until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert.dismiss()
        # then
        self.assertEqual(confirm_alert_p.text, "You pressed Cancel!")

    def tearDown(self) -> None:
        self.driver.quit()
