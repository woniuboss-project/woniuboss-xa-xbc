import unittest
from parameterized import parameterized

from WoniuBoss.lib.backstage_manage import Backstage
from WoniuBoss.tools.utility import Utility


data_config_info = Utility.get_json('..\\config\\testdata_du.conf')
test_addrole_info = Utility.get_excel_to_tuple(data_config_info[5])
test_queryuser_info = Utility.get_excel_to_tuple(data_config_info[6])


class BackstageTest(unittest.TestCase):
    def setUp(self):
        self.backstage = Backstage()

    def tearDown(self):
        pass

    @parameterized.expand(test_addrole_info)
    def test_add_role(self, add_role_url, post, add_role_data, status_code, content):
        add_role_resp = self.backstage.add_role(add_role_url, add_role_data)
        self.assertEqual(add_role_resp.text, content)

    # 查询0条，查询1条，查询所有
    @parameterized.expand(test_queryuser_info)
    def test_queryuser(self, query_user_url, post, query_user_data, status_code, content):
        queryuser_resp = self.backstage.query_user(query_user_url, query_user_data)
        sql_all = 'select count(id) from system_user'
        all_user_number = Utility.query_one('..\\config\\base.conf', sql_all)[0]
        if queryuser_resp.json()['totalRow'] == 0:
            actual = 'query zero'
        elif queryuser_resp.json()['totalRow'] == 1:
            actual = 'query one'
        elif queryuser_resp.json()['totalRow'] == all_user_number:
            actual = 'query all'
        else:
            actual = 'query error'
        self.assertEqual(actual, content)
