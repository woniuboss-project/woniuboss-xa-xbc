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

class GET_JOB(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI_four.conf')
        self.login=Login(self.driver)
        self.job=Job(self.driver)


    def tearDown(self):
        self.driver.quit()

    # #模拟面试-查询
    # @parameterized.expand(query_seek)
    # def test_simulation_seek(self,uname,upass,vcode,password, interview, classroom,name,code,expect):
    #     seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'interview': interview, 'classroom': classroom,'name':name,'code':code}
    #     self.login.do_login('..\\config\\base_UI_four.conf', seek_data)
    #     time.sleep(5)
    #     self.job.simulation_seek(seek_data)
    #     resp=self.driver.find_element_by_id('stuInfo_table')
    #     if '无符合条件的记录' not in resp.text:
    #         actual = 'success'
    #     else:
    #         actual = 'fail'
    #     self.assertEqual(actual, expect)

    # 模拟面试-查询
    @parameterized.expand(query_view)
    def test_simulation_seek(self, uname, upass, vcode, password, pay, link, remark, expect):
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
    #面试记录
    @parameterized.expand(query_record)
    def test_simulation_record(self, uname, upass, vcode, password, classroom, name, code, expect):
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




if __name__ == '__main__':
    unittest.main(verbosity=2)