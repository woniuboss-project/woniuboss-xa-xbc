from woniuboss2.tools.service import Service

class Backstage:
    def __init__(self):
        self.session = Service.get_session()

    #角色管理-新增角色
    def add_role(self,add_role_url,add_role_data):
        return self.session.post(add_role_url,add_role_data)

    #用户管理-查询用户
    def query_user(self,query_user_url,query_user_data):
        return self.session.post(query_user_url,query_user_data)


