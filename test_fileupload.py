import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from os import remove

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FileUpload(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/File-Upload/index.html")

    def test_fileupload(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        filepath = "C:/Users/T560/PycharmProjects/webdriveruni/myfile.txt"
        file = open(filepath, "x")
        file.close()
        el_input = self.driver.find_element(By.ID, "myFile")
        btn_submit = self.driver.find_element(By.ID, "submit-button")
        alert = Alert(self.driver)
        # when
        el_input.send_keys(filepath)
        btn_submit.click()
        wait.until(EC.alert_is_present())
        # then
        self.assertEqual(alert.text, "Your file has now been uploaded!")
        remove(filepath)

    def tearDown(self) -> None:
        self.driver.quit()
