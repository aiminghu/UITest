#coding:utf-8
"""
1.继承unittest父类，方便testcase使用
2.初始化和清理方法



"""
import unittest
from common.Driver import Driver
import time


class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('执行初始化类方法')
        cls.d = Driver()
        cls.driver = cls.d.startUp()
        print('连接driver')

    def setUp(self):
        print('执行初始化方法')
        time.sleep(3)
        self.driver.launch_app()        # 启动app但不是重新启动
        time.sleep(6)

    def tearDown(self):
        print('执行清理方法')
        self.driver.close_app()         # 关闭app但不杀掉进程

    @classmethod
    def tearDownClass(cls):
        print('执行清理类方法')
        cls.driver.quit()
        print('关闭driver')


if __name__ == '__main__':
    unittest.main()
