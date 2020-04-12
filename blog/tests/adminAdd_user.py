import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_admin_addUser(self):
        """ Sign In """
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"

        """ Add user """
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys("seleniumuser2")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys("SeleniumPassword1")
        time.sleep(2)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys("SeleniumPassword1")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/form/div/div/input[1]").click()
        time.sleep(3)
        assert "Saved"
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[3]").click()
        time.sleep(5)


        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
