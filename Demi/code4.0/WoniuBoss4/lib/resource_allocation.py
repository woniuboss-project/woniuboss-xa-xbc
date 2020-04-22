import time
from WoniuBoss4.tools.service import Service
from selenium.webdriver.support.select import Select


class ResourceAllocation:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text(u'分配资源').click()

    # 查询资源
    def decode(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()

    def allocation_query_one(self):
        self.decode()
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[2]/button').click()

    def allocation_query_two(self):
        self.decode()
        selector = self.driver.find_element_by_name('source')
        Select(selector).select_by_index(11)

    def allocation_query_three(self, name):
        self.decode()
        self.driver.find_element_by_name('cusInfo').send_keys(name)
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[2]/button').click()

    # 手动提交分配
    def excute_manual_commit(self):
        self.allocation_query_three('ww')
        time.sleep(2)
        self.driver.find_element_by_name('btSelectItem').click()
        time.sleep(2)
        selector = self.driver.find_element_by_id('empNameSelect')
        Service.select_random(selector)
        self.driver.find_element_by_id('Submit').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('button.btn.btn-primary').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button').click()

    # 按比例分配
    def excute_ratio_commit(self):
        self.allocation_query_one()
        time.sleep(2)
        self.driver.find_element_by_name('btSelectItem').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[3]/button').click()
        self.driver.find_element_by_id('proportion_submit').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button').click()



