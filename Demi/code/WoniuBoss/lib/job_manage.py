# 就业管理接口测试
from WoniuBoss.tools.service import Service


class JobManage:

    def __init__(self):
        self.session = Service.get_session(8)

    # 就业管理通过
    def creat_pass(self, creat_pass_url):
        return self.session.get(creat_pass_url).text

    # 面试提交功能
    def creat_commit(self, job_commit_url):
        return self.session.get(job_commit_url).text

    # 就业信息查询
    def creat_query(self, creat_query_url, creat_query_data):
        return self.session.post(creat_query_url, creat_query_data).text

    # 真实面试
    def creat_interview(self, creat_interview_url, creat_interview_data):
        return self.session.post(creat_interview_url, creat_interview_data).text

    # 入职情况
    def creat_status(self, creat_status_url, creat_status_data):
        return self.session.post(creat_status_url, creat_status_data).text
