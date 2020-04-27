from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.job_manage_tech import JobManageTech
import unittest
from parameterized import parameterized

# 获取测试数据
job_manage_tech_datas = Utility.get_json('..\\config\\testdata.conf')
# 技术面试通过
job_manage_tech_pass_datas = Utility.get_excel_to_tuple_url(job_manage_tech_datas[10])
# 技术面试不通过
job_manage_tech_unpass_datas = Utility.get_excel_to_tuple_url(job_manage_tech_datas[11])
# 查询资源
job_manage_tech_query_datas = Utility.get_excel_to_tuple(job_manage_tech_datas[12])


class TestJobManageTech(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 技术面试通过
    @parameterized.expand(job_manage_tech_pass_datas)
    def test_job_manage_tech_pass(self, job_manage_tech_pass_url, expect):
        job_manage_tech_pass_resp = JobManageTech().job_pass(job_manage_tech_pass_url)
        actual = job_manage_tech_pass_resp
        # 断言
        self.assertEqual(actual, expect)

    # 技术面试不通过
    @parameterized.expand(job_manage_tech_unpass_datas)
    def test_job_manage_tech_unpass(self, job_manage_tech_unpass_url, expect):
        job_manage_tech_unpass_resp = JobManageTech().job_pass(job_manage_tech_unpass_url)
        actual = job_manage_tech_unpass_resp
        # 断言
        self.assertEqual(actual, expect)

    # 查询资源
    @parameterized.expand(job_manage_tech_query_datas)
    def test_job_manage_tech_query(self, job_manage_tech_query_url, job_manage_tech_query_data, expect):
        job_manage_tech_query_resp = JobManageTech().job_query(job_manage_tech_query_url,
                                                               job_manage_tech_query_data)
        actual = job_manage_tech_query_resp
        # 断言
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
