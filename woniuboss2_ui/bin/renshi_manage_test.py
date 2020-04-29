import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By

from woniuboss2_ui.lib.renshi_manage import EmployManage
from woniuboss2_ui.tools.service import Service
from woniuboss2_ui.tools.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdataduyuexin.conf')
technical_interview_info = Utility.get_excel_GUI_tuple(test_config_info[2])
mock_interview_info = Utility.get_excel_GUI_tuple(test_config_info[3])

path = Service.choose_path()
class EmployTest(unittest.TestCase):

	def setUp(self):
		self.driver = Service.get_driver(path)
		self.employ = EmployManage(self.driver)

	def tearDown(self):
		self.driver.quit()

	@parameterized.expand(technical_interview_info)
	def test_technical_interview(self, q_content, e_content,expect):
		technical_interview_data = {'question_content': q_content,'evalute_content': e_content}
		# 执行技术面试的操作
		self.employ.technical_interview(path,technical_interview_data)

		if Service.is_element_present(self.driver, By.CSS_SELECTOR,'.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
			time.sleep(2)
			content = self.driver.find_element_by_css_selector('.bootbox-body').text
			if '不能为空' in content:
				actual = 'interview_fail'
				self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button').click()
			else:
				actual = 'interview_success'
				self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button').click()
		else:
			contents = self.driver.find_element_by_css_selector('#skill_table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)').text
			if '无符合条件' in contents:
				actual = 'interview_fail'
			else:
				actual = 'interview_success'
		self.assertEqual(actual, expect)

	@parameterized.expand(mock_interview_info)
	def test_mock_interview(self,money,remark,expect):
		mock_interview_data = {'salary': money, 'mremark': remark}
		# 执行技术面试的操作
		self.employ.mock_interview(path,mock_interview_data)
		if Service.is_element_present(self.driver, By.CSS_SELECTOR, '#stuInfo_table1 > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > button:nth-child(1)'):
			actual = 'mock_success'
		else:
			actual = 'mock_fail'
		self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)