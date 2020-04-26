from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from WoniuBoss4.tools.service import Service
import time

class StudentInfo:

    def __init__(self, driver):
        self.driver = driver
        Service.miss_login(driver, '../config/base.conf')

    def click_student_manage_link(self):
        self.driver.find_element_by_link_text('学员管理').click()

    def click_student_info_link(self):
        Service.wait_until_element_is_visible(self.driver, By.LINK_TEXT, '学员信息')
        self.driver.find_element_by_link_text('学员信息').click()

    def select_orientation_option(self,orien_name):
        Service.box_name_click(self.driver, 'orientation', orien_name)

    def select_class_options(self,class_name):
        Service.wait_until_element_is_visible(self.driver,By.NAME,'stuClass')
        Service.box_name_click(self.driver,'stuClass',class_name)

    def select_status_option(self,status_name):
        Service.box_name_click(self.driver, 'stuStatus', status_name)

    def input_stu_name(self,stu_name):
        ele = self.driver.find_element_by_name('stuName')
        Service.send_input(ele,stu_name)

    def click_query_btn(self):
        self.driver.find_element_by_css_selector('#stuInfo > div.col-lg-12.col-md-12.col-xs-12.con-body-padding.'
                                                 'text-left > button').click()

    def do_search_info(self,orien_name,class_name,status_name,stu_name):
        self.click_student_manage_link()
        self.click_student_info_link()
        self.select_orientation_option(orien_name)
        self.select_class_options(class_name)
        self.select_status_option(status_name)
        time.sleep(2)
        self.input_stu_name(stu_name)
        self.click_query_btn()

    def click_modify_btn(self):
        self.driver.find_element_by_css_selector('#stuInfo_table > tbody > tr:nth-child(1) > '
                                                 'td:nth-child(12) > button:nth-child(2)').click()

    def input_box_stu_name(self,name):
        ele = self.driver.find_element_by_name('stu.student_name')
        Service.send_input(ele, name)

    def input_box_stu_tel(self,stu_tel):
        ele = self.driver.find_element_by_name('stu.tel')
        Service.send_input(ele, stu_tel)

    def select_new_status(self,status):
        Service.box_name_click(self.driver,'stu.status',status)

    def select_pay_fee(self,fee):
        Service.box_name_click(self.driver,'stu.need_fee',fee)

    def input_connect_person(self,person):
        ele = self.driver.find_element_by_name('stu.emergency_person')
        Service.send_input(ele,person)

    def input_connect_tel(self,connect_tel):
        ele = self.driver.find_element_by_name('stu.emergency_tel')
        Service.send_input(ele,connect_tel)

    def input_box_school(self,school):
        ele = self.driver.find_element_by_name('stu.school')
        Service.send_input(ele,school)

    def select_diploma(self,diploma):
        Service.box_name_click(self.driver,'stu.education',diploma)

    def input_major(self,major):
        ele = self.driver.find_element_by_name('stu.major')
        Service.send_input(ele,major)

    def input_id_number(self,id_number):
        ele = self.driver.find_element_by_name('stu.IDnumber')
        Service.send_input(ele,id_number)

    def click_graduate_time(self):
        ele = self.driver.find_element_by_name('stu.graduation_time')
        ele.click()
        # self.driver.find_element_by_css_selector('body > div: nth - child(22) > div.datetimepicker - days > table >'
        #                                          ' tbody > tr:nth - child(2) > td: nth - child(4)').clcik()
        ele.send_keys(Keys.ENTER)

    def input_stu_age(self,age):
        ele = self.driver.find_element_by_name('stu.age')
        Service.send_input(ele,age)

    def click_save_btn(self):
        self.driver.find_element_by_css_selector('#form-modify > div > div > div.modal-footer > button').click()

    def do_modify_student_info(self,name,stu_tel,status,fee,person,connect_tel,school,diploma,major,id_number,age):
        self.click_student_manage_link()
        self.click_student_info_link()
        self.click_query_btn()
        self.click_modify_btn()
        self.input_box_stu_name(name)
        self.input_box_stu_tel(stu_tel)
        self.select_new_status(status)
        self.select_pay_fee(fee)
        self.input_connect_person(person)
        self.input_connect_tel(connect_tel)
        self.input_box_school(school)
        self.select_diploma(diploma)
        self.input_major(major)
        self.input_id_number(id_number)
        # self.click_graduate_time()
        self.input_stu_age(age)
        self.click_save_btn()

if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get('http://192.168.159.141:8080/WoniuBoss4.0')
    driver.maximize_window()
    driver.implicitly_wait(2)
    Service.miss_login(driver, '../config/base.conf')
    StudentInfo(driver).do_search_info('测试','全部','全部','吕布')


