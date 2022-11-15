#发邮件
import smtplib
#用于构建内容文本
from email.mime.text import MIMEText
# 从email包引入Header()方法，Header()是用来构建邮件头的
from email.header import Header

#发送邮箱
sender = '2118430400@qq.com'
#邮箱端口号
port=465
#接收邮箱
receiver = '523469321@qq.com'
#发送邮件主题
subject = '测试执行结果'
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/授权码
username = '2118430400@qq.com'
password ='kwrxtxruogjwhabh'
#邮件信息对象（编写text类型的邮件正文）
msg = MIMEText('<html><h1>本次UI自动化通过率100%</h1></html>','html','utf-8')
#Subject来自哪里，指发件人的名称或地址
msg['Subject'] = Header(subject, 'utf-8')
# 开启发信服务
smtp = smtplib.SMTP_SSL(smtpserver,port)
# 发件人邮箱账号、邮箱授权码
smtp.login(username, password)
# msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str
smtp.sendmail(sender, receiver,msg.as_string())
#发件人邮箱中的SMTP服务器
smtp.connect('smtp.qq.com')
# 关闭服务器
smtp.quit()