from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.enterprise_manage import EnterpriseManage
import unittest
from parameterized import parameterized

# 获取测试数据
enterprise_manage_datas = Utility.get_json('..\\config\\testdata_deng.conf')
# 新增资源
enterprise_manage_add_datas = Utility.get_excel_to_tuple_url(enterprise_manage_datas[7])
# 修改资源
enterprise_manage_update_datas = Utility.get_excel_to_tuple_url(enterprise_manage_datas[8])
# 查询资源
enterprise_manage_query_datas = Utility.get_excel_to_tuple_url(enterprise_manage_datas[9])


class TestEnterPrise(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 新增资源
    @parameterized.expand(enterprise_manage_add_datas)
    def test_enterprise_manage_add(self, enterprise_manage_add_url, expect):
        enterprise_manage_add_resp = EnterpriseManage().enterprise_add(enterprise_manage_add_url)
        actual = enterprise_manage_add_resp
        # 断言
        self.assertEqual(actual, expect)

    # 修改资源
    @parameterized.expand(enterprise_manage_update_datas)
    def test_enterprise_manage_update(self, enterprise_manage_update_url, expect):
        enterprise_manage_update_resp = EnterpriseManage().enterprise_update(enterprise_manage_update_url)
        actual = enterprise_manage_update_resp
        # 断言
        self.assertEqual(actual, expect)

    # 查询资源
    @parameterized.expand(enterprise_manage_query_datas)
    def test_enterprise_manage_query(self, enterprise_manage_query_url, expect):
        enterprise_manage_query_resp = EnterpriseManage().enterprise_query(enterprise_manage_query_url)
        actual = enterprise_manage_query_resp
        # 断言
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
