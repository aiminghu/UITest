#coding:utf-8

'''
功能：
    1.配置发送邮件属性
    2.读取邮件配置
    3.发送邮件
'''



import smtplib,os,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig import ReadConfig


class ConfigEmail():


    #读取ini文件配置属性
    r = ReadConfig()
    mail_host = r.get_email('mail_host')
    # 配置第三方 SMTP 服务
    # mail_host = "smtp.163.com"  #设置服务器
    mail_user = r.get_email('mail_user')  #用户名
    mail_pass = r.get_email('mail_pass')  #密码

    #配置邮件属性
    sender = r.get_email('sender') #发送方
    receivers = r.get_email('receiver')  # 接收方
    content = r.get_email('content') #内容
    msg = MIMEMultipart()

    # 获取创建时间最新的文件
    def get_last(self):
        report_dir = 'report'   # 报告所在文件夹名
        file_dir = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])     # 获取当前路径上层目录
        report_path = file_dir + '\\' + report_dir      # 报告所在目录
        report = os.listdir(report_path)            # 获取报告目录下的所有文件
        report_create_time = []         # 存放报告文件的创建时间
        report_dict = {}                # 存放文件及文件的创建时间
        for i in report:
            c_time = time.ctime(os.path.getctime(report_path + '\\' + i))
            report_create_time.append(c_time)
            report_dict[c_time] = i
        max_time = max(report_create_time)     # 获取最大的时间
        last_file = report_dict[max_time]       # 获取最新的文件
        return report_path + '\\' + last_file

    def config_file(self):
        #配置附件属性
        file = self.get_last()
        print(file)
        sendfile=open(file,'rb').read()
        att = MIMEText(sendfile, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.sender
        self.msg['Subject'] = 'Python SMTP 附件邮件测试'
        self.msg.attach(MIMEText('UI自动化报告邮件，如果想查看详情请查收附件', 'plain', 'utf-8'))


    #发送邮件
    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            # print(self.mail_host,self.mail_user,self.mail_pass,self.sender,self.receivers,self.message.as_string)
            s.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
            # s.set_debuglevel(1)
            # print(self.mail_user)
            # print(self.mail_pass)
            s.login(self.mail_user,self.mail_pass)

            s.sendmail(self.sender, self.receivers,self.msg.as_string())
            print("邮件发送成功")

        except smtplib.SMTPException as msg:
            print(msg)
            print("Error: 无法发送邮件")

if __name__ == '__main__':
# #     pass
    c = ConfigEmail()
    print(c)
    c.send_mail()
