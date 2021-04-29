'''
기능: 
이메일 전송 
21.04.03일 작동 확인!

테스트 환경
- 구글 계정으로 이메일 전송(오류 발생시 주석 내용 참고)

'''

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# support.google 오류가 발생한다면 해당 링크로 들어가서 '보안 수준이 낮은 앱의 액세스' - '보안 수준이 낮은 앱 허용'을 해야 한다
# password 입력은 sender 계정의 pw 입력하면 된다.

sender_email = "xxxxx@xxx.com" # 보내는 사람의 이메일 주소
receiver_email = "xxxxx@gmail.com" # 받는 사람의 이메일 주소
password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# 이메일 내용
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a>
       has many great tutorials.
    </p>
  </body>
</html>
"""
#html 변수가 메일 내용이 된다

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
        )