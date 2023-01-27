import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Click-Buttons/index.html")

    def test_webelement_click(self):
        self.driver.find_element(By.ID, "button1").click()
        modal = self.driver.find_element(By.ID, "myModalClick")
        self.assertTrue(modal)




    def tearDown(self) -> None:
        self.driver.quit()
