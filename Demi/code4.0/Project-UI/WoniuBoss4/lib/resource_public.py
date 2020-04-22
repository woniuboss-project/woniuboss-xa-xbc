import time
from WoniuBoss4.tools.service import Service
from selenium.webdriver.support.select import Select


class ResourcePublic:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text(u'公共资源').click()

    def decode(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()

    # 下拉选框查询
    def public_resource_query_one(self):
        self.decode()
        selector_one = self.driver.find_element_by_name('region')
        Select(selector_one).select_by_index(1)
        time.sleep(2)
        selector_two = self.driver.find_element_by_name('region')
        Select(selector_two).select_by_index(3)
        time.sleep(2)
        selector_three = self.driver.find_element_by_name('empName')
        Select(selector_three).select_by_index(1)
        time.sleep(2)
        selector_four = self.driver.find_element_by_name('last_status')
        Select(selector_four).select_by_index(6)
        time.sleep(2)
        selector_four = self.driver.find_element_by_name('source')
        Select(selector_four).select_by_index(8)
        time.sleep(2)
        selector_four = self.driver.find_element_by_name('education')
        Select(selector_four).select_by_index(4)

    def public_resource_query_two(self, name):
        self.decode()
        self.driver.find_element_by_name('cusInfo').send_keys(name)
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/button').click()

    # 认领资源
    def claim_resource(self):
        self.driver.find_element_by_name('btSelectItem').click()
        time.sleep(1)
        self.driver.find_element_by_id('ownCusBtn').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button[2]').click()
