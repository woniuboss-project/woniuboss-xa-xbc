# 市场营销接口测试
from WoniuBoss.tools.service import Service


class MarketPort:

    def __init__(self):
        self.session = Service.get_session(10)

    # 新增资源
    def market_add(self, market_add_url, market_add_data):
        return self.session.post(market_add_url, market_add_data).text

    # 上传专属
    def market_upload(self, market_upload_url, market_upload_data):
        return self.session.post(market_upload_url, market_upload_data).text

    # 查询资源
    def market_qurey(self, market_query_url, market_query_data):
        return self.session.post(market_query_url, market_query_data).text
