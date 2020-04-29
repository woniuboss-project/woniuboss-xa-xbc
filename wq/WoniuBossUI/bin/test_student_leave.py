#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium.webdriver.common.by import By
from WoniuBossui.tools.utility import Utility
from WoniuBossui.tools.service import Service
from WoniuBossui.lib.student_leave import StudentLeave
from parameterized import parameterized
import unittest
import time

# 获取测试数据
student_leave_datas = Utility.get_json("../config/testdata.conf")
student_leave_data = Utility.get_excel_GUI_tuple(student_leave_datas[2])

class TestLeave(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.open_page(self.driver, '../config/base.conf')
        self.leave = StudentLeave(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    @parameterized.expand(student_leave_data)
    def test_student_leave(self,childdate,childdates,day,uname,cause,idea,expect):
        contents = {'childdate': childdate, 'childdates': childdates,
                    'day':day,'uname':uname,'cause':cause,'idea':idea}
        self.leave.excute_leave(contents)
        if self.driver.driver.find_element_by_css_selector('driver.find_element_by_css_selector').text=='唐一':
            actual = 'success'
        else:
            actual = 'error'
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)

