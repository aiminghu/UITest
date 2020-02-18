#coding:utf-8
from appium import webdriver
from common.Mytest import MyTest
import os
import time


# 操作滑屏
class Public(MyTest):
    def getSize(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        print(x, y)
        return (x, y)

    # 向上滑动
    def swipeUp(self, driver, t=1000):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        y2 = int(l[1] * 0.25)
        driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, driver, t=1000):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        y2 = int(l[1] * 0.75)
        driver.swipe(x1, y1, x1, y2, t)

    def swipeLeft(self, driver, t=1000):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        x2 = int(l[1] * 0.25)
        driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, driver, t=1000):
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.5)
        x2 = int(l[1] * 0.75)
        driver.swipe(x1, y1, x2, y1, t)

    # 操作截图  get_screenshot_as_file
    def screen_shot(self, driver):
        image_path = os.path.dirname(os.path.split(os.path.abspath(__file__))[0]) + '\\' + 'image'
        current_time = time.strftime('%Y%m%d%H%M%S')
        image_name = image_path + '\\' + current_time + '.png'
        print(image_name)
        # 截图并保存
        driver.get_screenshot_as_file(image_name)
