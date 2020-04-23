from selenium.webdriver.support.select import Select
import time

from WoniuBoss.lib.login_four import Login
from WoniuBoss.tools.service import Service

class Report:
    def __init__(self,driver):
        self.driver=driver

    # 点击报表中心
    def click_report(self):
        self.driver.find_element_by_link_text('报表中心').click()

    # 点击咨询部
    def click_counsel(self):
        self.driver.find_element_by_link_text('咨询部').click()

    # 咨询输入搜索时间
    def input_time(self,timeone,timetwo):
        stime=self.driver.find_element_by_name('s_consulttime')
        Service.send_input(stime,timeone)
        etime=self.driver.find_element_by_name('e_consulttime')
        Service.send_input(etime, timetwo)
        self.driver.find_element_by_class_name('btn.btn-info.btn-padding').click()

    #咨询点击今日
    def click_today(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[1].click()

    #咨询点击本周
    def click_week(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[2].click()

    #咨询 点击本月
    def click_month(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[3].click()

    #咨询点击上周
    def click_lastweek(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[4].click()
    #咨询点击上月
    def click_lastmonth(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[5].click()
    #咨询点击本年
    def click_year(self):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[6].click()

    #咨询搜索组合操作
    def report_do(self,report):
        self.click_report()
        self.click_counsel()
        time.sleep(8)
        self.input_time(report['timeone'],report['timetwo'])

    #点击市场部
    def click_market(self):
        self.driver.find_element_by_link_text('市场部').click()

    # 市场输入搜索时间
    def market_time(self, timeone, timetwo):
        stime = self.driver.find_element_by_name('s_sourcetime')
        Service.send_input(stime, timeone)
        etime = self.driver.find_element_by_name('e_sourcetime')
        Service.send_input(etime, timetwo)
        self.driver.find_element_by_class_name('btn.btn-info.btn-padding').click()

    #市场搜索组合
    def market_do(self,market):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.market_time(market['timeone'], market['timetwo'])

    # 市场点击今日
    def market_today(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[1].click()

    # 市场点击本周
    def market_week(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[2].click()

    # 市场 点击本月
    def market_month(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[3].click()

    # 市场点击上周
    def market_lastweek(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[4].click()

    # 市场点击上月
    def market_lastmonth(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[5].click()

    # 市场点击本年
    def market_year(self):
        self.click_report()
        self.click_market()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[6].click()

    #点击教学部
    def teach_click(self):
        self.driver.find_element_by_link_text('教学部').click()
    #选择校区
    def select_sc(self,scour):
        sc = self.driver.find_element_by_name('region')
        sc.click()
        Select(sc).select_by_visible_text(scour)
    #选择方向
    def select_from(self,direction):
        direct = self.driver.find_element_by_name('orientation')
        direct.click()
        Select(direct).select_by_visible_text(direction)
    #选择开班状态
    def select_status(self,statue):
        stu = self.driver.find_element_by_name('opening_status')
        stu.click()
        Select(stu).select_by_visible_text(statue)
    #教学报表统计
    def teaching(self,teach):
        self.click_report()
        self.teach_click()
        self.select_sc(teach['scour'])
        self.select_from(teach['direction'])
        self.select_status(teach['statue'])
    #就业部
    def get_job_click(self):
        self.driver.find_element_by_link_text('就业部').click()
    #选择区域
    def select_area(self,area):
        are = self.driver.find_element_by_name('region_id')
        are.click()
        Select(are).select_by_visible_text(area)
    #就业内容搜索
    def job_time(self, timeone, timetwo):
        stime = self.driver.find_element_by_name('s_jobtime')
        Service.send_input(stime, timeone)
        etime = self.driver.find_element_by_name('e_jobtime')
        Service.send_input(etime, timetwo)
        self.driver.find_element_by_class_name('btn.btn-info.btn-padding').click()
    #就业搜索动作组合
    def job_do(self,job):
        self.click_report()
        self.get_job_click()
        self.select_area(job['area'])
        self.job_time(job['timeone'], job['timetwo'])
    # 就业点击今日
    def job_today(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[1].click()

    # 就业点击本周
    def job_week(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[2].click()

    # 就业 点击本月
    def job_month(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[3].click()

    # 就业点击上周
    def job_lastweek(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[4].click()

    # 就业点击上月
    def job_lastmonth(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[5].click()

    # 就业点击本年
    def job_year(self):
        self.click_report()
        self.get_job_click()
        time.sleep(8)
        self.driver.find_elements_by_class_name('btn.btn-primary.btn-padding')[6].click()