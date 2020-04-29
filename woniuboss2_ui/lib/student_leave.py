#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2_ui.tools.service import Service


class StudentLeave:

    def __init__(self, driver):
        self.driver = driver

    def click_student_manage_link(self):
        self.driver.find_element_by_link_text('学员管理').click()
        self.driver.find_element_by_link_text('学员请假').click()
        self.driver.find_element_by_link_text('新增请假').click()

    def input_time_begin(self,childdate):

        Service.remove_readonly(self.driver, 'childdate')
        childdate_one = self.driver.find_element_by_css_selector('#leave-form > '
                                                                 'div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
        Service.send_input(childdate_one, childdate)
    def input_time_finish(self,childdates):
        Service.remove_readonly(self.driver, 'childdate')
        childdate_tow = self.driver.find_element_by_css_selector('#leave-form > div:nth-child(2) >'
                                                                 ' div:nth-child(2) > input:nth-child(2)')
        Service.send_input(childdate_tow, childdates)
    #随机请假类型
    def select_type(self):
        type_select = self.driver.find_element_by_css_selector('#leave-form > div:nth-child(3) >'
                                                               ' div:nth-child(1) > select:nth-child(2)')
        Service.select_random(type_select)
    def input_leave_demo(self,day):
        u_day=self.driver.find_element_by_css_selector('#leave-form > div:nth-child(3) >'
                                                       ' div:nth-child(2) > input:nth-child(2)')
        Service.send_input(u_day, day)
    def input_leave_name(self,uname):
        u_name = self.driver.find_element_by_css_selector('#leave-form > div:nth-child(4) > '
                                                          'div:nth-child(1) > input:nth-child(2)')
        Service.send_input(u_name, uname)
    def input_leave_cause(self,cause):
        u_cause = self.driver.find_element_by_css_selector('#leave-form > div:nth-child(5) >'
                                                           ' div:nth-child(1) > textarea:nth-child(2)')
        Service.send_input(u_cause, cause)
    def input_leave_idea(self,idea):
        u_idea = self.driver.find_element_by_css_selector('#leave-form > div:nth-child(6) > '
                                                          'div:nth-child(1) > textarea:nth-child(2)')
        Service.send_input(u_idea, idea)
    def link_save(self):
        self.driver.find_element_by_css_selector('#leave-modal > div:nth-child(1) > div:nth-child(1) > '
                                                 'div:nth-child(3) > button:nth-child(1)')
    #新增请假功能实现
    def excute_leave(self,contents):
        self.click_student_manage_link()
        self.input_time_begin(contents['childdate'])
        self.input_time_finish('childdates')
        self.select_type()
        self.input_leave_demo(day=1)
        self.input_leave_name('唐一')
        self.input_leave_idea('idea')
        self.link_save()



