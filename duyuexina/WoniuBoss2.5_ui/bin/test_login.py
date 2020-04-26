from selenium.webdriver.common.by import By
from lib.login import Login
from tools.service import Service
from tools.utility import Utility
from parameterized import parameterized
import unittest
import time


login_datas = Utility.get_json("../config/testdata.conf")
login_data = Utility.get_excel_GUI_tuple(login_datas[0])


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('../config/base.conf')
        Service.open_page(self.driver, '../config/base.conf')
        self.login = Login(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


    # 测试登录功能
    @parameterized.expand(login_data)

    def test_login(self, login_userName, login_userPASS, login_checkcode, login_expect):
        contents = {'username': login_userName, 'password': login_userPASS, 'checkcode': login_checkcode}
        self.login.excute_login(contents)
        # 断言
        if Service.is_element_present(self.driver, By.LINK_TEXT, '注销'):
            actual = 'success'
        elif self.driver.find_element_by_id('pwMsg').text == '用户名或密码错误':
            actual = 'error'
        elif self.driver.find_element_by_id('checkcodeMsg').text == '用户名或密码错误':
            actual = 'error'
        else:
            actual = 'error'
        self.assertEqual(actual, login_expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
