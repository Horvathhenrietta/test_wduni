import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Login-Portal/index.html")

    def