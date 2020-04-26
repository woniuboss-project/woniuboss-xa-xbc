from selenium.webdriver.support.select import Select
import time
from tools.service import Service


class FinanceManage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.find_element_by_id('abc').click()
        time.sleep(2)


    #选择开始时间
    def select_start_time(self):
        self.driver.find_element_by_id('selectTimeStart').click()
        time.sleep(2)

    def select_end_time(self):
        self.driver.find_element_by_id('selectTimeEnd').click()
        time.sleep(2)

    #选择一级科目
    def select_one_subject(self,one_subject):
        Select(self.driver.find_element_by_id('1_subject')).select_by_visible_text(one_subject)

    #选择二级科目
    def select_two_subject(self,two_subject):
        Select(self.driver.find_element_by_id('2_subject')).select_by_visible_text(two_subject)

    #点击查询
    def click_query(self):
        self.driver.find_element_by_xpath('//div[@id="account"]/div/button[1]').click()

    #财务流水查询
    def finance_query(self,contents):
        self.select_start_time()
        self.select_end_time()
        self.select_one_subject(contents['one_subject'])
        self.select_two_subject(contents['two_subject'])
        self.click_query()

if __name__ == '__main__':

    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://192.168.159.143:8080/WoniuBoss2.5')
    driver.maximize_window()
    driver.implicitly_wait(2)
    Service.miss_login(driver,'../config/base.conf')
    contents = {'one_subject':'主营业务收入','two_subject':'就业培训'}
    FinanceManage(driver).finance_query(contents)


