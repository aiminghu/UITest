#coding:utf-8

"""
继承MyTest基础类
编写测试用例
每一个test用例使用test开头
"""
import unittest
import time
from common.MyTest  import MyTest
from common.Public import Public
from po.HomePage import HomePage
from common.ReadData import readdata
import sys


# 定义测试类
class HomeTest(MyTest):

    # 搜索
    def test_search(self):
        a = HomePage(self.driver)
        fun_name = sys._getframe().f_code.co_name
        d = readdata()
        search_data = d.get_data(fun_name)
        print('搜索')
        a.search(search_data)
        # a.clickSearch()
        # time.sleep(2)
        # self.driver.find_element_by_id('com.ss.android.article.news:id/w3').send_keys(search_data)
        # time.sleep(4)
        # self.driver.find_element_by_id('com.ss.android.article.news:id/w2').click()
        # time.sleep(10)

    # 点击个人中心
    def test_personalcenter(self):
        #self.driver.find_element_by_id('com.ss.android.article.news:id/dfi').click()
        a = HomePage(self.driver)
        a.personal_center()

    # 切换标签至“视频”
    def switch_tap(self):
        # self.driver.find_element_by_xpath('//android.view.View[@content-desc="视频"]').click()
        a = HomePage(self.driver)
        a.vedio_tap()


if __name__ == '__main__':
    unittest.main()
