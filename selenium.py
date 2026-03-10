import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

class SeleniumTest(TestCase):
    def test_input_value(self):
        self.URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYA89b557d6f70d54aa43eeb06153992579ebc32185&locale=pl"
        self.INPUT_NAME = "username"
        self.driver.get(self.URL)
        try:
            login_box = self.driver.find_element(By.NAME, self.INPUT_NAME)
        except Exception:
            self.fail("Login box not found")

        login_box.send_keys("test")
        inputValue = login_box.get_attribute("value")
        self.assertEqual(inputValue, "test")
