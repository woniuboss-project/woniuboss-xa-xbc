from WoniuBoss4.lib.resource_train import ResourceTrain
from WoniuBoss4.tools.utility import Utility
from WoniuBoss4.tools.service import Service
from parameterized import parameterized
import unittest
import time

# 获取测试数据
resoure_train_datas = Utility.get_json("../config/testdata.conf")
resoure_train_add = Utility.get_excel_GUI_tuple(resoure_train_datas[0])
resoure_train_tail = Utility.get_excel_GUI_tuple(resoure_train_datas[1])
resoure_train_edit = Utility.get_excel_GUI_tuple(resoure_train_datas[2])
resoure_train_query_one = Utility.get_excel_GUI_tuple(resoure_train_datas[3])
resoure_train_query_two = Utility.get_excel_GUI_tuple(resoure_train_datas[4])


class TestResourceTrain(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.miss_login(self.driver, '../config/base.conf')
        self.driver.find_element_by_link_text(u'资源管理').click()
        self.train = ResourceTrain(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # 新增资源
    @parameterized.expand(resoure_train_add)
    def test_resource_train_add(self, tel, name, expect):
        self.train.excute_add_train_resource(tel, name)
        length = len(self.driver.find_element_by_id('personal-table'))
        for i in range(1, length):
            if self.driver.find_element_by_xpath(f'//table[@id="personal-table"]/tobody/tr{i}/td[2]').text == '嘻嘻':
                actual = 'add-pass'
            else:
                actual = 'add-fail'
            # 断言
            self.assertEqual(actual, expect)

    # 废弃资源
    def test_resource_train_abandon(self):
        sql_one = 'select count(abandon_record_id) from abandon_record'
        result_one = Utility.query_one('../config/base.conf', sql_one)
        self.train.excute_abandon_button()
        sql_two = 'select count(abandon_record_id) from abandon_record'
        result_two = Utility.query_one('../config/base.conf', sql_two)
        if result_two[0] - result_one[0] > 0:
            actual = 'abandon-pass'
        else:
            actual = 'abandon-fail'
        self.assertEqual(actual, 'abandon-pass')

    # 跟踪资源
    @parameterized.expand(resoure_train_tail)
    def test_resource_train_tail(self, content):
        self.train.excute_tail(content)
        if self.driver.find_element_by_xpath('//table[@id="personal-table"]/tbody/tr[1]/td[14]/span').text == 'ok':
            actual = 'tail-pass'
        else:
            actual = 'tail-fail'
        self.assertEqual(actual, 'query-pass')

    # 修改资源
    @parameterized.expand(resoure_train_edit)
    def test_resource_train_edit(self, name, tel, expect):
        self.train.excute_edit(name, tel)
        length = len(self.driver.find_element_by_id('personal-table'))
        for i in range(1, length):
            if self.driver.find_element_by_xpath(f'//table[@id="personal-table"]/tobody/tr{i}/td[2]').text == '妮妮':
                actual = 'add-pass'
            else:
                actual = 'add-fail'
            # 断言
            self.assertEqual(actual, expect)

    # 搜索资源
    def test_resource_train_equery_one(self):
        self.train.select_query_resource()
        if len(self.driver.find_element_by_id('personal-table')) > 1:
            actual = 'query-pass'
        elif self.driver.find_element_by_xpath(
                '/html/body/div[15]/div/div/div[2]/div').text == '该页面不展示公共池资源，若需查看，可至公共资源模块查看详情':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_resource_train_equery_two(self):
        self.train.selector_query_status()
        if len(self.driver.find_element_by_id('personal-table')) > 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_resource_train_equery_three(self):
        self.train.selector_query_source()
        if len(self.driver.find_element_by_id('personal-table')) > 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    @parameterized.expand(resoure_train_query_one)
    def test_resource_train_equery_four(self, s_time, e_time):
        self.train.input_query_date(s_time, e_time)
        if len(self.driver.find_element_by_id('personal-table')) > 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    @parameterized.expand(resoure_train_query_two)
    def test_resource_train_equery_five(self, data):
        self.train.input_query_information(data)
        if len(self.driver.find_element_by_id('personal-table')) > 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_resource_train_equery_six(self):
        self.train.selector_query_combination()
        if self.driver.find_element_by_xpath('//tale[@id="personal-table"]/tbody/tr[1]/td[2]').text == '力力':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')


if __name__ == '__main__':
    unittest.main(verbosity=2)
