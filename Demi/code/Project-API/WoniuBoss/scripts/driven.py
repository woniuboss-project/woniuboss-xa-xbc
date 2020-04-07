import unittest


class Driven:
    def start(self):
        from HTMLTestRunner import HTMLTestRunner
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()
        from WoniuBoss.tools.utility import Utility
        testcase_names = Utility.trans_str('..\\config\\test.conf')
        tests = loader.loadTestsFromNames(testcase_names)
        ts.addTests(tests)
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        with open('..\\logs\\%s_report.html' % (ctime), 'w')as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(ts)


if __name__ == '__main__':
    Driven().start()
