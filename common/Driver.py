#coding:utf-8
'''
启动app，作为父类，便于po或testcase继承

'''


from appium import webdriver
import time,os

class Driver(object):


    def startUp(self):
        print('启动app')
        #设备及安装包信息
        desired_caps = {
          "deviceName": "127.0.0.1:21503",
          "platformName": "Android",
          "platformVersion": "5.1.1",
          "appPackage": "com.ss.android.article.news",
          "appActivity": "com.ss.android.article.news.activity.MainActivity",
          "noReset": True,
          "unicodeKeyboard": True

        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        print('已经启动，等待6s中。。。')
        return driver





# if __name__ == '__main__':
#     d = Driver()
#     driver = d.startup()
#     time.sleep(10)
#     print('已经启动，等待...')
#     # 发微头条
#     driver.find_element_by_id('com.ss.android.article.news:id/bpx').click()
#     time.sleep(2)
#     # driver.find_element_by_android_uiautomator("new UiSelector().text(\"发微头条\")").click()
#     # time.sleep(2)
#     # driver.find_element_by_id('com.ss.android.article.news:id/bmj').send_keys("这是我的第二个微头条")
#     # time.sleep(2)
#     # driver.find_element_by_id('com.ss.android.article.news:id/a96').click()
