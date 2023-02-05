import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoComplete(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")
    
    def test_autocomplete_avocado(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        search_query = "avacado"
        search_field = self.driver.find_element(By.ID, "myInput")
        # when
        search_field.send_keys(search_query[:2])
        wait.until(EC.visibility_of_element_located((By.ID, "myInputautocomplete-list")))
        autocomplete_list = self.driver.find_element(By.ID, "myInputautocomplete-list")
        # then
        self.assertIn(search_query, autocomplete_list.text.lower())
    
    def tearDown(self) -> None:
        self.driver.quit()