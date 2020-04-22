import requests

from woniuboss2.tools.utility import Utility


class Service:
    @classmethod
    def get_session(cls):
        base_info = Utility.get_json('..\\config\\base.conf')
        login_url = "%s://%s:%s/%s/" %(base_info['PROTOCOL'],base_info['HOSTNAME'],base_info['PORT'],base_info['AURL'])
        login_data = {"userName":base_info["USERNAME"],"userPass":base_info["PASSWORD"],"checkcode":base_info["VERIFYCODE"]}
        #print(login_data)
        session = requests.session()
        session.post(login_url,login_data)
        return session
if __name__ == '__main__':
    Service.get_session()