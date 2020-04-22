from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from WoniuBoss4.lib.resource_public import ResourcePublic
from WoniuBoss4.tools.utility import Utility
from WoniuBoss4.tools.service import Service
from parameterized import parameterized
import unittest
import time

# 获取测试数据
resource_public_datas = Utility.get_json("../config/testdata.conf")
resource_public_query = Utility.get_excel_GUI_tuple(resource_public_datas[7])


class TestResourceTrain(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.miss_login(self.driver, '../config/base.conf')
        self.driver.find_element_by_link_text(u'资源管理').click()
        self.public = ResourcePublic(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    def test_resource_public_query_one(self):
        self.public.public_resource_query_one()
        if "成都" in WebDriverWait(self.driver, 10, 1).until(
                lambda dr: dr.find_element(By.XPATH, '//table[@id="public-pool-table"]/tbody/tr[1]/td[2]').text):
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    @parameterized.expand(resource_public_query)
    def test_resource_public_query_two(self, name):
        self.public.public_resource_query_two(name)
        if "%s" % name in WebDriverWait(self.driver, 10, 1).until(
                lambda dr: dr.find_element(By.XPATH, '//table[@id="public-pool-table"]/tbody/tr[1]/td[2]').text):
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_resource_claim(self):
        self.public.claim_resource()
        if '已成功认领1份资源，系统已将这些资源加入到您的临时池中' in \
                WebDriverWait(self.driver, 10, 1).until \
                            (lambda dr: dr.find_element \
                                    (By.CSS_SELECTOR,
                                     'html body.modal-open div.bootbox.modal.fade.mydialog.in div.modal-dialog.modal-sm') \
                                .text):
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')
