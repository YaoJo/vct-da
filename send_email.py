# 1 导入模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from email.utils import formataddr #发件人信息


# 发件人邮箱配置
sender_email = '1907077582@qq.com'
sender_password = ''
receiver_email = 'yaojo_0119@163.com'

# 创建邮件对象
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "战队A胜负数据可视化图表"

# 添加邮件正文
body = "附件为战队A对阵各对手的胜负场次分析图，请查收。"
msg.attach(MIMEText(body, "plain"))

# 添加图片附件
with open('EDG_vs_opponents.png', "rb") as f:
    img_data = f.read()
    img = MIMEImage(img_data, name="战队A胜负对比.png")
    msg.attach(img)

# 发送
try:
    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('发送成功')
except Exception as e:
    print(f"Error: {e}")