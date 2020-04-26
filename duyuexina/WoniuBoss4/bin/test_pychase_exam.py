
from selenium.webdriver.common.by import By
import unittest
from parameterized import parameterized
from WoniuBoss4.lib.pychase_exam import PhaseExam
from WoniuBoss4.tools.service import Service
from WoniuBoss4.tools.utility import Utility

test_config_info=Utility.get_json('../config/testdata.conf')
import_sigle_phase_info = Utility.get_excel_GUI_tuple(test_config_info[3])


class PhaseExamTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Service.get_driver('../config/base.conf')
        cls.phase_exam = PhaseExam(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @parameterized.expand(import_sigle_phase_info)
    def test_a_entry_sigle_phase_exam(self,class_name,score,phase,comment,expect):
        self.phase_exam.do_entry_sigle_phase_exam(class_name,score,phase,comment)
        if Service.is_element_present(self.driver,By.CSS_SELECTOR,'body > div.bootbox.modal.fade.mydialog.in > '
                                                                  'div > div'):
            actual = 'test import sigle phase exam fail'
            self.driver.refresh()
        else:
            ele = self.driver.find_element_by_css_selector( '#pe-result > tbody > tr:nth-child(1) > '
                                                            'td:nth-child(9) > button')
            attr = ele.get_attribute('onclick')
            attr_dict = attr.split('(')[1].split(')')[0]
            import json
            dict_attr = json.loads(attr_dict, encoding='utf-8')
            student_id = dict_attr['student_id']
            phase1_score = dict_attr['phase1']
            phase2_score = dict_attr['phase2']
            phase3_score = dict_attr['phase3']
            phase4_score = dict_attr['phase4']
            sql = f"select score from phase_exam where phase_exam_student_id ='{student_id}' and phase_exam_class_id = '1' order by phase asc"
            db_result = Utility.query_all('../config/base.conf', sql)
            num = len(db_result)
            if num == 1:
                if float(db_result[0][0]) == float(phase1_score):
                    actual = 'test import sigle phase exam pass'
                else:
                    actual = 'test import sigle phase exam fail'
            elif num == 2:
                if float(db_result[0][0]) == float(phase1_score) and float(db_result[1][0]) == float(phase2_score):
                    actual = 'test import sigle phase exam pass'
                else:
                    actual = 'test import sigle phase exam fail'
            elif num == 3:
                if float(db_result[0][0]) == float(phase1_score) and float(db_result[1][0]) == float(phase2_score) and \
                        float(db_result[2][0]) == float(phase3_score):
                    actual = 'test import sigle phase exam pass'
                else:
                    actual = 'test import sigle phase exam fail'
            elif num == 4:
                if float(db_result[0][0]) == float(phase1_score) and float(db_result[1][0]) == float(phase2_score) and float(db_result[2][0]) == float(phase3_score)\
                         and float(db_result[3][0]) == float(phase4_score):
                    actual = 'test import sigle phase exam pass'
                else:
                    actual = 'test import sigle phase exam fail'
            else:
                actual = 'test import sigle phase exam fail'
        self.assertEqual(expect,actual)

if __name__ == '__main__':
    unittest.main(verbosity=2)