import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ToDoList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/To-Do-List/index.html")

    def test_add_new_to_do(self):
        # given
        to_do_text = "test"
        self.input = self.driver.find_element(By.XPATH, "//input")
        # when
        self.input.send_keys(to_do_text + Keys.RETURN)
        # then
        self.assertTrue(to_do_text in self.driver.find_element(By.XPATH, "//li[4]").text)

    def test_delete_to_do(self):
        # given
        a = ActionChains(self.driver)
        container_el = self.driver.find_element(By.XPATH, "//ul")
        to_do_el = self.driver.find_elements(By.XPATH, "//li[1]")
        trash_el = self.driver.find_element(By.XPATH, "//li[1]/span/i")
        # when
        a.move_to_element(to_do_el[0]).perform()
        trash_el.click()
        to_do_el = self.driver.find_elements(By.XPATH, "//li[1]")

        # then
        self.assertTrue(to_do_el[0].text != " Go to potion class")

    def test_set_completed(self):
        # given
        to_do_el = self.driver.find_element(By.XPATH, "//li[1]")
        # when
        to_do_el.click()
        # then
        self.assertTrue("completed" in to_do_el.get_attribute("class"))

    def tearDown(self):
        self.driver.quit()
