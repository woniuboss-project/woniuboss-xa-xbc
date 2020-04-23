from woniuboss2.tools.service import Service


class Hr:
    def __init__(self):
        self.session = Service.get_session()

    def add_staff(self,add_staff_url,add_staff_data):
        return self.session.post(add_staff_url,add_staff_data)

    def query_staff(self,query_staff_url,query_staff_data):
        return self.session.post(query_staff_url,query_staff_data)
        # query_staff_result = []
        # page_index = 1
        # while 1:
        #     result = self.session.post(query_staff_url, {'pageSize':query_staff_data['pageSize'],'pageIndex':str(page_index),'regionId':query_staff_data['regionId'],'deptId':query_staff_data['deptId'],
        #                                                  'empName':query_staff_data['empName'],'status':query_staff_data['status']})
        #     result_json = result.json()
        #     if len(result_json) == 0:
        #         break
        #     else:
        #         for r in result_json:
        #             query_staff_result.append(r)
        #         page_index += 1
        # return query_staff_result

    def edit_staff(self,edit_staff_url,edit_staff_data):
        return self.session.post(edit_staff_url,edit_staff_data)

