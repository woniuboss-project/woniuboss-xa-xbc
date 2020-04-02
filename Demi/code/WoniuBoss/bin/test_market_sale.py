from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.market_sale import MarketPort
import unittest
from parameterized import parameterized

# 获取测试数据
market_sale_datas = Utility.get_json('..\\config\\testdata.conf')
# 新增资源
market_add_datas = Utility.get_excel_to_tuple(market_sale_datas[4])
# 上传简历
market_upload_datas = Utility.get_excel_to_tuple(market_sale_datas[5])
# 查询资源
market_query_datas = Utility.get_excel_to_tuple(market_sale_datas[6])


class TestMarketSale(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test over")

    # 新增资源
    @parameterized.expand(market_add_datas)
    def test_market_add(self, market_add_url, market_add_data, expect):
        market_add_resp = MarketPort().market_add(market_add_url, market_add_data)
        # 断言
        if market_add_resp == expect:
            print("market add test success")
        else:
            print("market add test fail")

    # 上传简历
    @parameterized.expand(market_upload_datas)
    def test_market_add(self, market_upload_url, market_upload_data, expect):
        market_upload_resp = MarketPort().market_add(market_upload_url, market_upload_data)
        # 断言
        if market_upload_resp == expect:
            print("market upload test success")
        else:
            print("market upload test fail")

    # 查询资源
    @parameterized.expand(market_query_datas)
    def test_market_add(self, market_query_url, market_query_data, expect):
        market_query_resp = MarketPort().market_add(market_query_url, market_query_data)
        # 断言
        if market_query_resp == expect:
            print("market query test success")
        else:
            print("market query test fail")


if __name__ == '__main__':
    unittest.main(verbosity=2)
