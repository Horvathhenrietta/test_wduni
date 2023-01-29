import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageObjectModel(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://www.webdriveruniversity.com/Page-Object-Model/index.html"
        self.driver.get(self.url)

    def test_titles(self):
        # given
        elements = self.driver.find_elements(By.XPATH, "//p[@class='sub-heading']")
        # when
        # then
        self.assertEqual(elements[0].text, "Who Are We?")
        self.assertEqual(elements[1].text, "GREAT SERVICE!")
        self.assertEqual(elements[2].text, "Why Choose Us?")
        self.assertEqual(elements[3].text, "Excellent Customer Service!")

    def test_navigation(self):
        # given
        expected_urls = ["index.html", "products.html", "contactus.html"]
        # this would only assert if the elements have the expected urls in the href attribute
        # elements = self.driver.find_elements(By.XPATH, "//nav//ul//li//a")
        # for i, el in enumerate(elements):
        #     self.assertIn(expected_urls[i], el.get_attribute("href"))
        # actually checks if nav buttons were clicked do they redirect to the correct page
        # I don't know if it's actually useful but anyway:
        for i, expected_url in enumerate(expected_urls):
            # when
            el = self.driver.find_element(By.XPATH, f"//nav//ul//li[position()={i + 1}]")
            el.click()
            # then
            self.assertIn(expected_url, self.driver.current_url)
            self.driver.get(self.url)

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
            time.sleep(1)
            cur_item = self.driver.find_element(By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]')
            arrow_right = self.driver.find_element(By.XPATH, "//div[@id='carousel-example-generic']/a[2]")
            cur_dot = self.driver.find_element(By.XPATH, f"//div[@id='carousel-example-generic']/ol/li[{i}]")
            self.assertIn("active", cur_item.get_attribute("class"))
            self.assertIn("active", cur_dot.get_attribute("class"))
            arrow_right.click()
            print(i)

    def test_carousel_left_arrow(self):
        for i in range(3, 0):
            # given
            time.sleep(1)
            cur_item = self.driver.find_element(By.XPATH, f'//div[@class="carousel-inner"]/div[{i}]')
            arrow_left = self.driver.find_element(By.XPATH, "//div[@id='carousel-example-generic']/a[1]")
            cur_dot = self.driver.find_element(By.XPATH, f"//div[@id='carousel-example-generic']/ol/li[{i}]")
            arrow_left.click()
            self.assertIn("active", cur_item.get_attribute("class"))
            self.assertIn("active", cur_dot.get_attribute("class"))
            print(i)

    def tearDown(self) -> None:
        self.driver.quit()
