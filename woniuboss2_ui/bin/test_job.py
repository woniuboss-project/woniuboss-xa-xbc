
from parameterized import parameterized
import unittest
import time

# 获取测试数据
from woniuboss2_ui.lib.job import Job
from woniuboss2_ui.tools.service import Service
from woniuboss2_ui.tools.utility import Utility

jpb_datas = Utility.get_json('../config/testdata_dengyu.conf')
tech_data = Utility.get_excel_GUI_tuple(jpb_datas[11])
edit_one_data = Utility.get_excel_GUI_tuple(jpb_datas[12])
edit_two_data = Utility.get_excel_GUI_tuple(jpb_datas[13])
edit_three_data = Utility.get_excel_GUI_tuple(jpb_datas[14])

path = Service.choose_path()
class Testjob(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.miss_login(self.driver, path)
        self.driver.find_element_by_link_text(u'就业管理').click()
        self.job = Job(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # 技术面试
    @parameterized.expand(tech_data)
    def test_excute_tech(self, question, result, expect):
        contents = {'question': question, 'result': result}
        self.job.excute_tech(contents)
        sql_one = 'select question from skill_record where skillrecord_student_id="858"'
        result_one = Utility.query_one(path, sql_one)
        if contents['question'] == result_one[0]:
            actual = 'add-pass'
        else:
            actual = 'add-fail'
        self.assertEqual(actual, expect)

    # 就业管理查询
    def test_query_job(self):
        self.job.query_job_manager()
        if self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[1]').text == '谢竺颖':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    # 模拟面试
    @parameterized.expand(edit_one_data)
    def test_edit_job_one(self, name, data, content, expect):
        contents = {'name': name, 'data': data, 'content': content}
        self.job.edit_job_manager_one(contents)
        if self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[1]').text == '付文攀':
            actual = 'edit-pass'
        else:
            actual = 'edit-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(edit_two_data)
    def test_edit_job_two(self, date, content, expect):
        self.job.edit_job_manager_two(date, content)
        if self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[1]').text == '付文攀':
            actual = 'edit-pass'
        else:
            actual = 'edit-fail'
        self.assertEqual(actual, expect)

    @parameterized.expand(edit_three_data)
    def test_edit_job_three(self, date, salary, content, expect):
        self.job.edit_job_manager_three(date, salary, content)
        if self.driver.find_element_by_xpath('//table[@id="stuInfo_table1"]/tbody/tr[1]/td[1]').text == '付文攀':
            actual = 'edit-pass'
        else:
            actual = 'edit-fail'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
