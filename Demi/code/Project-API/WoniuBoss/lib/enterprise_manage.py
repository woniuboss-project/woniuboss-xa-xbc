# 企业管理接口测试
from WoniuBoss.tools.service import Service


class EnterpriseManage:

    def __init__(self):
        self.session = Service.get_session(0)

    # 新增企业客户
    def enterprise_add(self, enterprise_add_url):
        return self.session.get(enterprise_add_url).text

    # 修改企业客户信息
    def enterprise_update(self, enterprise_update_url):
        return self.session.get(enterprise_update_url).text

    # 查询企业客户
    def enterprise_query(self, enterprise_query_url):
        return self.session.get(enterprise_query_url).text

    
