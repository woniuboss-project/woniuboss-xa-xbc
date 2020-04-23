import unittest

from selenium.webdriver.common.by import By

from WoniuBoss.lib.login_four import Login
from WoniuBoss.tools.service import Service
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
train_data=Utility.get_json('..\\config\\testdata_four.conf')
query_login=Utility.get_excel_GUI_tuple(train_data[0])
class Logining(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base_UI_four.conf')
        self.login=Login(self.driver)


    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(query_login)
    def test_login(self,uname,upass,vcode,expect):
        login_data={'uname':uname,'upass':upass,'vcode':vcode,}
        self.login.do_login('..\\config\\base_UI_four.conf',login_data)
        if Service.is_element_present(self.driver,By.ID,'btn-decrypt'):
            actual='success'
        else:
            actual='fail'
        self.assertEqual(actual,expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)