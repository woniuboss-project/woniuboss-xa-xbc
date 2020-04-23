import unittest
from parameterized import parameterized

from woniuboss2.lib.renshi_manage import Hr
from woniuboss2.tools.utility import Utility

data_config_info = Utility.get_json('..\\config\\testdata.conf')
test_addstaff_info = Utility.get_excel_to_tuple(data_config_info[2])
test_querystaff_info = Utility.get_excel_to_tuple(data_config_info[3])
test_editstaff_info = Utility.get_excel_to_tuple(data_config_info[4])

class HrTest(unittest.TestCase):
    def setUp(self):
        self.hr = Hr()

    def tearDown(self):
        pass

    @parameterized.expand(test_addstaff_info)
    def test_addstaff(self, add_staff_url, post, add_staff_data, status_code, content):
        addstaff_resp = self.hr.add_staff(add_staff_url, add_staff_data)
        self.assertEqual(addstaff_resp.text, content)

    #查询0条，查询1条，查询部分，查询所有
    @parameterized.expand(test_querystaff_info)
    def test_querystaff(self, query_staff_url, post, query_staff_data, status_code, content):
        querystaff_resp = self.hr.query_staff(query_staff_url, query_staff_data)
        sql_all = 'select count(employee_id) from employee'
        all_staff_number = Utility.query_one('..\\config\\base.conf',sql_all)[0]
        sql_part = 'select count(employee_id) from employee where region_id=3'
        part_staff_number = Utility.query_one('..\\config\\base.conf', sql_part)[0]
        if querystaff_resp.json()['totalRow'] == 0:
            actual = 'query zero'
        elif querystaff_resp.json()['totalRow'] == 1:
            actual = 'query one'
        elif querystaff_resp.json()['totalRow'] == all_staff_number:
            actual = 'query all'
        elif querystaff_resp.json()['totalRow'] == part_staff_number:
            actual = 'query part'
        else:
            actual = 'query error'
        self.assertEqual(actual, content)

    @parameterized.expand(test_editstaff_info)
    def test_editstaff(self, edit_staff_url, post, edit_staff_data, status_code, content):
        editstaff_resp = self.hr.edit_staff(edit_staff_url, edit_staff_data)
        self.assertEqual(editstaff_resp.text, content)
