#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

#学员管理
from WoniuBoss.tools.service import Service


class StudentCenter:

    def __init__(self):
        self.session = Service.get_session(0)

    #基本信息
    def essential_report(self,essential_report_url,essential_report_data):
        return self.session.post(essential_report_url,essential_report_data).text
    #今日晨考
    def morning_report(self,morning_report_url,morning_report_data):
        return self.session.post(morning_report_url, morning_report_data).text
    #学员请假
    def vacate_report(self,vacate_report_url,vacate_report_data):
        return self.session.post(vacate_report_url, vacate_report_data).text
    #测评阶段
    def appraisal_report(self,appraisal_report_url,appraisal_report_data):
        return self.session.post(appraisal_report_url, appraisal_report_data).text
    #测评记录
    def record_report(self,record_report_url,record_report_data):
        return self.session.post(record_report_url, record_report_data).text
    #班级管理
    def class_report(self,class_report_url,class_report_data):
        return self.session.post(class_report_url, class_report_data).text


