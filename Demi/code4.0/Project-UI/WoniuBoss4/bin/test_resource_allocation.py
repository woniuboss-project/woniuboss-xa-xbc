from WoniuBoss4.lib.resource_allocation import ResourceAllocation
from WoniuBoss4.tools.utility import Utility
from WoniuBoss4.tools.service import Service
from parameterized import parameterized
import unittest
import time

# 获取测试数据
resource_allocation_datas = Utility.get_json("../config/testdata.conf")
resource_allocation_query = Utility.get_excel_GUI_tuple(resource_allocation_datas[6])


class TestResourceTrain(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.miss_login(self.driver, '../config/base.conf')
        self.driver.find_element_by_link_text(u'资源管理').click()
        self.allocation = ResourceAllocation(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    def test_alloacation_query_one(self):
        self.allocation.allocation_query_one()
        sql = 'select count(work_id) from customer'
        result = Utility.query_one('../config/base.conf', sql)
        if result[0] == 8:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_alloacation_query_two(self):
        self.allocation.allocation_query_two()
        sql = 'select count(source) from customer where work_id="0"'
        result = Utility.query_one('../config/base.conf', sql)
        if result[0] == 8:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    @parameterized.expand(resource_allocation_query)
    def test_alloacation_query_three(self, name):
        self.allocation.allocation_query_three(name)
        sql = 'select count(*) from customer where name="%s"' % name
        result = Utility.query_one('../config/base.conf', sql)
        if result[0] == 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_alloacation_commit_one(self, ):
        self.allocation.excute_manual_commit()
        sql = 'select work_id from customer where name="ww"'
        result = Utility.query_one('../config/base.conf', sql)
        if result[0] != 0:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_alloacation_commit_two(self):
        self.allocation.excute_ratio_commit()
        sql = 'select work_id from customer'
        result = Utility.query_one('../config/base.conf', sql)
        if 0 not in result:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')
