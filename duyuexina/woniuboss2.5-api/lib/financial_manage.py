from woniuboss2.tools.service import Service


class Finance:
    def __init__(self):
        self.session = Service.get_session()

    def add_flow(self,add_flow_url,add_flow_data):
        return self.session.post(add_flow_url, add_flow_data)

    def query_flow(self,query_flow_url,query_flow_data):
        return self.session.post(query_flow_url,query_flow_data)

    def edit_flow(self,edit_flow_url,edit_flow_data):
        return self.session.post(edit_flow_url,edit_flow_data)

