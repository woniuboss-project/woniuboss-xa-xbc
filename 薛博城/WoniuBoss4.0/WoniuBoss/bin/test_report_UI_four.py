import unittest
import time
from WoniuBoss.lib.login_four import Login
from WoniuBoss.lib.report_four import Report
from WoniuBoss.tools.service import Service
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
train_data=Utility.get_json('..\\config\\testdata_four.conf')
query_seek=Utility.get_excel_GUI_tuple(train_data[6])
query_market=Utility.get_excel_GUI_tuple(train_data[7])
query_teach=Utility.get_excel_GUI_tuple(train_data[8])
query_job=Utility.get_excel_GUI_tuple(train_data[9])

class Reporting(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI_four.conf')
        self.login=Login(self.driver)
        self.report=Report(self.driver)


    def tearDown(self):
        self.driver.quit()

    #咨询部——搜索
    @parameterized.expand(query_seek)
    def test_console_seek(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.report_do(seek_data)
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #咨询部——今日
    @parameterized.expand(query_seek)
    def test_console_today(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and create_time LIKE "2020-04-22%"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_today()
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #咨询部——本周
    @parameterized.expand(query_seek)
    def test_console_week(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and (create_time LIKE "2020-04-2%" OR create_time LIKE "2020-04-2%")   '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_week()
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #咨询部——本月
    @parameterized.expand(query_seek)
    def test_console_month(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and create_time like "2020-04%"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_month()
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)
    #咨询部——上周
    @parameterized.expand(query_seek)
    def test_console_lastweek(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and (create_time LIKE "2020-04-1%" OR create_time LIKE "2020-04-2%")'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_lastweek()
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    # 咨询部——上月
    @parameterized.expand(query_seek)
    def test_console_lastmonth(self, uname, upass, vcode, password, timeone, timetwo, expect):
        seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'timeone': timeone,
                     'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and create_time LIKE "2020-03%" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_lastmonth()
        resp = self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text == str(result[0]):
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #咨询部——本年
    @parameterized.expand(query_seek)
    def test_console_year(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(tracking_record_id) FROM tracking_record WHERE remark != "None" and create_time LIKE "2020%" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.click_year()
        resp=self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[7]')
        if resp.text==str(result[0]):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)


    #市场部——搜索
    @parameterized.expand(query_market)
    def test_market_seek(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE create_time like "2020-04-22%"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_do(seek_data)
        if result[0]==3:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #市场部——今日
    @parameterized.expand(query_seek)
    def test_market_today(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE create_time like "2020-04-22%" and work_id="WNCD005" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_today()
        if result[0]==3:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #市场部——本周
    @parameterized.expand(query_seek)
    def test_market_week(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE create_time like "2020-04-2%" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_week()
        if result[0]==3:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #市场部——本月
    @parameterized.expand(query_seek)
    def test_market_month(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE create_time like "2020-04%" and work_id="WNCD005"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_month()
        if result[0]==0:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)
    #市场部——上周
    @parameterized.expand(query_seek)
    def test_market_lastweek(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE "2020-04-16"<=create_time<="2020-04-22" and work_id="WNCD005"'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_lastweek()
        if result[0]==0:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #市场部——上月
    @parameterized.expand(query_seek)
    def test_market_lastmonth(self, uname, upass, vcode, password, timeone, timetwo, expect):
        seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'timeone': timeone,
                     'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE "2020-03-22"<=create_time<="2020-04-22" and work_id="WNCD005" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_lastmonth()
        if result[0]==0:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #市场部——本年
    @parameterized.expand(query_seek)
    def test_market_year(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        sql = f'select count(customer_id) FROM customer WHERE create_time LIKE "2020%" and work_id="WNCD005" '
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.market_year()
        if result[0]==0:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #教学部
    @parameterized.expand(query_teach)
    def test_teach(self,uname,upass,vcode, scour, direction,statue,expect):
        try:
            teach_data={'uname':uname,'upass':upass,'vcode':vcode,'scour': scour, 'direction': direction, 'statue': statue}
            self.login.do_login('..\\config\\base_UI_four.conf', teach_data)
            self.report.teaching(teach_data)
            resp=self.driver.find_element_by_id('phaseScore_table')
            if '无符合条件的记录' not in resp.text:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    #就业部-搜索
    @parameterized.expand(query_job)
    def test_job(self,uname,upass,vcode, area, timeone,timetwo,expect):
        try:
            job_data={'uname':uname,'upass':upass,'vcode':vcode,'area': area, 'timeone': timeone, 'timetwo': timetwo}
            self.login.do_login('..\\config\\base_UI_four.conf', job_data)
            self.report.job_do(job_data)
            resp = self.driver.find_element_by_id('jobTb')
            if '无符合条件的记录' not in resp.text:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    #就业——今日
    @parameterized.expand(query_seek)
    def test_job_today(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_today()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #就业——本周
    @parameterized.expand(query_seek)
    def test_job_week(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_week()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #就业——本月
    @parameterized.expand(query_seek)
    def test_job_month(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_month()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #就业——上周
    @parameterized.expand(query_seek)
    def test_job_lastweek(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_lastweek()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #就业——上月
    @parameterized.expand(query_seek)
    def test_job_lastmonth(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_lastmonth()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)
    #就业——本年
    @parameterized.expand(query_seek)
    def test_job_today(self,uname,upass,vcode,password, timeone, timetwo,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'timeone': timeone, 'timetwo': timetwo}
        self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
        self.report.job_year()
        resp = self.driver.find_element_by_id('jobTb')
        if '无符合条件的记录' not in resp.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)
