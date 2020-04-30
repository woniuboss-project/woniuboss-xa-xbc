# 报表中心接口测试
from WoniuBoss.tools.service import Service


class ReportCenter:

    def __init__(self):
        self.session = Service.get_session(0)

    # 咨询部
    def console_report(self, console_report_url, console_report_data):
        return self.session.post(console_report_url, console_report_data).text

    # 电销部
    def sale_report(self, sale_report_url, sale_report_data):
        return self.session.post(sale_report_url, sale_report_data)

    # 市场部
    def mark_report(self, mark_report_url, mark_report_data):
        return self.session.post(mark_report_url, mark_report_data)

    # 就业部
    def job_report(self, job_report_url, job_report_data):
        return self.session.post(job_report_url, job_report_data)
