from selenium.webdriver.support.select import Select
import time
from WoniuBoss.tools.service import Service
from selenium import webdriver

class Train:
    def __init__(self,driver):
        self.driver=driver

    #进行解密
    def click_psd(self,passwd):
        self.driver.find_element_by_id('btn-decrypt').click()
        sepass=self.driver.find_element_by_name('secondPass')
        Service.send_input(sepass,passwd)
        time.sleep(5)
        self.driver.find_elements_by_class_name('btn.btn-info')[0].click()



    #选择资源库
    def select_pool(self,pool):
        pools=self.driver.find_element_by_id('poolSelect')
        pools.click()
        Select(pools).select_by_visible_text(pool)

    #选择咨询师
    def select_Name(self,name):
        empName=self.driver.find_element_by_id('empNameSelect')
        empName.click()
        Select(empName).select_by_visible_text(name)

    #选择状态
    def select_status(self,status):
        statu=self.driver.find_element_by_id('statusSelect')
        statu.click()
        Select(statu).select_by_visible_text(status)

    #选择来源
    def select_source(self,source):
        soure=self.driver.find_element_by_id('sourceSelect')
        soure.click()
        Select(soure).select_by_visible_text(source)

    #输入时间
    def input_time(self,data_time1,data_time2):
        data1=self.driver.find_element_by_id('date1')
        Service.send_input(data1,data_time1)
        data2=self.driver.find_element_by_id('date2')
        Service.send_input(data2,data_time2)

    #输入搜索内容
    def input_text(self,text_want):
        cus=self.driver.find_element_by_name('cusInfo')
        Service.send_input(cus,text_want)
    #点击查询
    def click_seek(self):
        self.driver.find_elements_by_class_name('btn.btn-padding')[3].click()

    #搜索动作组合
    def seek(self,path,seek_student):
        driver=self.driver
        Service.miss_login(driver,path)
        self.click_psd(seek_student['passwd'])
        self.select_pool(seek_student['pool'])
        self.select_Name(seek_student['name'])
        self.select_status(seek_student['status'])
        self.select_source(seek_student['source'])
        self.input_time(seek_student['data_time1'],seek_student['data_time2'])
        self.input_text(seek_student['text_want'])
        self.click_seek()

    #点击新增
    def click_add(self):
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

    #输入电话号码
    def input_phone(self,telephone):
        phone=self.driver.find_elements_by_name('cus.tel')[0]
        Service.send_input(phone,telephone)
    #输入姓名
    def input_name(self,in_name):
        names=self.driver.find_elements_by_name('cus.name')[0]
        Service.send_input(names,in_name)
    #选择最新状态
    def find_zhuangtai(self,condition):
        state=self.driver.find_element_by_css_selector('select.form-control:nth-child(2)')
        state.click()
        Select(state).select_by_visible_text(condition)
    #选择渠道来源
    def find_from(self,SOURCE):
        source=self.driver.find_element_by_css_selector('div:nth-child(5) > div:nth-child(1) > select')
        source.click()
        Select(source).select_by_visible_text(SOURCE)
    #点击保存
    def button_add(self):
        self.driver.find_element_by_id('addCusBtn').click()

    #新增组合动作
    def add_student(self,path,add_student):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_psd(add_student['passwd'])
        self.click_add()
        self.input_phone(add_student['phone'])
        self.input_name(add_student['name'])
        self.find_zhuangtai(add_student['condition'])
        self.find_from(add_student['SOURCE'])
        self.button_add()

    #点击修改
    def click_edit(self):
        self.driver.find_elements_by_css_selector('button.btn.btn-info')[4].click()

    #修改姓名
    def edit_name(self,name):
        uname = self.driver.find_element_by_id('cusName')
        Service.send_input(uname, name)
    #修改电话
    def edit_phone(self,phone):
        uphone = self.driver.find_element_by_id('cusTel')
        Service.send_input(uphone, phone)
    #修改求职意向
    def job_intention(self,intention):
        uinten=self.driver.find_element_by_id('cusIntent')
        Service.send_input(uinten,intention)
    #修改工作年限
    def workage(self,worktime):
        state = self.driver.find_element_by_id('cusWorkageSelect')
        state.click()
        Select(state).select_by_visible_text(worktime)
    #点击保存
    def button_edit(self):
        self.driver.find_element_by_id('alterCusBtn').click()

    #修改组合动作
    def edit_customer(self,path,edit_customer):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_psd(edit_customer['passwd'])
        time.sleep(5)
        self.click_edit()
        self.edit_name(edit_customer['name'])
        self.edit_phone(edit_customer['phone'])
        self.job_intention(edit_customer['intention'])
        self.workage(edit_customer['workage'])
        self.button_edit()

    #点击跟踪
    def click_tail(self):
        self.driver.find_elements_by_css_selector('button.btn.btn-info')[3].click()
    #点击跟踪资源
    def click_tail_resour(self):
        self.driver.find_element_by_css_selector('#trackingCusLi > a:nth-child(1)').click()
    #选择状态
    def click_state(self,state):
        states = self.driver.find_element_by_id('newStatus')
        states.click()
        Select(states).select_by_visible_text(state)
    #选择级别
    def click_priority(self,priority):
        states = self.driver.find_element_by_css_selector('#formFollow > div:nth-child(3) > select:nth-child(2)')
        states.click()
        Select(states).select_by_visible_text(priority)
    #输入跟踪记录
    def input_record(self,record):
        records=self.driver.find_element_by_css_selector('textarea.form-control')
        Service.send_input(records,record)
    #点击保存
    def click_save(self):
        self.driver.find_element_by_id('saveTrackingBtn').click()

    #跟踪组合动作
    def do_tail(self,path,tail):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_psd(tail['passwd'])
        time.sleep(5)
        self.click_tail()
        self.click_tail_resour()
        self.click_state(tail['state'])
        self.click_priority(tail['priority'])
        self.input_record(tail['record'])
        self.click_save()

    #选择信息
    def click_one(self,num):
        self.driver.find_element_by_xpath(f'//input[@data-index={num}]').click()
    #点击废弃
    def click_del(self):
        self.driver.find_element_by_id('abandon').click()
        self.driver.find_element_by_css_selector('button.btn-primary:nth-child(2)').click()

    #废弃组合动作
    def do_delt(self,path,delt):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_psd(delt['passwd'])
        time.sleep(5)
        self.select_pool(delt['pool'])
        time.sleep(5)
        self.click_one(delt['num'])
        self.click_del()
        time.sleep(10)
        self.select_pool(delt['pool_1'])

    #点击转交责任人
    def click_deliver(self):
        self.driver.find_element_by_xpath('//a[@href="transmit"]').click()

    #选择咨询师
    def click_deliver_emp(self,name):
        empName = self.driver.find_element_by_id('empNameSelect1')
        empName.click()
        Select(empName).select_by_visible_text(name)
    #选择区域
    def click_deliver_region(self,region):
        reg = self.driver.find_element_by_id('regionSelect1')
        reg.click()
        Select(reg).select_by_visible_text(region)
    #选择状态
    def click_deliver_status(self,status):
        statu = self.driver.find_element_by_xpath('//select[@name="last_status"]')
        statu.click()
        Select(statu).select_by_visible_text(status)
    #选择来源
    def click_deliver_source(self,source):
        sour=self.driver.find_element_by_xpath("//select[@name='source']")
        sour.click()
        Select(sour).select_by_visible_text(source)
    #选择转交咨询师
    def click_deliver_emp2(self, name_2):
        empName = self.driver.find_element_by_id('empNameSelect2')
        empName.click()
        Select(empName).select_by_visible_text(name_2)
    #选择转交区域
    def click_deliver_region2(self,region_2):
        reg = self.driver.find_element_by_id('regionSelect2')
        reg.click()
        Select(reg).select_by_visible_text(region_2)
    #点击提交
    def click_deliver_submint(self):
        self.driver.find_element_by_id('Submit').click()
    #输入查询的内容
    def click_deliver_Info(self,ucus):
        uname=self.driver.find_element_by_name('cusInfo')
        Service.send_input(uname,ucus)
    #点击查询
    def click_deliver_chaxun(self):
        self.driver.find_element_by_xpath("//button[@onclick='initTable();']").click()
    #选择转交信息
    def click_deliver_one(self,num):
        self.driver.find_element_by_xpath(f'//input[@data-index={num}]').click()
    #确定转交
    def click_deliver_button(self):
        self.driver.find_element_by_xpath('//button[@data-bb-handler="confirm"]').click()
    def click_deliver_button2(self):
        self.driver.find_element_by_xpath('//button[@data-bb-handler="ok"]').click()

    #点击查看
    def click_look(self):
        self.driver.find_element_by_xpath('//button[@data-backdrop="static"]').click()

    #提交组合动作
    def do_submit(self,path,submit):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_deliver()
        self.click_psd(submit['passwd'])
        time.sleep(5)
        self.click_deliver_emp(submit['name'])
        self.click_deliver_region(submit['region'])
        self.click_deliver_status(submit['status'])
        self.click_deliver_source(submit['source'])
        self.click_deliver_emp2(submit['name_2'])
        self.click_deliver_region2(submit['region_2'])
        self.click_deliver_one(submit['num'])
        self.click_deliver_submint()
        time.sleep(3)
        self.click_deliver_button()
        time.sleep(3)
        self.click_deliver_button2()

    #转交查询组合动作
    def do_look(self,path,look):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_deliver()
        self.click_psd(look['passwd'])
        time.sleep(5)
        self.click_deliver_Info(look['ucus'])
        self.click_deliver_chaxun()
        self.click_look()

    #点击公共
    def public_click(self):
        self.driver.find_element_by_xpath('//a[@href="public"]').click()

    #选择最后废弃人
    def public_people(self,upeople):
        people=self.driver.find_element_by_name('empName')
        people.click()
        Select(people).select_by_visible_text(upeople)
    #点击认领
    def public_claim(self):
        self.driver.find_element_by_id('ownCusBtn').click()
    #点击查询
    def public_look(self):
        self.driver.find_elements_by_class_name('btn.btn-padding')[1].click()
    #公共资源池认领组合动作
    def do_claim(self,path,claim):
        driver = self.driver
        Service.miss_login(driver, path)
        self.click_deliver()
        self.click_psd(claim['passwd'])
        time.sleep(5)
        self.public_click()
        self.public_people(claim['name'])
        self.click_deliver_status(claim['status'])
        self.click_deliver_source(claim['source'])
        self.click_deliver_Info(claim['ucus'])
        self.public_look()
        self.click_deliver_one(claim['num'])

    #确认认领
    def affirm_claim(self):
        self.public_claim()
        time.sleep(3)
        self.click_deliver_button()
        time.sleep(3)
        self.click_deliver_button2()

    #点击分配资源
    def resource_click(self):
        self.driver.find_element_by_xpath('//a[@href="allot"]').click()

    #分配资源提交动作组合
    def resource_submit(self,path,submit):
        driver = self.driver
        Service.miss_login(driver, path)
        self.resource_click()
        self.click_psd(submit['passwd'])
        time.sleep(5)
        self.click_deliver_source(submit['source'])
        self.click_deliver_Info(submit['ucus'])
        self.public_look()
        time.sleep(5)
        self.click_deliver_one(submit['num'])
        self.select_Name(submit['name'])
        self.click_deliver_submint()
        time.sleep(3)
        self.click_deliver_button()
        time.sleep(3)
        self.click_deliver_button2()

    #点击按比例分配
    def prorate_distribution(self):
        self.driver.find_element_by_xpath('//button[@onclick="distribution();"]').click()
    #输入比例
    def input_prorate(self,proportion0,proportion1,proportion2,proportion3,proportion4,proportion5):
        pro0=self.driver.find_element_by_name('proportion0')
        Service.send_input(pro0, proportion0)
        pro1 = self.driver.find_element_by_name('proportion1')
        Service.send_input(pro1, proportion1)
        pro2 = self.driver.find_element_by_name('proportion2')
        Service.send_input(pro2, proportion2)
        pro3 = self.driver.find_element_by_name('proportion3')
        Service.send_input(pro3, proportion3)
        pro4 = self.driver.find_element_by_name('proportion4')
        Service.send_input(pro4, proportion4)
        pro5 = self.driver.find_element_by_name('proportion5')
        Service.send_input(pro5, proportion5)

    #提交比例分配
    def submit_proportion(self):
        self.driver.find_element_by_id('proportion_submit').click()
    #按比例分配
    def do_resource(self,path,prorate):
        driver = self.driver
        Service.miss_login(driver, path)
        self.resource_click()
        self.click_psd(prorate['passwd'])
        time.sleep(5)
        self.prorate_distribution()
        self.input_prorate(prorate['proportion0'],prorate['proportion1'],prorate['proportion2'],prorate['proportion3'],prorate['proportion4'],prorate['proportion5'])
        self.submit_proportion()
        self.click_deliver_button()
        self.click_deliver_button2()

