import unittest
import time
from WoniuBoss.lib.login_four import Login
from WoniuBoss.lib.marketing_four import Market
from WoniuBoss.tools.service import Service
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
train_data=Utility.get_json('..\\config\\testdata_four.conf')
query_seek=Utility.get_excel_GUI_tuple(train_data[1])
query_add=Utility.get_excel_GUI_tuple(train_data[2])
query_edit=Utility.get_excel_GUI_tuple(train_data[3])
quert_upload=Utility.get_excel_GUI_tuple(train_data[4])
query_email=Utility.get_excel_GUI_tuple(train_data[5])

class Marketing(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI_four.conf')
        self.login=Login(self.driver)
        self.market=Market(self.driver)


    def tearDown(self):
        self.driver.quit()

    # #查询
    @parameterized.expand(query_seek)
    def test_seek(self, uname,upass,vcode,password, region, status, source, time1, time2, content,expect):
        seek_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'region': region, 'status': status, 'source': source, 'time1': time1,
                     'time2': time2, 'content': content }
        self.login.do_login('..\\config\\base_UI_four.conf',seek_data)
        self.market.do_seek(seek_data)
        resp=self.driver.find_element_by_id('netCus-table')
        if content in resp.text or '无符合条件的记录'not in resp.text :
            actual='success'
        else:
            actual = 'fail'
        self.assertEqual(actual,expect)

    #新增
    @parameterized.expand(query_add)
    def test_add(self,uname,upass,vcode,password, region, section, tel, name, status, expect):
        try:
            add_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'region': region, 'section': section, 'tel': tel, 'name': name,'status':status}
            sql = f'select count(customer_id) from customer'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf',add_data)
            time.sleep(5)
            self.market.add_do(add_data)
            resp = self.driver.find_element_by_id('netCus-table')
            new_result=Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if name in resp.text and new_result[0]-result[0]==1:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual='fail'
            self.assertEqual(actual, expect)

    #修改
    @parameterized.expand(query_edit)
    def test_edit(self,uname,upass,vcode,password, region, section, tel, name, status, expect):
        try:
            edit_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'region': region, 'section': section, 'tel': tel, 'name': name,'status':status}
            sql = f'select count(customer_id) from customer'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf',edit_data)
            time.sleep(5)
            self.market.edit_do(edit_data)
            resp = self.driver.find_element_by_id('netCus-table')
            new_result=Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if name in resp.text and new_result[0]-result[0]!=1:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual='fail'
            self.assertEqual(actual, expect)

    #提交文件
    @parameterized.expand(quert_upload)
    def test_upload(self,uname,upass,vcode,password, region, section,xsl,expect):
        try:
            xls_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password, 'region': region, 'section': section, 'xsl':xsl}
            sql = f'select count(customer_id) from customer'
            result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            self.login.do_login('..\\config\\base_UI_four.conf', xls_data)
            time.sleep(5)
            self.market.upload_do(xls_data)
            new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
            if new_result[0]-result[0]>1:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

    #邮件读取
    @parameterized.expand(query_email)
    def test_email(self,uname,upass,vcode,password,expect):
        email_data={'uname':uname,'upass':upass,'vcode':vcode,'passwd': password}
        sql = f'select count(customer_id) from customer'
        result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        self.login.do_login('..\\config\\base_UI_four.conf', email_data)
        time.sleep(5)
        self.market.email_read(email_data)
        time.sleep(10)
        new_result = Utility.query_one('..\\config\\base_UI_four.conf', sql)
        if new_result[0]-result[0]>1:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)









if __name__ == '__main__':
    unittest.main(verbosity=2)
