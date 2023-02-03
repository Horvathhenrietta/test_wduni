import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_conditions import element_has_css_class


class HiddenElements(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Hidden-Elements/index.html")
        self.wait = WebDriverWait(self.driver, 10)

    def test_not_displayed(self):
        # given
        element_not_displayed = self.driver.find_element(By.ID, "not-displayed")
        modal = self.driver.find_element(By.ID, "myModalClick")
        modal_close_btn = self.driver.find_element(By.XPATH,
                                                   "//div[@id='myModalClick']//div[@class='modal-footer']/button[@type='button']")
        # when
        self.driver.execute_script("arguments[0].style.display = 'block';", element_not_displayed)
        self.wait.until(EC.element_to_be_clickable((By.ID, "button1"))).click()
        self.wait.until(element_has_css_class((By.ID, "myModalClick"), "in"))
        # then
        self.assertEqual(modal.value_of_css_property("display"), "block")
        modal_close_btn.click()

    def test_visibility_hidden(self):
        # given
        element_not_visible = self.driver.find_element(By.ID, "visibility-hidden")
        modal_close_btn = self.driver.find_element(By.XPATH,
                                                   "//div[@id='myModalJSClick']//div[@class='modal-footer']/button[@type='button']")
        modal = self.driver.find_element(By.ID, "myModalJSClick")
        # when
        self.driver.execute_script("arguments[0].style.visibility = 'visible'", element_not_visible)
        self.wait.until(EC.element_to_be_clickable((By.ID, "button2"))).click()
        self.wait.until(element_has_css_class((By.ID, "myModalJSClick"), "in"))
        # then
        self.assertEqual(modal.value_of_css_property("display"), "block")
        modal_close_btn.click()

    def test_opacity_0_percent(self):
        # given
        element_not_visible = self.driver.find_element(By.ID, "zero-opacity")
        modal = self.driver.find_element(By.ID, "myModalMoveClick")
        modal_close_btn = self.driver.find_element(By.XPATH,
                                                   "//div[@id='myModalMoveClick']//div[@class='modal-footer']/button[@type='button']")
        # when
        self.driver.execute_script("arguments[0].style.opacity = '100'", element_not_visible)
        self.wait.until(EC.element_to_be_clickable((By.ID, "button3"))).click()
        self.wait.until(element_has_css_class((By.ID, "myModalMoveClick"), "in"))
        # then
        self.assertEqual(modal.value_of_css_property("display"), "block")
        modal_close_btn.click()

    def tearDown(self) -> None:
        self.driver.quit()
