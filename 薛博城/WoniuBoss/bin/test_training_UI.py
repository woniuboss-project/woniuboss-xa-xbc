import unittest
import time
from selenium.webdriver.common.by import By

from WoniuBoss.lib.training_ui import Train
from WoniuBoss.tools.service import Service
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
train_data=Utility.get_json('..\\config\\testdata.conf')
query_seek=Utility.get_excel_GUI_tuple(train_data[0])
query_add=Utility.get_excel_GUI_tuple(train_data[1])
query_edit=Utility.get_excel_GUI_tuple(train_data[2])
query_tail=Utility.get_excel_GUI_tuple(train_data[3])
query_delt=Utility.get_excel_GUI_tuple(train_data[4])

query_deliver=Utility.get_excel_GUI_tuple(train_data[5])
query_look=Utility.get_excel_GUI_tuple(train_data[6])


query_public=Utility.get_excel_GUI_tuple(train_data[7])

query_resource=Utility.get_excel_GUI_tuple(train_data[8])
query_prorate=Utility.get_excel_GUI_tuple(train_data[9])
print(query_prorate)

class Training(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI.conf')
        self.train=Train(self.driver)


    def tearDown(self):
        self.driver.quit()

    #查询
    @parameterized.expand(query_seek)
    def test_login(self, password, pool, name, status, source, data1, data2, text_want, expect):
        seek_data = {'passwd': password, 'pool': pool, 'name': name, 'status': status, 'source': source,
                     'data_time1': data1, 'data_time2': data2, 'text_want': text_want}
        self.train.seek('..\\config\\base_UI.conf', seek_data)
        body=self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr')
        print(body.text)
        if name in body.text:
            actual = 'success'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #新增
    @parameterized.expand(query_add)
    def test_add(self,password,phone,name,condition,SOURCE,expect):
        add_data={'passwd': password, 'phone': phone, 'name': name, 'condition': condition, 'SOURCE': SOURCE}
        #查询新增之前的总数
        sql = f'select count(customer_id) from customer'
        result = Utility.query_one('..\\config\\base_UI.conf', sql)
        self.train.add_student('..\\config\\base_UI.conf',add_data)
        new_result=Utility.query_one('..\\config\\base_UI.conf', sql)
        if new_result[0] - result [0] ==1:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #修改
    @parameterized.expand(query_edit)
    def test_edit(self,password,name,phone,intention,workage,expect):
        edit_data={'passwd': password, 'name': name, 'phone': phone, 'intention': intention,'workage':workage}
        sql = f'select count(customer_id) from customer'
        result = Utility.query_one('..\\config\\base_UI.conf', sql)
        self.train.edit_customer('..\\config\\base_UI.conf',edit_data)
        new_result = Utility.query_one('..\\config\\base_UI.conf', sql)
        resp=self.driver.find_element_by_css_selector('#personal-table > tbody:nth-child(2)')
        if new_result[0] - result[0] != 1 and name in resp.text:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #跟踪
    @parameterized.expand(query_tail)
    def test_tail(self,password,state,priority,record,expect):
        tail_data={'passwd': password, 'state': state, 'priority': priority, 'record': record}
        sql = f'select count(customer_id) from customer'
        result = Utility.query_one('..\\config\\base_UI.conf', sql)
        self.train.do_tail('..\\config\\base_UI.conf',tail_data)
        new_result = Utility.query_one('..\\config\\base_UI.conf', sql)
        resp=self.driver.find_element_by_css_selector('#personal-table > tbody:nth-child(2)')
        # print(resp.text)
        if new_result[0] - result[0] != 1 and record in resp.text:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    @parameterized.expand(query_delt)
    def test_delt(self,password,pool,num,pool_1,expect):
        tail_data = {'passwd': password,'pool':pool,'num':int(num),'pool_1':pool_1}
        self.train.do_delt('..\\config\\base_UI.conf',tail_data)
        resp=self.driver.find_element_by_class_name('pagination-info')
        if '0' not in resp.text:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #转交责任人提交
    @parameterized.expand(query_deliver)
    def test_deliver(self,password,name,region,status,source,name_2,region_2,num,expect):
        try:
            deliver_data={'passwd': password, 'name': name, 'region': region, 'status': status,'source':source,'name_2':name_2,'region_2':region_2,'num':num}
            sql = f'select count(customer_id) from customer'
            result = Utility.query_one('..\\config\\base_UI.conf', sql)
            self.train.do_submit('..\\config\\base_UI.conf',deliver_data)
            new_result = Utility.query_one('..\\config\\base_UI.conf', sql)
            if result[0] - new_result[0] !=1:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual,expect)

    #转交责任人查询
    @parameterized.expand(query_look)
    def test_look(self,password,ucus,expect):
        look_data={'passwd': password, 'ucus': ucus}
        self.train.do_look('..\\config\\base_UI.conf',look_data)
        resp=self.driver.find_element_by_id('resumeDivId')
        if ucus in resp.text:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #公共资源池认领
    @parameterized.expand(query_public)
    def test_public(self,password,name,status,source,ucus,num,expect):
        claim_data = {'passwd': password, 'name': name, 'status': status, 'source': source, 'ucus': ucus,'num':num}
        sql = f'select count(customer_id) from customer'
        result = Utility.query_one('..\\config\\base_UI.conf', sql)
        self.train.do_claim('..\\config\\base_UI.conf',claim_data)
        resp=self.driver.find_element_by_id('public-pool-table')
        self.train.affirm_claim()
        new_result = Utility.query_one('..\\config\\base_UI.conf', sql)
        if ucus not in resp.text and new_result[0]-result[0]!=1:
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)

    #分配提交
    @parameterized.expand(query_resource)
    def test_resource(self,password,source,ucus,num,name,expect):
        try:
            res_data={'passwd': password, 'source': source, 'ucus': ucus, 'num': num, 'name': name}
            sql = f'select count(customer_id) from customer'
            result = Utility.query_one('..\\config\\base_UI.conf', sql)
            self.train.resource_submit('..\\config\\base_UI.conf',res_data)
            resp=self.driver.find_element_by_id('allot-table')
            new_result = Utility.query_one('..\\config\\base_UI.conf', sql)
            if ucus not in resp.text and result[0]-new_result[0]!=1:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual, expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual,expect)

    #按比例分配
    @parameterized.expand(query_prorate)
    def test_prorate(self,password,proportion0,proportion1,proportion2,proportion3,proportion4,proportion5,expect):
        try:
            pro_data={'passwd': password, 'proportion0': proportion0, 'proportion1': proportion1, 'proportion2': proportion2, 'proportion3': proportion3,'proportion4':proportion4,'proportion5':proportion5}
            self.train.do_resource('..\\config\\base_UI.conf',pro_data)
            resp=self.driver.find_element_by_id('allot-table')
            if resp.text != None:
                actual='success'
            else:
                actual='fail'
            self.assertEqual(actual,expect)
        except Exception as e:
            actual = 'fail'
            self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)

