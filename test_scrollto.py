import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scrolling(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Scrolling/index.html")

    def test_scrolling_to_thumbnail(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        element = self.driver.find_element(By.XPATH, "//div[2]/div[@class='thumbnail']")
        a = ActionChains(self.driver)
        # when
        a.move_to_element(element).perform()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[2]/div[@class='thumbnail']"), "Well done"))
        # then
        self.assertEqual(element.text, "Well done for scrolling to me!")
        self.assertIn("rgb(26, 255, 26)", element.value_of_css_property("background"))

    def test_scrolling_to_counters(self):
        # given
        counter1 = self.driver.find_element(By.ID, "zone2")
        counter_text1 = self.driver.find_element(By.XPATH, "//div[@id='zone2']/h1")
        counter2 = self.driver.find_element(By.ID, "zone3")
        counter_text2 = self.driver.find_element(By.XPATH, "//div[@id='zone3']/h1")
        a = ActionChains(self.driver)
        # when
        a.move_to_element(counter1).perform()
        a.move_to_element(counter2).perform()
        # then
        self.assertEqual(counter_text1.text, "1 Entries")
        self.assertEqual(counter_text2.text, "1 Entries")

    def tearDown(self) -> None:
        self.driver.quit()
