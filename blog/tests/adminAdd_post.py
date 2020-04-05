import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_admin_addPost(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[1]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_author")
        elem.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(2)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a selenium test post as administrator title")
        time.sleep(2)
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a selenium test post as administrator description")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[4]/div/p/span[2]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
