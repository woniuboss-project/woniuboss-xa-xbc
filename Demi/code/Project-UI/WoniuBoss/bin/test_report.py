from WoniuBoss.lib.report import Report
from WoniuBoss.tools.utility import Utility
from WoniuBoss.tools.service import Service
from parameterized import parameterized
import unittest
import time

# 获取测试数据
date_datas = Utility.get_json('../config/testdata.conf')
console_data = Utility.get_excel_GUI_tuple(date_datas[7])
sale_data = Utility.get_excel_GUI_tuple(date_datas[8])
market_data = Utility.get_excel_GUI_tuple(date_datas[9])
job_data = Utility.get_excel_GUI_tuple(date_datas[10])


class TestReport(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.miss_login(self.driver, '../config/base.conf')
        self.driver.find_element_by_link_text(u'报表中心').click()
        self.report = Report(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # 咨询部
    @parameterized.expand(console_data)
    def test_console_query_one(self, starttime, endtime, expect):
        self.report.click_console()
        # 搜索
        self.report.input_console_date(starttime, endtime)
        self.report.click_cnsole_query()
        sql_one = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_one = Utility.query_one('../config/base.conf', sql_one)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_one[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

    def test_console_query_two(self):
        self.report.click_console()
        # 当期
        self.report.click_evedate_console()
        sql_two = 'select count(last_status) from customer where work_id="11" and last_status="已认领"'
        result_two = Utility.query_one('../config/base.conf', sql_two)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[1]/td[9]').text == result_two[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_three(self):
        self.report.click_console()
        # 今日
        self.report.click_eveday_console()
        sql_three = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_three = Utility.query_one('../config/base.conf', sql_three)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_three[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_four(self):
        self.report.click_console()
        # 本周
        self.report.click_eveweek_console()
        sql_four = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_four = Utility.query_one('../config/base.conf', sql_four)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_four[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_five(self):
        self.report.click_console()
        # 本月
        self.report.click_sale_evemonth_console()
        sql_five = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_five = Utility.query_one('../config/base.conf', sql_five)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_five[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_six(self):
        self.report.click_console()
        # 上周
        self.report.click_oldweek_console()
        sql_six = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_six = Utility.query_one('../config/base.conf', sql_six)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_six[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_seven(self):
        self.report.click_console()
        # 上月
        self.report.click_oldmonth_console()
        sql_seven = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_seven = Utility.query_one('../config/base.conf', sql_seven)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_seven[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_console_query_eight(self):
        self.report.click_console()
        # 本年
        self.report.click_eveyear_console()
        sql_eight = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_eight = Utility.query_one('../config/base.conf', sql_eight)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_eight[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    # 电销部
    @parameterized.expand(sale_data)
    def test_sale_data_one(self, starttime, endtime, expect):
        self.report.click_sale()
        # 搜索
        self.report.input_sale_date(starttime, endtime)
        self.report.click_sale_query()
        sql_one = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_one = Utility.query_one('../config/base.conf', sql_one)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_one[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

    def test_sale_data_two(self):
        self.report.click_sale()
        # 当期
        self.report.click_sale_evedate_console()
        sql_two = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_two = Utility.query_one('../config/base.conf', sql_two)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_two[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_sale_data_three(self):
        self.report.click_sale()
        # 今日
        self.report.click_sale_eveday_console()
        sql_three = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_three = Utility.query_one('../config/base.conf', sql_three)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_three[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_sale_data_four(self):
        self.report.click_sale()
        # 本周
        self.report.click_sale_veweek_console()
        sql_four = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_four = Utility.query_one('../config/base.conf', sql_four)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_four[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_sale_data_five(self):
        self.report.click_sale()
        # 本月
        self.report.click_sale_evemonth_console()
        sql_five = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_five = Utility.query_one('../config/base.conf', sql_five)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_five[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_sale_data_six(self):
        self.report.click_sale()
        # 上周
        self.report.click_sale_oldweek_console()
        sql_six = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_six = Utility.query_one('../config/base.conf', sql_six)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_six[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-fail')

    def test_sale_data_seven(self):
        self.report.click_sale()
        # 上月
        self.report.click_sale_oldmonth_console()
        sql_seven = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_seven = Utility.query_one('../config/base.conf', sql_seven)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_seven[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_sale_data_eight(self):
        self.report.click_sale()
        # 本年
        self.report.click_sale_eveyear_console()
        sql_eight = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_eight = Utility.query_one('../config/base.conf', sql_eight)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_eight[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    # 市场部
    @parameterized.expand(market_data)
    def test_market_data_one(self, starttime, endtime, expect):
        self.report.click_market()
        # 搜索
        self.report.input_market_date(starttime, endtime)
        self.report.click_market()
        sql_one = 'select count(department_id) from customer where create_time="2020-04-13"  '
        result_one = Utility.query_one('../config/base.conf', sql_one)
        if result_one[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

    def test_market_data_two(self):
        self.report.click_market()
        # 当期
        self.report.click_market_evedate_console()
        sql_two = 'select count(department_id) from customer where "2020-01-31"<=create_time<="2020-03-31'
        result_two = Utility.query_one('../config/base.conf', sql_two)
        if result_two[0] == 0:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_three(self):
        self.report.click_market()
        # 今日
        self.report.click_market_eveday_console()
        sql_three = 'select count(department_id) from customer where create_time="2020-04-13"'
        result_three = Utility.query_one('../config/base.conf', sql_three)
        if result_three[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_four(self):
        self.report.click_market()
        # 本周
        self.report.click_market_eveday_console()
        sql_four = 'select count(department_id) from customer where "2020-04-13"<=create_time<="2020-04-13"'
        result_four = Utility.query_one('../config/base.conf', sql_four)
        if result_four[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_five(self):
        self.report.click_market()
        # 本月
        self.report.click_market_evemonth_console()
        sql_five = 'select count(department_id) from customer where "2020-04-01"<=create_time<="2020-04-13"'
        result_five = Utility.query_one('../config/base.conf', sql_five)
        if result_five[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_six(self):
        self.report.click_market()
        # 上周
        self.report.click_market_oldweek_console()
        sql_six = 'select count(department_id) from customer where "2020-04-06"<=create_time<="2020-04-12"'
        result_six = Utility.query_one('../config/base.conf', sql_six)
        if result_six[0] == 0:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_seven(self):
        self.report.click_market()
        # 上月
        self.report.click_market_oldmonth_console()
        sql_seven = 'select count(department_id) from customer where "2020-03-01"<=create_time<="2020-03-31"'
        result_seven = Utility.query_one('../config/base.conf', sql_seven)
        if result_seven[0] == 0:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_market_data_eight(self):
        self.report.click_market()
        # 本年
        self.report.click_market_eveyear_console()
        sql_eight = 'select count(department_id) from customer where "2020-01-01"<=create_time<="2020-04-13"'
        result_eight = Utility.query_one('../config/base.conf', sql_eight)
        if result_eight[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    # 就业部
    @parameterized.expand(job_data)
    def test_job_data_one(self, starttime, endtime, expect):
        self.report.click_job()
        # 搜索
        self.report.input_job_date(starttime, endtime)
        self.report.click_job_cnsole_query()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '甘立文':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)

    def test_job_data_two(self):
        self.report.click_job()
        # 今日
        self.report.click_job_eveday_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '甘立文':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_job_data_three(self):
        self.report.click_job()
        # 本周
        self.report.click_eveweek_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '无符合条件的记录':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_job_data_four(self):
        self.report.click_job()
        # 本月
        self.report.click_job_evemonth_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '甘立文':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_job_data_five(self):
        self.report.click_job()
        # 上周
        self.report.click_job_oldweek_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '无符合条件的记录':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_job_data_six(self):
        self.report.click_job()
        # 上月
        self.report.click_job_oldmonth_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '无符合条件的记录':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')

    def test_job_data_seven(self):
        self.report.click_job()
        # 本年
        self.report.click_job_eveyear_console()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '甘立文':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'query-pass')


if __name__ == '__main__':
    unittest.main(verbosity=2)
