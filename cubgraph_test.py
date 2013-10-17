import unittest
from selenium import webdriver
import keys 

class TestingCubgraphica(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.CHROME
        desired_capabilities['version'] = ''
        desired_capabilities['platform'] = 'OS X 10.6'
        desired_capabilities['name'] = 'Testing Cubgraphica in Python at Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor=keys.executor
        )
        self.driver.implicitly_wait(30)

    def test_cubgraphica(self):
        self.driver.get('http://www.cubgraphica.com')
        self.assertTrue("Grace Wong" in self.driver.title)
     	more = self.driver.find_element_by_class_name('slidedown')
        more.click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('In my previous life' in body.text)

        # test links
        github = self.driver.find_element_by_link_text('Github')
        github.click()
        self.assertTrue('gwongz' in self.driver.title)
  
        # commented = self.driver.find_element_by_id('your_comments')
        # self.assertTrue('Your comments: Hello! I am some example comments.'
        #                 ' I should be in the page after submitting the form'
        #                 in commented.text)
        # body = self.driver.find_element_by_xpath('//body')
        # self.assertFalse('I am some other page content' in body.text)
        # self.driver.find_elements_by_link_text('i am a link')[0].click()
        # body = self.driver.find_element_by_xpath('//body')
        # self.assertTrue('I am some other page content' in body.text)

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

