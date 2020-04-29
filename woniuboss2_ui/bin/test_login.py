from selenium.webdriver.common.by import By

from parameterized import parameterized
import unittest
import time

# 获取测试数据
from woniuboss2_ui.lib.login import Login
from woniuboss2_ui.tools.service import Service
from woniuboss2_ui.tools.utility import Utility

login_datas = Utility.get_json("../config/testdata_dengyu.conf")
login_data = Utility.get_excel_GUI_tuple(login_datas[0])

path = Service.choose_path()
class TestLogin(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.open_page(self.driver, path)
        self.login = Login(self.driver)

    def tearDown(self):
        print('test over')
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
