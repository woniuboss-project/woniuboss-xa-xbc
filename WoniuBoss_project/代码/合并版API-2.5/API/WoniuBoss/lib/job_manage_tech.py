# 就业管理技术面试接口测试
from WoniuBoss.tools.service import Service


class JobManageTech:

    def __init__(self):
        self.session = Service.get_session(6)

    # 技术面试通过
    def job_pass(self, job_pass_url):
        return self.session.get(job_pass_url).text

    # 技术面试不通过
    def job_unpass(self, job_unpass_url):
        return self.session.get(job_unpass_url).text

    # 技术面试信息查询
    def job_query(self, job_query_url, job_query_data):
        return self.session.post(job_query_url, job_query_data).text
