from time import sleep

from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 1.扫描所有用例
tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\calc", pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="加法运算",
    verbosity=1,
    stream=open(file="计算器.html", mode="w+", encoding="utf-8")
)

# 3.运行
runner.run(tests)
sleep(10)
import zmail

# 你的邮件内容

mail_content = {
        'subject': 'Success!',  # 随便填写
        'content_text': '报错！！！',  # 随便填写
        'attachments': ['D:\\pythonProject\\calc\\计算器.html'],
    }

# 使用你的邮件账户名和密码登录服务器
server = zmail.server('3121114552@qq.com', 'rgjtefctpecrddgb')
# 发送邮件
server.send_mail('2431320433@qq.com', mail_content)
