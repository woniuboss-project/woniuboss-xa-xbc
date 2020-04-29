import time
from selenium.webdriver.support.select import Select


class ResourceTurn:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text(u'转交资源').click()

    def decode(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()

    def resource_turn_query_one(self):
        self.decode()
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/button').click()

    def resource_turn_query_two(self):
        self.decode()
        selector_one = self.driver.find_element_by_id('regionSelect1')
        Select(selector_one).select_by_index(1)
        time.sleep(2)
        selector_two = self.driver.find_element_by_name('dept')
        Select(selector_two).select_by_index(3)
        time.sleep(2)
        selector_three = self.driver.find_element_by_id('empNameSelect1')
        Select(selector_three).select_by_index(1)
        time.sleep(2)
        selector_four = self.driver.find_element_by_name('last_status')
        Select(selector_four).select_by_index(6)
        time.sleep(2)
        selector_four = self.driver.find_element_by_name('source')
        Select(selector_four).select_by_index(11)
        time.sleep(2)
        self.driver.find_element_by_name('cusInfo').send_keys('huhu')
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/button').click()

    def resource_turn_commit(self):
        self.resource_turn_query_two()
        time.sleep(2)
        self.driver.find_element_by_name('btSelectItem').click()
        time.sleep(2)
        selector_one = self.driver.find_element_by_id('regionSelect2')
        Select(selector_one).select_by_index(1)
        time.sleep(2)
        selector_two = self.driver.find_element_by_id('deptSelect2')
        Select(selector_two).select_by_index(3)
        time.sleep(2)
        selector_three = self.driver.find_element_by_id('empNameSelect2')
        Select(selector_three).select_by_index(2)
        time.sleep(2)
        self.driver.find_element_by_id('Submit').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[2]').click()



