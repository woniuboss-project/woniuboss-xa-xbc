from selenium.webdriver.support.select import Select
import time

from WoniuBoss.lib.login_four import Login
from WoniuBoss.tools.service import Service

class Job:
    def __init__(self,driver):
        self.driver=driver
    #点击就业管理
    def click_job(self):
        self.driver.find_element_by_link_text('就业管理').click()

    #点击模拟面试
    def simulation_of_interview(self):
        self.driver.find_element_by_link_text('模拟面试').click()

    # 点击面试记录
    def interview_records(self):
        self.driver.find_element_by_link_text('面试记录').click()

    #点击入职信息
    def entry_information(self):
        self.driver.find_element_by_link_text('入职信息').click()
    #点击企业客户
    def business_customer(self):
        self.driver.find_element_by_link_text('企业客户').click()

    # 进行解密
    def click_psd(self, passwd):
        self.driver.find_element_by_id('btn-decrypt').click()
        sepass = self.driver.find_element_by_name('secondPass')
        Service.send_input(sepass, passwd)
        time.sleep(5)
        self.driver.find_element_by_xpath('//button[@onclick="decrypt();"]').click()
    #技术面试选择
    def select_interview(self,interview):
        view=self.driver.find_element_by_id('studentSelect')
        view.click()
        Select(view).select_by_visible_text(interview)

    # 班级选择
    def select_class(self, classroom):
        croom = self.driver.find_element_by_id('semesterSelect')
        croom.click()
        Select(croom).select_by_visible_text(classroom)
    #输入姓名
    def input_name(self,name):
        uname=self.driver.find_element_by_name('stuName')
        Service.send_input(uname,name)
    #输入学号
    def input_code(self,code):
        stuNo = self.driver.find_element_by_name('stuNo')
        Service.send_input(stuNo, code)
    #点击确定
    def click_button(self):
        self.driver.find_element_by_xpath('//button[@onclick="queryStuInfo();"]').click()

    #查询动作组合
    def simulation_seek(self,seek):
        self.click_job()
        self.simulation_of_interview()
        self.click_psd(seek['passwd'])
        time.sleep(5)
        self.select_interview(seek['interview'])
        self.select_class(seek['classroom'])
        self.input_name(seek['name'])
        self.input_code(seek['code'])
        self.click_button()
    #点击面试
    def simulation_click(self):
        self.driver.find_elements_by_class_name('btn.btn-info').click()
    #输入面试信息
    def simulation_message(self,pay,link,remark):
        mon=self.driver.find_element_by_id('msalary')
        Service.send_input(mon,pay)
        exchange = self.driver.find_element_by_id('mcomm')
        exchange.click()
        Select(exchange).select_by_visible_text(link)
        ps = self.driver.find_element_by_id('mremark')
        Service.send_input(ps, remark)
        self.driver.find_element_by_id('saveSkillbtn').click()

    #面试操作
    def simulation_input(self,do):
        self.click_job()
        self.simulation_of_interview()
        self.click_psd(do['passwd'])
        time.sleep(5)
        self.simulation_click()
        self.simulation_message(do['pay'],do['link'],do['remark'])

    #面试记录
    def records_click(self,records):
        self.click_job()
        self.interview_records()
        self.click_psd(records['passwd'])
        time.sleep(5)
        sem=self.driver.find_element_by_id('semesterSelect')
        Service.send_input(sem,records['classroom'])
        self.input_name(records['name'])
        self.input_code(records['code'])
        self.click_button()



