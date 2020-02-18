#coding:utf-8
# 导包
import unittest
import time
import os
import HTMLTestRunner
from common.configEmail import ConfigEmail

# 用例目录
case_dir='testCase'
case_path = os.path.split(os.path.abspath(__file__))[0] + '\\' + case_dir
report_dir = os.path.split(os.path.abspath(__file__))[0] + '\\' + 'report'


# 查找所有测试用例
def run_case(case_dir=case_path):
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='*test*.py', top_level_dir=None)
    return discover


# 删除文件
def cls_report(report_dir=report_dir):
    a = os.listdir(report_dir)
    print(a)
    for i in a:
        # print(i)
        i = report_dir + '\\' + i
        try:
            os.remove(i)
            print('文件删除完成')
        except Exception as msg:
            print('文件删除失败：' + str(msg))


if __name__ == '__main__':
    # 结合单元测试框架生成测试报告
    cls_report(report_dir)
    time_stamp = time.strftime('%Y%m%d%H%M%S')
    report_path = os.path.split(os.path.abspath(__file__))[0] + '\\' + 'report' + '\\' + time_stamp + '.html'

    # print(report_path)
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    runner.run(run_case())
    # 发送邮件
    send_email = ConfigEmail()
    send_email.send_mail()
    fp.close()


