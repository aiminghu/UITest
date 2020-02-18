#coding=utf-8

import os
import configparser

#获取该文件的真实路径,然后分割路径和文件名存入一个元祖
proDir = os.path.split(os.path.realpath(__file__))[0]
#获取上层目录
parDir = os.path.dirname(proDir)

configPath = os.path.join(parDir,"config.ini")
# print("prodir:",proDir,configPath)


class ReadConfig(object):
    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding="utf-8")

    #获取配置文件中的分组（eg:EMAIL）中的对应选项(eg:name)的值
    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_screen(self,name):
        value = self.cf.get("SCREEN", name)
        return value

    # 获取app信息
    def get_app(self, name):
        return self.cf.get('APP', name)

    # 获取操作平台信息
    def get_platform(self, name):
        return self.cf.get('PLATFORM', name)

if __name__ == '__main__':
    a = ReadConfig()
    host_name = a.get_email('mail_host')
    print(host_name)

    print(a.get_app('appPackage'))
    print(a.get_platform('platformVersion'))

