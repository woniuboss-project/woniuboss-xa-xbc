import time
from selenium.webdriver.common.by import By

import unittest

from parameterized import parameterized

from WoniuBoss4.lib.student_info import StudentInfo
from WoniuBoss4.tools.service import Service
from WoniuBoss4.tools.utility import Utility

test_config_info=Utility.get_json('../config/testdata.conf')
# search_stu_info = Utility.get_excel_GUI_tuple(test_config_info[1])

modify_stu_info = Utility.get_excel_GUI_tuple(test_config_info[2])

class StudentInfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Service.get_driver('../config/base.conf')
        cls.student_info = StudentInfo(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @parameterized.expand(search_stu_info)
    # def test_a_serach_stu_info(cls, orien_name,class_name,status_name,stu_name,expect):
    #     cls.student_info.do_search_info(orien_name,class_name,status_name,stu_name)
    #     time.sleep(2)
    #     if status_name == '全部':
    #         re_status = '%'
    #     elif status_name == '未开班':
    #         re_status = '01'
    #     elif status_name == '在校学习':
    #         re_status = '02'
    #     elif status_name == '转就业':
    #         re_status = '03'
    #     elif status_name == '已就业':
    #         re_status = '04'
    #     elif status_name == '已休学':
    #         re_status = '05'
    #     elif status_name == '已失联':
    #         re_status = '06'
    #     else:
    #         re_status = '07'
    #
    #     if stu_name == '':
    #         re_name = '%'
    #     else:
    #         re_name = stu_name
    #
    #     if class_name == '全部':
    #         re_class = '%'
    #     else:
    #         re_class = class_name
    #
    #     if orien_name == '全部':
    #         re_orien = '%'
    #     else:
    #         re_orien = orien_name
    #     sql = f"select count(*) from student where student_class_id in (select class_id from class where class_no like '{re_class}' " \
    #           f"and orientation like '{re_orien}') and status like '{re_status}' and student_name like '{re_name}%'"
    #     db_result = Utility.query_one('../config/base.conf',sql)
    #     sum_text = cls.driver.find_element_by_css_selector('#stuInfo > div.bootstrap-table > div.fixed-table-container'
    #                                                    '> div.fixed-table-pagination > div.pull-left.'
    #                                                    'pagination-detail > span.pagination-info').text
    #     if '总共' in sum_text:
    #         sum_num = sum_text.split('总共 ')[1].split(' 条')[0]
    #         if db_result[0] == int(sum_num):
    #             actual = 'test query student info pass'
    #         else:
    #             actual = 'test query student info fail'
    #     else:
    #         actual = 'test query student info fail'
    #     cls.assertEqual(expect,actual)

    @parameterized.expand(modify_stu_info)
    def test_b_modify_student_info(cls,name,stu_tel,status,fee,person,connect_tel,school,diploma,major,id_number,age,expect):
        cls.student_info.do_modify_student_info(name,stu_tel,status,fee,person,connect_tel,school,diploma,major,id_number,age)
        time.sleep(5)
        if Service.is_element_present(cls.driver,By.XPATH,'/html/body/div[12]/div/div/div[2]/div'):
            text = cls.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div').text
            print(text)
            if '操作成功' in text:
                actual = 'test modify student info pass'
            else:
                actual = 'test modify student info fail'
        else:
            actual = 'test modify student info fail'

        cls.driver.refresh()

        cls.assertEqual(expect,actual)

if __name__ == '__main__':
    unittest.main(verbosity=2)
