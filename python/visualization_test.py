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

if __name__ == '__main__':
    unittest.main(verbosity=2)


