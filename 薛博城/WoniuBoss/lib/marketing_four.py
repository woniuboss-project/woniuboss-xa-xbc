from selenium.webdriver.support.select import Select
import time

from WoniuBoss.lib.login_four import Login
from WoniuBoss.tools.service import Service

class Market:
    def __init__(self,driver):
        self.driver=driver

    #点击市场营销
    def click_market(self):
        self.driver.find_element_by_link_text('市场营销').click()

    #点击建立资源
    def click_resume(self):
        self.driver.find_element_by_link_text('简历资源').click()

    # 进行解密
    def click_psd(self, passwd):
        self.driver.find_element_by_id('btn-decrypt').click()
        sepass = self.driver.find_element_by_name('secondPass')
        Service.send_input(sepass, passwd)
        time.sleep(5)
        self.driver.find_element_by_xpath('//button[@onclick="decrypt();"]').click()
    #选择区域
    def click_region(self,region):
        reg = self.driver.find_element_by_name('regionSelect')
        reg.click()
        Select(reg).select_by_visible_text(region)

    # 选择状态
    def click_status(self, status):
        statu = self.driver.find_elements_by_class_name('m-sel.sel-text')[1]
        statu.click()
        Select(statu).select_by_visible_text(status)
    #选择来源
    def click_source(self,source):
        sour=self.driver.find_element_by_name("source")
        sour.click()
        Select(sour).select_by_visible_text(source)

    # 输入时间
    def input_time(self, data_time1, data_time2):
        data1 = self.driver.find_element_by_name('s_time')
        Service.send_input(data1, data_time1)
        data2 = self.driver.find_element_by_name('e_time')
        Service.send_input(data2, data_time2)
    #输入搜索内容
    def input_text(self,text_want):
        cus=self.driver.find_element_by_name('info')
        Service.send_input(cus,text_want)

    # 点击查询
    def click_seek(self):
        self.driver.find_element_by_class_name('btn.btn-padding.btn-info.btn-search').click()

    #查询动作组合
    def do_seek(self,seek):
        self.click_market()
        self.click_resume()
        self.click_psd(seek['passwd'])
        self.click_region(seek['region'])
        self.click_status(seek['status'])
        self.click_source(seek['source'])
        self.input_time(seek['time1'],seek['time2'])
        self.input_text(seek['content'])
        self.click_seek()

    #点击新增
    def add_click(self):
        self.driver.find_element_by_xpath('//button[@onclick="showAddResModal();"]').click()

    # 选择区域
    def add_region(self, region):
        reg = self.driver.find_elements_by_xpath('//select[@name="cus.region_id"]')[1]
        reg.click()
        Select(reg).select_by_visible_text(region)
    #选择部门
    def add_section(self,section):
        sec=self.driver.find_elements_by_xpath('//select[@name="cus.department_id"]')[1]
        sec.click()
        Select(sec).select_by_visible_text(section)
    #输入电话
    def add_tel(self,phone):
        tel=self.driver.find_elements_by_xpath('//input[@name="cus.tel"]')[1]
        Service.send_input(tel,phone)
    #输入姓名
    def add_name(self,name):
        aname=self.driver.find_elements_by_xpath('//input[@name="cus.name"]')[1]
        Service.send_input(aname,name)
    #选择最新状态
    def add_status(self,status):
        sta = self.driver.find_elements_by_xpath('//select[@name="cus.last_status"]')[2]
        sta.click()
        Select(sta).select_by_visible_text(status)
    #点击保存
    def add_button(self):
        self.driver.find_element_by_id('addCusBtn').click()
    #点击确定
    def add_affirm(self):
        self.driver.find_element_by_xpath('//button[@data-bb-handler="ok"]').click()

    #新增组合动作
    def add_do(self,add):
        self.click_market()
        self.click_resume()
        self.click_psd(add['passwd'])
        self.add_click()
        time.sleep(5)
        self.add_region(add['region'])
        self.add_section(add['section'])
        self.add_tel(add['tel'])
        self.add_name(add['name'])
        self.add_status(add['status'])
        time.sleep(2)
        self.add_button()
        time.sleep(2)
        self.add_affirm()

    #点击修改
    def edit_click(self):
        self.driver.find_elements_by_class_name('btn.btn-info')[3].click()

    # 点击保存
    def edit_button(self):
        self.driver.find_element_by_id('eidtCusBtn').click()

    #修改组合动作
    def edit_do(self,edit):
        self.click_market()
        self.click_resume()
        self.click_psd(edit['passwd'])
        self.edit_click()
        time.sleep(5)
        self.add_region(edit['region'])
        self.add_section(edit['section'])
        self.add_tel(edit['tel'])
        self.add_name(edit['name'])
        self.add_status(edit['status'])
        time.sleep(2)
        self.edit_button()
        time.sleep(2)
        self.add_affirm()

    #点击上传
    def uploading(self):
        self.driver.find_element_by_xpath('//button[@onclick="showUpResModal();"]').click()
    #选择区域
    def upload_region(self,region):
        upreg = self.driver.find_element_by_id('regionSelect')
        upreg.click()
        Select(upreg).select_by_visible_text(region)

    #选择部门
    def upload_section(self,region):
        upreg = self.driver.find_element_by_id('dpetSelect')
        upreg.click()
        Select(upreg).select_by_visible_text(region)
    #上传文件
    def upload_xsl(self,path):
        upxsl=self.driver.find_element_by_id('files')
        upxsl.send_keys(path)

    #点击提交
    def upload_submit(self):
        self.driver.find_element_by_xpath('//button[@onclick="uploadfile();"]').click()

    #上传文件组合动作
    def upload_do(self,upload):
        self.click_market()
        self.click_resume()
        self.click_psd(upload['passwd'])
        time.sleep(2)
        self.uploading()
        self.upload_region(upload['region'])
        self.upload_section(upload['section'])
        self.upload_xsl(upload['xsl'])
        self.upload_submit()
        time.sleep(10)
        self.add_affirm()

    #点击邮件读取
    def email_read(self,read):
        self.click_market()
        self.click_resume()
        self.click_psd(read['passwd'])
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@onclick="readmail();"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@data-bb-handler="confirm"]').click()

