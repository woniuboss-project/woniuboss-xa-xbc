import time
from WoniuBoss4.tools.service import Service
import random
from selenium.webdriver.support.select import Select


class ResourceTrain:

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element_by_link_text(u'培训资源').click()

    def decode(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()

    def click_train_add_button(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/div/div/button').click()
        time.sleep(2)

    def input_train_telephone(self, telephone):
        t_phone = self.driver.find_element_by_name('cus.tel')
        Service.send_input(t_phone, telephone)

    def input_train_name(self, name):
        t_name = self.driver.find_element_by_name('cus.name')
        Service.send_input(t_name, name)

    def train_sex_select_random(self):
        selector = self.driver.find_element_by_name('cus.sex')
        Service.select_random(selector)

    def train_status_select_random(self):
        selector = self.driver.find_element_by_name('cus.last_status')
        Service.select_random(selector)

    def train_edu_select_random(self):
        selector = self.driver.find_element_by_name('cus.education')
        Service.select_random(selector)

    def train_where_select_random(self):
        selector = self.driver.find_element_by_name('cus.source')
        Service.select_random(selector)

    def click_train_save_button(self):
        self.driver.find_element_by_id('addCusBtn').click()

    def check_add(self):
        time.sleep(5)
        if "新增成功" in self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[2]/div').text:
            self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button').click()
        else:
            self.driver.refresh()

    # 资源新增
    def excute_add_train_resource(self, tel, name):
        self.decode()
        self.click_train_add_button()
        self.input_train_telephone(tel)
        self.input_train_name(name)
        self.train_sex_select_random()
        self.train_status_select_random()
        self.train_edu_select_random()
        self.train_where_select_random()
        self.click_train_save_button()
        self.check_add()

    # 废弃资源
    def excute_abandon_button(self):
        self.decode()
        self.driver.find_element_by_name('btSelectItem').click()
        self.driver.find_element_by_id('abandon').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[3]/button[2]').click()

    def click_find_button(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div/button').click()

    def click_train_tail_button(self):
        self.driver.find_element_by_xpath(
            '//table[@id="personal-table"]/tbody/tr[1]/td[15]/button[1]')
        time.sleep(2)

    def click_link_text(self):
        self.driver.find_element_by_link_text(u'跟踪资源').click()

    def train_this_status_random(self):
        selector = self.driver.find_element_by_id('newStatus')
        Service.select_random(selector)

    def train_this_level_random(self):
        selector = self.driver.find_element_by_name('priority')
        Service.select_random(selector)

    def click_tail_date(self):
        self.driver.find_element_by_id('next_time').click()
        self.driver.find_element_by_xpath('/html/body/div[11]/div[3]/table/tbody/tr[4]/td[2]').click()

    def input_tail_information(self, content):
        self.driver.find_element_by_name('t.remark').send_keys(content)

    def click_tail_save_button(self):
        self.driver.find_element_by_id('saveTrackingBtn').click()

    # 跟踪资源
    def excute_tail(self, content):
        self.decode()
        self.click_find_button()
        self.click_train_tail_button()
        self.click_link_text()
        self.train_status_select_random()
        self.train_this_level_random()
        self.click_tail_date()
        self.input_tail_information(content)
        self.click_tail_save_button()
        time.sleep(5)
        self.driver.refresh()

    def click_edit_button(self):
        self.driver.find_element_by_xpath(
            '//table[@id="personal-table"]/tbody/tr[%s]/td[15]/button[2]' % random.randint(1, 2))

    def train_edit_information(self, name, telphone):
        self.input_train_name(name)
        self.input_train_telephone(telphone)

    def click_edit_save_button(self):
        self.driver.find_element_by_id('alterCusBtn').click()

    # 修改资源
    def excute_edit(self, name, telphone):
        self.decode()
        self.click_find_button()
        time.sleep(1)
        self.click_edit_button()
        self.train_edit_information(name, telphone)
        self.click_edit_save_button()

    # 搜索资源
    def select_query_resource(self):
        self.decode()
        selector = self.driver.find_element_by_name('pool_type')
        for i in range(0, 5):
            Select(selector).select_by_index(i)
            time.sleep(1)

    def selector_query_status(self):
        self.decode()
        selector = self.driver.find_element_by_name('last_status')
        for i in range(0, 12):
            Select(selector).select_by_index(i)
            time.sleep(2)

    def selector_query_source(self):
        self.decode()
        selector = self.driver.find_element_by_name('source')
        for i in range(0, 26):
            Select(selector).select_by_index(i)
            time.sleep(2)

    def input_query_date(self, s_time, e_time):
        self.decode()
        self.driver.find_element_by_name('s_allottime').send_keys(s_time)
        self.driver.find_element_by_name('e_allottime').send_keys(e_time)
        self.click_find_button()

    def input_query_information(self, data):
        self.decode()
        self.driver.find_element_by_name('cusInfo').send_keys(data)
        self.click_find_button()

    def selector_query_combination(self):
        self.decode()
        selector_one = self.driver.find_element_by_name('region')
        Select(selector_one).select_by_index(3)
        selector_two = self.driver.find_element_by_name('dept')
        Select(selector_two).select_by_index(3)
        selector_three = self.driver.find_element_by_name('workId')
        Select(selector_three).select_by_index(2)
