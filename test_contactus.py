import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ContactUs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.webdriveruniversity.com/Contact-Us/contactus.html")
        self.first_name = self.driver.find_element(By.NAME, "first_name")
        self.last_name = self.driver.find_element(By.NAME, "last_name")
        self.email = self.driver.find_element(By.NAME, "email")
        self.msg = self.driver.find_element(By.NAME, "message")
        self.submit_btn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        self.reset_btn = self.driver.find_element(By.XPATH, "//input[@type='reset']")

    def test_contact_us_with_correct_data(self):
        # given
        self.first_name.send_keys("Joe")
        self.last_name.send_keys("Doe")
        self.email.send_keys("JoeDoe@jd.com")
        self.msg.send_keys("message")
        # when
        self.submit_btn.click()
        # then
        self.assertTrue("Thank You for your Message!" == self.driver.find_element(By.XPATH, "//h1").text)
        self.assertIn("thank-you", self.driver.current_url)

    def test_contact_us_with_incorrect_data(self):
        # given
        self.email.send_keys("notanemail")
        # when
        self.submit_btn.click()
        # then
        self.assertIn("Error: all fields are required", self.driver.find_element(By.XPATH, "/html/body").text)
        self.assertIn("Error: Invalid email address", self.driver.find_element(By.XPATH, "/html/body").text)

    def test_contact_us_reset(self):
        # given
        self.first_name.send_keys("Joe")
        self.last_name.send_keys("Doe")
        self.email.send_keys("JoeDoe@s.com")
        self.msg.send_keys("message")

        # when
        self.reset_btn.click()

        # then
        self.assertEqual("", self.first_name.get_attribute("value"))
        self.assertEqual("", self.last_name.get_attribute("value"))
        self.assertEqual("", self.email.get_attribute("value"))
        self.assertEqual("", self.msg.get_attribute("value"))

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
