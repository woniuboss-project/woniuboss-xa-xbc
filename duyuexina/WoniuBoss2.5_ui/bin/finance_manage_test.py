from selenium.webdriver.common.by import By
from lib.finance_manage import FinanceManage
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
import unittest
import time


query_flow_datas = Utility.get_json("../config/testdata.conf")
query_data = Utility.get_excel_GUI_tuple(query_flow_datas[1])


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('../config/base.conf')
        Service.open_page(self.driver, '../config/base.conf')
        self.finance = FinanceManage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


    # 测试查询按钮
    @parameterized.expand(query_data)
    def test_login(self, one_subject, two_subject,expect):
        contents = {'one_subject': one_subject, 'two_subject': two_subject}
        self.finance.finance_query(contents)
        # 断言
        if not Service.is_element_present(self.driver, By.LINK_TEXT, '修改'):
            actual = 'query-pass'
        else:
            actual = 'quey-fail'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
