import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_conditions import element_has_css_class


class Iframes(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/IFrame/index.html")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame")))

    def test_titles(self):
        # given
        elements = self.driver.find_elements(By.XPATH, "//p[@class='sub-heading']")
        # when
        # then
        self.assertEqual(elements[0].text, "Who Are We?")
        self.assertEqual(elements[1].text, "GREAT SERVICE!")
        self.assertEqual(elements[2].text, "Why Choose Us?")
        self.assertEqual(elements[3].text, "Excellent Customer Service!")

    def test_findoutmore_open(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        button = self.driver.find_element(By.XPATH, '//button[@id="button-find-out-more"]')
        # when
        button.click()
        # then
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, 'myModal'))))

    def test_findoutmore_close(self):
        # given
        wait = WebDriverWait(self.driver, 10)
        close_btn_xpath = "//div[@class='modal-footer']/button[1]"
        self.driver.find_element(By.XPATH, '//button[@id="button-find-out-more"]').click()
        close_btn = self.driver.find_element(By.XPATH, close_btn_xpath)
        # when
        wait.until(EC.element_to_be_clickable((By.XPATH, close_btn_xpath)))
        close_btn.click()
        # then
        self.assertTrue(wait.until(EC.invisibility_of_element_located((By.ID, 'myModal'))))

    def test_carousel_right_arrow(self):
        for i in range(1, 4):
            # given
            wait = WebDriverWait(self.driver, 10)
            active_img = self.driver.find_element(By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]')
            arrow_right = self.driver.find_element(By.XPATH, "//div[@id='carousel-example-generic']/a[2]")
            active_dot = self.driver.find_element(By.XPATH, f"//div[@id='carousel-example-generic']/ol/li[{i}]")
            wait.until(element_has_css_class((By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]'), "active"))
            # then
            self.assertIn("active", active_img.get_attribute("class"))
            self.assertIn("active", active_dot.get_attribute("class"))
            # when
            arrow_right.click()

    def test_carousel_left_arrow(self):
        for i in range(3, 0):
            # given
            wait = WebDriverWait(self.driver, 10)
            active_img = self.driver.find_element(By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]')
            arrow_left = self.driver.find_element(By.XPATH, "//div[@id='carousel-example-generic']/a[1]")
            active_dot = self.driver.find_element(By.XPATH, f"//div[@id='carousel-example-generic']/ol/li[{i}]")
            wait.until(element_has_css_class((By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]'), "active"))
            # when
            arrow_left.click()
            # then
            self.assertIn("active", active_img.get_attribute("class"))
            self.assertIn("active", active_dot.get_attribute("class"))

    def test_carousel_dots(self):
        for i in range(1, 4):
            # given
            wait = WebDriverWait(self.driver, 10)
            active_img = self.driver.find_element(By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]')
            active_dot = self.driver.find_element(By.XPATH, f"//div[@id='carousel-example-generic']/ol/li[{i}]")
            # when
            active_dot.click()
            wait.until(element_has_css_class((By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]'), "active"))
            # then
            self.assertIn("active", active_img.get_attribute("class"))
            self.assertIn("active", active_dot.get_attribute("class"))

    def tearDown(self) -> None:
        self.driver.quit()
