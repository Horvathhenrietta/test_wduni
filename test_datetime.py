from datetime import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DatePicking(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Datepicker/index.html")

    def test_datepicker(self):
        # given
        nth_of_day = 10
        expected = datetime.now().strftime(f"%m-{nth_of_day + 1}-%Y")
        wait = WebDriverWait(self.driver, 10)
        datepicker_el = self.driver.find_element(By.ID, "datepicker")
        date_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        # when
        datepicker_el.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".datepicker-orient-left")))
        days = self.driver.find_elements(By.CSS_SELECTOR, ".datepicker-days .day:not(.old, .new)")
        days[nth_of_day].click()
        # then
        self.assertEqual(expected, date_input.get_attribute("value"))

    def tearDown(self) -> None:
        self.driver.quit()
