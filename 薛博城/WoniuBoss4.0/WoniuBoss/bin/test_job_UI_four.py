import unittest
import time

from WoniuBoss.lib.JOB_four import Job
from WoniuBoss.lib.login_four import Login

from WoniuBoss.tools.service import Service
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
train_data=Utility.get_json('..\\config\\testdata_four.conf')
query_seek=Utility.get_excel_GUI_tuple(train_data[10])
query_view=Utility.get_excel_GUI_tuple(train_data[11])
query_record=Utility.get_excel_GUI_tuple(train_data[12])
query_submit=Utility.get_excel_GUI_tuple(train_data[13])
query_add=Utility.get_excel_GUI_tuple(train_data[14])
query_bus=Utility.get_excel_GUI_tuple(train_data[15])
bus_add=Utility.get_excel_GUI_tuple(train_data[16])

class GET_JOB(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI_four.conf')
        self.login=Login(self.driver)
        self.job=Job(self.driver)


    def tearDown(self):
        self.driver.quit()

    #模拟面试-查询
    @parameterized.expand(query_seek)
    def test_simulation_seek(self,uname,upass,vcode,password, interview, classroom,name,code,expect):
        try:
            seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'interview': interview, 'classroom': classroom,'name':name,'code':code}
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.simulation_seek(seek_data)
            resp=self.driver.find_element_by_id('stuInfo_table')
            if '无符合条件的记录' not in resp.text:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    # 模拟面试-面试
    @parameterized.expand(query_view)
    def test_simulation_view(self, uname, upass, vcode, password, pay, link, remark, expect):
        try:
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'pay': pay,
                         'link': link, 'remark': remark}
            sql=f'select count(minterview_id) FROM mockinterview '
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.simulation_input(seek_data)
            new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if new_result[0] - result[0] ==1:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)
    #面试记录
    @parameterized.expand(query_record)
    def test_simulation_record(self, uname, upass, vcode, password, classroom, name, code, expect):
        try:
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'classroom': classroom,
                         'name': name, 'code': code}
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.records_click(seek_data)
            resp=self.driver.find_element_by_id('stuInfo_table')
            if '无符合条件的记录' not in resp.text:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    #提交协议签订
    @parameterized.expand(query_submit)
    def test_simulation_submit(self, uname, upass, vcode, password, num,agreement,  expect):
        try:
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'num':num,'agreement': agreement,}
            sql='select count(student_id) FROM student WHERE is_sign="1"'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.do_entry_information(seek_data)
            new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if new_result[0]!=result[0]:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    #新增就业
    @parameterized.expand(query_add)
    def test_simulation_add(self, uname, upass, vcode, password, num,work,utime,pay,inps,  expect):
        try:
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'num':num,'work': work,'utime':utime,'pay':pay,'inps':inps}
            sql='select count(job_regist_id) FROM job_register'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.add_entry_information(seek_data)
            new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if new_result[0]-result[0] ==1:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)
    #企业查询
    @parameterized.expand(query_bus)
    def test_simulation_bus(self, uname, upass, vcode, password, busine,  expect):
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'busine':busine}
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.find_business(seek_data)
            resp=self.driver.find_element_by_id('enterpriseTb')
            if busine in resp.text:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
    #新增企业
    @parameterized.expand(bus_add)
    def test_bus_add(self, uname, upass, vcode, password, buname,bucate,buaddr,buader,butel,expect):
        try:
            seek_data = {'uname': uname, 'upass': upass, 'vcode': vcode, 'passwd': password, 'buname':buname,'bucate':bucate,'buaddr':buaddr,'buader':buader,'butel':butel}
            sql = 'select count(enterprise_id) FROM enterprise_info'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
            time.sleep(5)
            self.job.busine_add(seek_data)
            new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if new_result[0] - result[0]==1:
                actual = 'success'
            else:
                actual = 'fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)