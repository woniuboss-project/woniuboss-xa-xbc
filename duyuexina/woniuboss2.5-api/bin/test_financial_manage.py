import unittest
from parameterized import parameterized
from woniuboss2.lib.financial_manage import Finance
from woniuboss2.tools.utility import Utility

data_config_info = Utility.get_json('..\\config\\testdata.conf')
test_addflow_info = Utility.get_excel_to_tuple(data_config_info[1])
test_queryflow_info = Utility.get_excel_to_tuple(data_config_info[7])
test_editflow_info = Utility.get_excel_to_tuple(data_config_info[8])

class FinancialTest(unittest.TestCase):
    def setUp(self):
        self.finance = Finance()

    def tearDown(self):
        pass

    @parameterized.expand(test_addflow_info)
    def test_addflow(self, addflow_url, post, addflow_data, status_code, content):
        addflow_resp = self.finance.add_flow(addflow_url, addflow_data)
        self.assertEqual(addflow_resp.text,content)

    # 按条件查询
    @parameterized.expand(test_queryflow_info)
    def test_querflow(self, query_flow_url, post, query_flow_data, status_code, content):
        queryflow_resp = self.finance.query_flow(query_flow_url, query_flow_data)
        sql_part01 = 'select count(detailed_id) from detailed_dealings where trading_time between "2018-05-29" and "2018-05-31"'
        part_flow_number01 = Utility.query_one('..\\config\\base.conf', sql_part01)[0]
        sql_part02 = 'select count(detailed_id) from detailed_dealings where trading_time between "2020-03-01" and "2020-03-31"'
        part_flow_number02 = Utility.query_one('..\\config\\base.conf', sql_part02)[0]
        sql_part03 = 'select count(detailed_id) from detailed_dealings where trading_time between "2020-04-01" and "2020-04-30"'
        part_flow_number03 = Utility.query_one('..\\config\\base.conf', sql_part03)[0]

        if queryflow_resp.json()['totalRow'] == part_flow_number01:
            actual = 'query part'
        elif queryflow_resp.json()['totalRow'] == part_flow_number02:
            actual = 'query lastmonth'
        elif queryflow_resp.json()['totalRow'] == part_flow_number03:
            actual = 'query thismonth'
        else:
            actual = 'query error'
        self.assertEqual(actual, content)

    @parameterized.expand(test_editflow_info)
    def test_editflow(self, edit_flow_url, post, edit_flow_data, status_code, content):
        editflow_resp = self.finance.edit_flow(edit_flow_url, edit_flow_data)
        if editflow_resp.text == '修改成功.':
            actual = 'edit success'
        else:
            actual = 'edit fail'
        self.assertEqual(actual, content)
