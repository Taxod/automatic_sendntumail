import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
import random
import time
'''
Win 10
Python 

Use NTU Mail to automicly send mail
Between random peroid send mail to somesone

1. Login
2. List the receiver
3. Write content 
4. Send mail (set SMTP_SSL)
5. Set random time and send times
6. close
'''


user = '_______________@ntu.edu.tw'
password = '___________'
receiver = ['____________@gmail.com','__________@ntu.edu.tw']

def send_mail_from_NTU(user,password,receiver,content):
    try:
        msg = MIMEText(content,'html','utf-8')
        msg['Subject'] = Header('_________')
        msg['From'] = Header(user)
        msg['To']= ";".join(receiver)
        server = smtplib.SMTP_SSL('smtps.ntu.edu.tw',465)
        server.ehlo()
        server.login('___________', password)
        server.sendmail(user,receiver,msg.as_string())
        server.quit()
        print('sent!')
    except:
        print("error!")

count = 0
while(True):
    count+= 1
    print(count)
    print(datetime.datetime.now())
    content = "_________________________"  # write in html
    send_mail_from_NTU(user, password, receiver, content)
    random_minute = random.randint(10, 20)
    print(random_minute)
    if count == 3:
        break
    time.sleep(random_minute*60) #second
print("end")

