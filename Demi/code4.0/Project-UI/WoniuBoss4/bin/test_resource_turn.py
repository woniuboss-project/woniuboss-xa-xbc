from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from WoniuBoss4.lib.resource_turn import ResourceTurn
from WoniuBoss4.tools.utility import Utility
from WoniuBoss4.tools.service import Service
import unittest
import time


class TestResourceTurn(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver('../config/base.conf')
        Service.miss_login(self.driver, '../config/base.conf')
        self.driver.find_element_by_link_text(u'资源管理').click()
        self.turn = ResourceTurn(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    def test_query_one(self):
        self.turn.resource_turn_query_one()
        sql = 'select count(*) from customer'
        result = Utility.query_one('../config/base.conf', sql)
        if len(self.driver.find_element_by_id('transmit-table')) == result[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'turn-pass')

    def test_query_two(self):
        self.turn.resource_turn_query_two()
        sql = 'select count(*) from customer where name="huhu"'
        result = Utility.query_one('../config/base.conf', sql)
        if self.driver.find_element_by_xpath('//table[@id="transmit-table"]/tbody/tr[1]/td[2]').text == 'huhu' \
                and result[0] == 1:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, 'turn-pass')

    def test_turn(self):
        self.turn.resource_turn_commit()
        if self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div').text == '转交资源完成.':
            actual = 'turn-pass'
        else:
            actual = 'turn-fail'
        self.assertEqual(actual, 'turn-pass')
