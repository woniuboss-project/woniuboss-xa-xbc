from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.enterprise_manage import EnterpriseManage
import unittest
from parameterized import parameterized

# 获取测试数据
enterprise_manage_datas = Utility.get_json('..\\config\\testdata.conf')
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
        # 断言
        if enterprise_manage_add_resp == expect:
            print("enterprise manage add test success")
        else:
            print("enterprise manage add test fail")

    # 修改资源
    @parameterized.expand(enterprise_manage_update_datas)
    def test_enterprise_manage_update(self, enterprise_manage_update_url, expect):
        enterprise_manage_update_resp = EnterpriseManage().enterprise_update(enterprise_manage_update_url)
        # 断言
        if enterprise_manage_update_resp == expect:
            print("enterprise manage update test success")
        else:
            print("enterprise manage update test fail")

    # 查询资源
    @parameterized.expand(enterprise_manage_query_datas)
    def test_enterprise_manage_query(self, enterprise_manage_query_url, expect):
        enterprise_manage_query_resp = EnterpriseManage().enterprise_query(enterprise_manage_query_url)
        # 断言
        if enterprise_manage_query_resp == expect:
            print("enterprise manage query test success")
        else:
            print("enterprise manage query test fail")


if __name__ == '__main__':
    unittest.main(verbosity=2)
