#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import  unittest
import HTMLTestRunner
import  os ,time,datetime
import  smtplib
from email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
from  email.mime.image import MIMEImage
#定义发送邮件
def sentmail(file_new):
    #发送信箱
    main_from='466328820@qq.com'
    #收信箱
    main_to = '1536772729@qq.com'
    #定义正文
    f = open(file_new,'rb')
    main_body = f.read()
    f.close()
    msg=MIMEText(main_body, _subtype='html', _charset='utf-8')
    msg['Subject']=u"百度测试报告"
    msg['date']=time.strftime('%a, %d %b %y %H:%M:%S %z')
    try:
        smtp =smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.login('466328820@qq.com', 'pclnwknonockbjah')
        smtp.sendmail(main_from, main_to, msg.as_string())
        print("发送成功")
    except Exception:
        print("发送失败")
    finally:
        smtp.quit()
    #print('eamli has send out!')

#查找测试报告
def sendreport():
    result_dir = 'D:\\pythonwork\\test_report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print(u'最新的测试报告: ' +lists[-1])
    file_new =os.path.join(result_dir, lists[-1])
    print(file_new)
    sentmail(file_new)

if __name__ == '__main__':
    sendreport()
