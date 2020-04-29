import time

from woniuboss2_ui.tools.service import Service


class Job:

    def __init__(self, driver):
        self.driver = driver

    def status_random(self):
        selector = self.driver.find_element_by_id('studentSelect')
        from selenium.webdriver.support.select import Select
        Select(selector).select_by_index(0)

    def click_interview_button(self):
        self.driver.find_element_by_xpath(
            '//table[@id="stuInfo_table"]/tbody/tr[5]/td[8]/button').click()
        time.sleep(2)

    def status_two_random(self):
        selector = self.driver.find_element_by_id('isPassSkill')
        Service.select_random(selector)

    def input_interview_information(self, contents):
        e_text = self.driver.find_element_by_id('squestion')
        Service.send_input(e_text, contents['question'])
        e_resu = self.driver.find_element_by_id('sval')
        Service.send_input(e_resu, contents['result'])
        self.driver.find_element_by_id('saveSkillbtn').click()

    # 技术面试
    def excute_tech(self, contents):
        self.status_random()
        self.click_interview_button()
        self.status_two_random()
        self.input_interview_information(contents)

    def query_job_manager(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()
        time.sleep(2)
        selector_one = self.driver.find_element_by_id('semesterSelect')
        from selenium.webdriver.support.select import Select
        Select(selector_one).select_by_index(7)
        time.sleep(2)
        selector_two = self.driver.find_element_by_id('stu-orientation')
        Select(selector_two).select_by_index(2)
        time.sleep(2)

    def edit_job_manager_one(self, contents):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element_by_name('stuName').send_keys(contents['name'])
        self.driver.find_element_by_xpath('//div[@id="employ"]/div[2]/button').click()
        self.driver.find_element_by_id('protocol0').click()
        self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[9]/button[2]').click()
        time.sleep(2)
        Service.alert_windows(self.driver)
        time.sleep(2)
        self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[9]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_id('msalary').send_keys(contents['data'])
        seletor = self.driver.find_element_by_id('mcomm')
        Service.select_random(seletor)
        self.driver.find_element_by_id('mremark').send_keys(contents['content'])
        self.driver.find_element_by_id('saveEditMBtn').click()

    def edit_job_manager_two(self, date, content):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[9]/button[1]').click()
        self.driver.find_element_by_link_text(u'真实面试').click()
        time.sleep(2)
        self.driver.find_element_by_id('reatime').send_keys(date)
        time.sleep(2)
        self.driver.find_element_by_id('rearemark').send_keys(content)
        time.sleep(2)
        self.driver.find_element_by_id('saveEditRBtn').click()

    def edit_job_manager_three(self, date, salary, content):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/ul/li[2]/a').click()
        time.sleep(3)
        self.driver.find_element_by_id('btn-decrypt').click()
        self.driver.find_element_by_name('secondPass').send_keys('woniu123')
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div[1]/div[1]/div[3]/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[9]/button[1]').click()
        self.driver.find_element_by_link_text(u'入职情况').click()
        time.sleep(2)
        self.driver.find_element_by_id('jdate').send_keys(date)
        time.sleep(2)
        self.driver.find_element_by_id('jsalary').send_keys(salary)
        time.sleep(2)
        self.driver.find_element_by_id('jremark').send_keys(content)
        time.sleep(2)
        self.driver.find_element_by_id("saveEditJBtn").click()
