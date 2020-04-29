from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from parameterized import parameterized
import unittest
import time

# 获取测试数据
from woniuboss2_ui.lib.enterprise import Enterprise
from woniuboss2_ui.tools.service import Service
from woniuboss2_ui.tools.utility import Utility

enterprise_datas = Utility.get_json('../config/testdata_dengyu.conf')
enterprise_add_data = Utility.get_excel_GUI_tuple(enterprise_datas[4])
enterprise_edit_data = Utility.get_excel_GUI_tuple(enterprise_datas[5])
enterprise_query_data = Utility.get_excel_GUI_tuple(enterprise_datas[6])

path = Service.choose_path()
class TestEnterprise(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.miss_login(self.driver, path)
        self.driver.find_element_by_link_text(u'企业客户').click()
        self.enterprise = Enterprise(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # @parameterized.expand(enterprise_add_data)
    # def test_enterprise_add(self, newentname, newentcate, newentaddr, newentheade, newtel, newemail, neqq, expect):
    #     contents = {'newentname': newentname, 'newentcate': newentcate, 'newentaddr': newentaddr,
    #                 'newentheade': newentheade, 'newtel': newtel, 'newemail': newemail, 'neqq': neqq}
    #     self.enterprise.excute_add(contents)
    #     sql = 'select ent_name from enterprise_info where tel = "%s"' % contents['newtel']
    #     result = Utility.query_one('../config/base.conf', sql)
    #     print(result)
    #     if result[0] == contents['newentname']:
    #         actual = 'add-pass'
    #     else:
    #         actual = 'add-fail'
    #     self.assertEqual(actual, expect)

    # @parameterized.expand(enterprise_edit_data)
    # def test_enterprise_edit(self, entName, entCate, entAddr, entHeader, entTel, entEmail, entQq, expect):
    #     contents = {'entName': entName, 'entCate': entCate, 'entAddr': entAddr,
    #                 'entHeader': entHeader, 'entTel': entTel, 'entEmail': entEmail, 'entQq': entQq}
    #     self.enterprise.excute_edit(contents)
    #     sql = 'select ent_name from enterprise_info where tel = "%s"' % contents['entTel']
    #     result = Utility.query_one('../config/base.conf', sql)
    #     if result == contents['entName']:
    #         actual = 'edit-pass'
    #     else:
    #         actual = 'edit-fail'
    #     self.assertEqual(actual, expect)

    @parameterized.expand(enterprise_query_data)
    def test_enterprise_query(self, companyname, expect):
        self.enterprise.excute_query(companyname)
        if WebDriverWait(self.driver, 5, 1).until(
                lambda dr: dr.find_element(By.XPATH,
                                           '//table[@id="enterpriseTb"]/tbody/tr[1]/td[1]').text) == companyname:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
