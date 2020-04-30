#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.student_center import StudentCenter
import unittest
from parameterized import parameterized

# 获取测试数据
student_center_datas = Utility.get_json('..\\config\\testdata_wang.conf')
print(student_center_datas)
#基本信息数据
essential_datas=Utility.get_excel_to_tuple(student_center_datas[0])
print(essential_datas)
#今日考勤数据
check_datas=Utility.get_excel_to_tuple(student_center_datas[1])
#今日晨考数据
morning_datas=Utility.get_excel_to_tuple(student_center_datas[2])
#学员请假数据
vacate_datas=Utility.get_excel_to_tuple(student_center_datas[3])
# 晨考记录数据
records_datas=Utility.get_excel_to_tuple(student_center_datas[4])
#测评阶段数据
appraisal_datas=Utility.get_excel_to_tuple(student_center_datas[5])
#测试记录数据
record_datas=Utility.get_excel_to_tuple(student_center_datas[6])
#班级管理数据
class_datas=Utility.get_excel_to_tuple(student_center_datas[7])
#课程安排数据
couser_datas=Utility.get_excel_to_tuple(student_center_datas[8])
class TestReportCenter(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 基本信息功能测试
    @parameterized.expand(essential_datas)
    def test_essential_report(self, essential_url, essential_data, essential_expect):
        essential_report_resp = StudentCenter().essential_report(essential_url, essential_data)
        # 断言
        if essential_report_resp == essential_expect:
            print("essential report test successful")
        else:
            print("essential report test fail")
    #今日考勤功能测试
    @parameterized.expand(check_datas)
    def test_check_report(self, check_url, check_data, check_expect):
        check_report_resp = StudentCenter().check_report(check_url, check_data)
        # 断言
        if check_report_resp == check_expect:
            print("check report test successful")
        else:
            print("check report test fail")
    # 今日晨考功能测试
    @parameterized.expand(morning_datas)
    def test_morning_report(self, morning_url, morning_data, morning_expect):
        morning_report_resp = StudentCenter().essential_report(morning_url, morning_data)
        # 断言
        if morning_report_resp == morning_expect:
            print("morning report test successful")
        else:
            print("morning report test fail")
    # 学员请假功能测试
    @parameterized.expand(vacate_datas)
    def test_vacate_report(self, vacate_url, vacate_data, vacate_expect):
        vacate_report_resp = StudentCenter().essential_report(vacate_url, vacate_data)
        # 断言
        if vacate_report_resp == vacate_expect:
            print("vacate report test successful")
        else:
            print("vacate report test fail")
    #晨考记录功能测试
    @parameterized.expand(records_datas)
    def test_records_report(self, records_url, records_data, records_expect):
        records_report_resp = StudentCenter().records_report(records_url, records_data)
        # 断言
        if records_report_resp == records_expect:
            print("records report test successful")
        else:
            print("records report test fail")
     # 测评阶段功能测试
    @parameterized.expand(appraisal_datas)
    def test_appraisal_report(self, appraisal_url, appraisal_data, appraisal_expect):
        appraisal_report_resp = StudentCenter().essential_report(appraisal_url, appraisal_data)
        # 断言
        if appraisal_report_resp == appraisal_expect:
            print("appraisal report test successful")
        else:
            print("appraisal report test fail")

    # 测评记录功能测试
    @parameterized.expand(record_datas)
    def test_record_report(self, record_url, record_data, record_expect):
        record_report_resp = StudentCenter().essential_report(record_url, record_data)
        # 断言
        if record_report_resp == record_expect:
            print("record report test successful")
        else:
            print("record report test fail")

    # 班级管理功能测试
    @parameterized.expand(class_datas)
    def test_class_report(self, class_url, class_data, class_expect):
        class_report_resp = StudentCenter().essential_report(class_url, class_data)
        # 断言
        if class_report_resp == class_expect:
            print("class report test successful")
        else:
            print("class report test fail")
    #课程安排功能测试
    @parameterized.expand(couser_datas)
    def test_couser_report(self, couser_url, couser_data, couser_expect):
        couser_report_resp = StudentCenter().couser_report(couser_url, couser_data)
        # 断言
        if couser_report_resp == couser_expect:
            print("couser report test successful")
        else:
            print("couser report test fail")

if __name__ == '__main__':
    unittest.main(verbosity=2)













