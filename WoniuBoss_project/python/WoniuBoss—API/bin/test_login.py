from woniuboss2.lib.login import Login
from woniuboss2.tools.utility import Utility
import unittest
from parameterized import parameterized
data_config_info = Utility.get_json('..\\config\\testdata.conf')
test_login_info = Utility.get_excel_to_tuple(data_config_info[0])

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.login = Login()

    def tearDown(self):
        pass

    @parameterized.expand(test_login_info)
    def test_login(self,login_url,post,login_data,status_code,content):
        login_resp = self.login.do_login(login_url, login_data)
        if 'success' in login_resp.text:
            actual = 'login-pass'
        else:
            actual = 'login-fail'

        self.assertEqual(actual,content)