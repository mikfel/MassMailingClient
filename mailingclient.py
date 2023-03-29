import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

x=int(input("What's your mailing server? \n1. Gmail\n2. Outlook\n3. Yahoo\n4. Protonmail\n"))

if x==1:
    print("Due to gmail security, you need to enable less secure apps which is only available for Google Workspace and Cloud identity accounts. If you don't have one, you can't use this program.")
    server=smtplib.SMTP('smtp.gmail.com',587)
elif x==2:
    server=smtplib.SMTP('smtp-mail.outlook.com',587)
elif x==3:
    server=smtplib.SMTP('smtp.mail.yahoo.com',587)
elif x==4:
    server=smtplib.SMTP('smtp.protonmail.com',1025)


server.starttls()
server.ehlo()

with open("password.txt",'r') as f:
    password = f.read()
sender='youremail@example.com' #CHANGE IT TO YOUR EMAIL
server.login(sender,password) 



msg = MIMEMultipart()
msg['from'] = 'John'   #CHANGE IT TO YOUR NAME
msg['Subject'] = 'Test' #Change IT TO YOUR SUBJECT

with open('message.txt','r') as f: #file that contains the message you want to send
    message= f.read()

with open('receivers.txt','r') as f1: #receivers.txt is a file that contains the list of receivers separated by commas
    list_of_receivers=f1.read()
list_of_receivers=list_of_receivers.split(',')


msg.attach(MIMEText(message, 'plain'))

filename = 'image.png' #name of the file you want to send
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
for i in list_of_receivers:
    server.sendmail(sender,i,text)

print("Emails sent successfully!")