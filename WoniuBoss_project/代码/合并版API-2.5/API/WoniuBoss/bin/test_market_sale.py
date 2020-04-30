from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.market_sale import MarketPort
import unittest
from parameterized import parameterized

# 获取测试数据
market_sale_datas = Utility.get_json('..\\config\\testdata_deng.conf')
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
        actual = market_add_resp
        # 断言
        self.assertEqual(actual, expect)

    # 上传简历
    @parameterized.expand(market_upload_datas)
    def test_market_add(self, market_upload_url, market_upload_data, expect):
        market_upload_resp = MarketPort().market_add(market_upload_url, market_upload_data)
        actual = market_upload_resp
        # 断言
        self.assertEqual(actual, expect)

    # 查询资源
    @parameterized.expand(market_query_datas)
    def test_market_add(self, market_query_url, market_query_data, expect):
        market_query_resp = MarketPort().market_add(market_query_url, market_query_data)
        actual = market_query_resp
        # 断言
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
