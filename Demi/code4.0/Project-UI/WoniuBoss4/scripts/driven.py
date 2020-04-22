import unittest
from WoniuBoss4.tools.utility import Utility
from HTMLTestRunner import HTMLTestRunner


class Driven:
    def start(self):
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()
        testcase_names = Utility.trans_str('..\\config\\test.conf')
        # print(testcase_names)
        tests = loader.loadTestsFromNames(testcase_names)
        ts.addTests(tests)
        # 测试报告文件名称的格式为：xxxx-xx-xx_xx_xx_xx_report.html
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\logs\\%s_report.html' % (ctime), 'w')as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(ts)


if __name__ == '__main__':
    Driven().start()
