from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from parameterized import parameterized
import unittest
import time

# 获取测试数据
from woniuboss2_ui.lib.market import Market
from woniuboss2_ui.tools.service import Service
from woniuboss2_ui.tools.utility import Utility

market_datas = Utility.get_json("../config/testdata_dengyu.conf")
market_decode_data = Utility.get_excel_GUI_tuple(market_datas[1])
market_add_data = Utility.get_excel_GUI_tuple(market_datas[2])
market_upload_data = Utility.get_excel_GUI_tuple(market_datas[3])

path = Service.choose_path()
class TestMarket(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.miss_login(self.driver, path)
        self.driver.find_element_by_link_text(u'市场营销').click()
        self.market = Market(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # 解密功能
    @parameterized.expand(market_decode_data)
    def test_market_decode(self, vp, expect):
        self.market.excute_decode(vp)
        if '*' not in self.driver.find_element_by_xpath('//table[@id="netCus-table"]/tbody/tr[1]/td[1]').text:
            actual = 'solve-pass'
        else:
            actual = 'solve-fail'
        # 断言
        self.assertEqual(actual, expect)

    # 新增功能
    @parameterized.expand(market_add_data)
    def test_market_add(self, vp, phone, name, mail, qq, study, major, want, money, test, age, school, job, fllow,
                        expect):
        contents = {'vp': vp, 'phone': phone, 'name': name, 'mail': mail, 'qq': qq, 'study': study, 'major': major,
                    'want': want,
                    'money': money, 'test': test, 'age': age, 'school': school, 'job': job, 'fllow': fllow}
        self.market.excute_add_case(contents)
        time.sleep(50)
        if self.driver.find_element_by_css_selector('div.bootbox-body').text == '保存成功，但邮件未发送成功':
            actual = 'add-fail'
        elif self.driver.find_element_by_css_selector('div.bootbox-body').text == '程序出错':
            actual = 'add-fail'
        elif self.driver.find_element_by_css_selector('div.bootbox-body').text == '该资源已存在于系统中，请填写上最后跟踪记录点击保存':
            actual = 'add-fail'
        else:
            actual = 'add-fail'
        # 断言
        self.assertEqual(actual, expect)

    # 读取邮件
    def test_read_mail(self):
        self.market.excute_read_mail()
        try:
            if WebDriverWait(self.driver, 20, 1).until_not(
                    lambda dr: dr.find_element(By.CSS_SELECTOR, 'p.loading-title.txt-textOneRow')):
                actual = 'read-fail'
            else:
                actual = 'read-pass'
            # 断言
            self.assertEqual(actual, 'read-pass')
        except Exception as file:
            raise Exception

    # 上传文件
    @parameterized.expand(market_upload_data)
    def test_market_load(self, path, expect):
        self.market.excute_upload(path)
        if self.driver.find_element_by_xpath(
                '/html/body/div[9]/div/div/div[2]/div').text == '总共上传:1 有效数量:1 数据库重复数量:0  存入数量1':
            actual = 'upload-pass'
        else:
            actual = 'upload-fail'
        self.assertEqual(actual, expect)

    # 查询功能
    def test_market_query(self):
        self.market.excute_query()
        if self.driver.find_element_by_xpath('//table[@id="netCus-table"]/tbody/tr[1]/td[1]').text != '无符合条件的记录':
            actual = 'queru-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')


if __name__ == '__main__':
    unittest.main(verbosity=2)
