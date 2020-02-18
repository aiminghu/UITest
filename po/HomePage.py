#coding:utf-8

from selenium.webdriver.common.by import By
from common.ReadData import readdata
from appium import webdriver
from common.Driver import Driver
import time
import sys


class HomePage(Driver):
    def __init__(self, driver):
        self.driver = driver

    # 个人中心按钮
    personal_center = (By.ID, 'com.ss.android.article.news:id/dfi')
    # 视频标签
    vedio_tap = (By.XPATH, '//android.view.View[@content-desc="视频"]')
    # 搜索页面
    search_page = (By.ID, 'com.ss.android.article.news:id/bpb')
    # 搜索框
    search_box = (By.ID, 'com.ss.android.article.news:id/w3')
    # 搜索按钮
    search_button = (By.ID, 'com.ss.android.article.news:id/w2')

    # 点击个人中心
    def personalCenter(self):
        time.sleep(4)
        self.driver.find_element(*self.personal_center).click()

    # 视频标签
    def vedioTap(self):
        time.sleep(4)
        self.driver.find_element(*self.vedio_tap).click()

    # 点击搜索，进入搜索页面
    def clickSearch(self):
        time.sleep(3)
        self.driver.find_element(*self.search_page).click()
        time.sleep(10)
        return self.driver

    # 进入搜索页面，输入内容进行搜索
    def search(self, search_data):
        time.sleep(3)
        self.clickSearch()
        time.sleep(4)
        self.driver.find_element(*self.search_box).send_keys(search_data)
        time.sleep(6)
        self.driver.find_element(*self.search_button).click()
        time.sleep(8)

    # 发布按钮
    public_button = (By.ID, 'com.ss.android.article.news:id/bpx')
    # 发微头条按钮
    weitotiao_button = (By.LINK_TEXT, '发微头条')

    # 发微头条
    def post_weitoutiao(self):
        time.sleep(5)
        self.driver.find_element(*self.public_button).click()
        time.sleep(6)
        self.driver.find_element(*self.weitotiao_button).click()
        time.sleep(5)


if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    # fun_name = sys._getframe().f_code.co_name
    # fun_name = 'test_search'
    # print(fun_name)
    # d = readdata()
    # search_data = d.get_data(fun_name)
    # h = HomePage(driver)
    # h.search(search_data)
    h = HomePage(driver)
    h.post_weitoutiao()
