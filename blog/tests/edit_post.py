import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editPost(self):
        """ SIGN IN """
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"

        """ Edit Post """
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h2/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys("This title has been changed with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys("This description has been changed with selenium")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(2)
        assert "Saved"
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()