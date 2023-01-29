import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AjaxLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Ajax-Loader/index.html")

    def test_ajax_loader(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        loader = self.driver.find_element(By.ID, "loader")
        btn = self.driver.find_element(By.XPATH, "//span[@id='button1']/p")

        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@id='button1']/p")))
        btn.click()

    def tearDown(self) -> None:
        self.driver.quit()
