import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# SEND EMAIL ATTACHMENT USING PYTHON
# THIS PROGRAM HELPS YOU READ EMAIL ADDRESS FROM A TEXT FILE's FIRST LINE
# AND THEN COMPOSE YOUR OWN EMAIL WITH AN ATTACHMENT THAT YOU CAN SEND
# TO THE ADDRESSEE


# Enter your filename
# The addressee's email has to be contained in the first line
line = open('sample.txt').readline()
   
fromaddr = "sample@example.com"

toaddr = line
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Subject"
  
# string to store the body of the mail 
body = "EMAIL BODY"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "send_file.txt"
attachment = open("File location on your laptop", "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# PORT NUMBER
PORT_NUMBER = 587
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', PORT_NUMBER) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "C") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
