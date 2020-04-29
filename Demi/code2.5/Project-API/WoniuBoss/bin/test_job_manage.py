from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.job_manage import JobManage
import unittest
from parameterized import parameterized

# 获取测试数据
job_manage_datas = Utility.get_json('..\\config\\testdata_deng.conf')
# 就业面试通过
job_manage_pass_datas = Utility.get_excel_to_tuple_url(job_manage_datas[13])
# 就业管理提交
job_manage_commit_datas = Utility.get_excel_to_tuple_url(job_manage_datas[14])
# 查询资源
job_manage_query_datas = Utility.get_excel_to_tuple(job_manage_datas[15])
# 真实面试
job_manage_interview_datas = Utility.get_excel_to_tuple(job_manage_datas[16])
# 入职情况
job_manage_status_datas = Utility.get_excel_to_tuple(job_manage_datas[17])


class TestJobManage(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 就业面试通过
    @parameterized.expand(job_manage_pass_datas)
    def test_job_manage_pass(self, job_manage_pass_url, expect):
        job_manage_pass_resp = JobManage().creat_pass(job_manage_pass_url)
        actual = job_manage_pass_resp
        # 断言
        self.assertEqual(actual, expect)

    # 就业管理提交
    @parameterized.expand(job_manage_commit_datas)
    def test_job_manage_commit(self, job_manage_commit_url, expect):
        job_manage_commit_resp = JobManage().creat_commit(job_manage_commit_url)
        actual = job_manage_commit_resp
        # 断言
        self.assertEqual(actual, expect)

    # 查询资源
    @parameterized.expand(job_manage_query_datas)
    def test_job_manage_tech_query(self, job_manage_query_url, job_manage_query_data, expect):
        job_manage_query_resp = JobManage().creat_query(job_manage_query_url,
                                                        job_manage_query_data)
        actual = job_manage_query_resp
        # 断言
        self.assertEqual(actual, expect)

    # 真实面试
    @parameterized.expand(job_manage_interview_datas)
    def test_job_manage_tech_query(self, job_manage_interview_url, job_manage_interview_data, expect):
        job_manage_interview_resp = JobManage().creat_interview(job_manage_interview_url,
                                                                job_manage_interview_data)
        actual = job_manage_interview_resp
        # 断言
        self.assertEqual(actual, expect)

    # 真实面试
    @parameterized.expand(job_manage_status_datas)
    def test_job_manage_tech_query(self, job_manage_status_url, job_manage_status_data, expect):
        job_manage_status_resp = JobManage().creat_interview(job_manage_status_url,
                                                             job_manage_status_data)
        actual = job_manage_status_resp
        # 断言
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
