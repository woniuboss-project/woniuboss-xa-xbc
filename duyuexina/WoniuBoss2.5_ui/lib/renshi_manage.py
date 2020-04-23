import time
from tools.service import Service


class EmployManage:
    def __init__(self,driver):
        self.driver = driver

    #点击“面试”按钮
    def click_interview(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[8]/button').click()

    #输入提问内容
    def input_question(self,question_content):
        content = self.driver.find_element_by_id('squestion')
        Service.send_input(content,question_content)

    #输入评价内容
    def input_evalute(self,evalute_content):
        content = self.driver.find_element_by_id('sval')
        Service.send_input(content,evalute_content)

    #保存面试结果
    def click_save(self):
        self.driver.find_element_by_id('saveSkillbtn').click()

    #技术面试动作组合
    def technical_interview(self,base_config_path,technical_interview_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[6]').click()
        time.sleep(6)
        self.click_interview()
        # self.choose_result(technical_interview_data['result'])
        self.input_question(technical_interview_data['question_content'])
        self.input_evalute(technical_interview_data['evalute_content'])
        self.click_save()

    #点击“就业管理”按钮
    def click_job_manage(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/ul/li[2]/a').click()

    #点击“面试”
    def mock(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[9]/button[1]').click()

    #输入期望薪资
    def input_salary(self,salary):
        money = self.driver.find_element_by_id('msalary')
        Service.send_input(money,salary)

    #选择沟通能力
    def choose_ability(self):
        ability_select = self.driver.find_element_by_id('mcomm')
        Service.select_random(ability_select)

    #输入备注
    def input_remark(self,mremark):
        remark = self.driver.find_element_by_id('mremark')
        Service.send_input(remark,mremark)

    #点击“保存”按键
    def click_save_button(self):
        self.driver.find_element_by_id('saveEditMBtn').click()

    #模拟面试动作组合
    def mock_interview(self,base_config_path,mock_interview_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[6]').click()
        time.sleep(6)
        self.click_job_manage()
        self.mock()
        self.input_salary(mock_interview_data['salary'])
        self.choose_ability()
        self.input_remark(mock_interview_data['mremark'])
        self.click_save_button()
        driver.switch_to.alert.accept()

    #勾选电脑回收
    def click_computer(self):
        self.driver.find_element_by_id('computer4').click()

    #勾选协议
    def click_sign(self):
        self.driver.find_element_by_id('protocol4').click()

    #勾选入职
    def click_injob(self):
        self.driver.find_element_by_id('entry4').click()

    #点击提交按钮
    def click_submit(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[2]/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[9]/button[2]').click()

    #提交结果组合
    def submit(self):
        self.click_computer()
        self.click_sign()
        self.click_injob()
        self.click_submit()





