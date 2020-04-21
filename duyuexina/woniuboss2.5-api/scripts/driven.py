import unittest
from woniuboss2.tools.utility import Utility
class Driven:
    def start(self):
        from HTMLTestRunner import HTMLTestRunner
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()
        testcase_names = Utility.trans_str('..\\config\\test.conf')

        tests = loader.loadTestsFromNames(testcase_names)
        ts.addTests(tests)
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\report\\%s_report.html' % (ctime), 'w',encoding='UTF-8') as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(ts)


if __name__ == '__main__':
    Driven().start()