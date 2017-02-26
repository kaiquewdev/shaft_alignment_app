''' Component Standalone Example Test '''

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class VisualizationIndexTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8910',desired_capabilities=DesiredCapabilities.PHANTOMJS)
        self.component_target_url = 'http://localhost:8082/visualization'

    def test_h1(self):
        self.driver.get(self.component_target_url)
        self.header = self.driver.find_element_by_css_selector('h1')
        self.assertEqual(self.header.text,'Shaft alignment')

    def test_hr(self):
        self.driver.get(self.component_target_url)
        self.hr = self.driver.find_elements_by_css_selector('hr')
        self.assertEqual(len(self.hr),2)

    def test_input(self):
        self.driver.get(self.component_target_url)
        self.input = self.driver.find_elements_by_css_selector('input')
        self.assertEqual(len(self.input),4)

    def test_br(self):
        self.driver.get(self.component_target_url)
        self.br = self.driver.find_elements_by_css_selector('br')
        self.assertEqual(len(self.br),10)

if __name__ == '__main__':
    unittest.main(verbosity=2)


