from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.report_center import ReportCenter
import unittest
from parameterized import parameterized

# 获取测试数据
report_center_datas = Utility.get_json('..\\config\\testdata.conf')
# 咨询部数据
console_datas = Utility.get_excel_to_tuple(report_center_datas[0])
# 电销部数据
sale_datas = Utility.get_excel_to_tuple(report_center_datas[1])
# 市场部数据
mark_datas = Utility.get_excel_to_tuple(report_center_datas[2])
# 就业部数据
job_datas = Utility.get_excel_to_tuple(report_center_datas[3])


class TestReportCenter(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 咨询部报表中心功能测试
    @parameterized.expand(console_datas)
    def test_console_report(self, console_url, console_data, console_expect):
        console_report_resp = ReportCenter().console_report(console_url, console_data)
        # 断言
        if console_report_resp == console_expect:
            print("console report test successful")
        else:
            print("console report test fail")

    # 电销部报表中心功能测试
    @parameterized.expand(sale_datas)
    def test_sale_report(self, sale_url, sale_data, sale_expect):
        sale_report_resp = ReportCenter().console_report(sale_url, sale_data)
        # 断言
        if sale_report_resp == sale_expect:
            print("sale report test successful")
        else:
            print("sale report test fail")

    # 市场部报表中心功能测试
    @parameterized.expand(mark_datas)
    def test_sale_report(self, mark_url, mark_data, mark_expect):
        mark_report_resp = ReportCenter().console_report(mark_url, mark_data)
        # 断言
        if mark_report_resp == mark_expect:
            print("mark report test successful")
        else:
            print("mark report test fail")

    # 市场部报表中心功能测试
    @parameterized.expand(job_datas)
    def test_sale_report(self, job_url, job_data, job_expect):
        job_report_resp = ReportCenter().console_report(job_url, job_data)
        # 断言
        if job_report_resp == job_expect:
            print("job report test successful")
        else:
            print("job report test fail")


if __name__ == '__main__':
    unittest.main(verbosity=2)
