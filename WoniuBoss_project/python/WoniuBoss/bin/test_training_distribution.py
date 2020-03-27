import unittest
from parameterized import parameterized
from WoniuBoss.tools.utility import Utility
from WoniuBoss.lib.training import Tran
train_data=Utility.get_json('..\\config\\testAPI.conf')
distribution_query_info=Utility.get_excel_to_tuple(train_data[9])
Proportionate_distribution_info=Utility.get_excel_to_tuple(train_data[10])
class Training(unittest.TestCase):
    def setUp(self):
        self.train = Tran(3)

    @parameterized.expand(distribution_query_info)
    def test_distribution_query(self, URL, DATA, CONTENT):
        distribution_query_url=URL
        distribution_query_data=DATA
        resp=self.train.distribution_query(distribution_query_url,distribution_query_data)

    @parameterized.expand(Proportionate_distribution_info)
    def test_Proportionate_distribution(self, URL, DATA, CONTENT):
        Proportionate_distribution_url=URL
        Proportionate_distribution_data=DATA
        resp=self.train.Proportionate_distribution(Proportionate_distribution_url,Proportionate_distribution_data)

if __name__ == '__main__':
    unittest.main(verbosity=2)