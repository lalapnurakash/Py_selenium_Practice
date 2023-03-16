import smtplib
import ssl
from email import encoders
from email.message import  EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

email_sendr="akashpatel0426@gmail.com"
email_pwd="sfctoatezfnpusko"

email_rvr="lalapnurakash@gmail.com"

subj="this from python"
body="""ntg"""
#em=MIMEMultipart()
em=EmailMessage()
em['From']=email_sendr
em['To']=email_rvr
em['subject']=subj
em.set_content(body)

attachment=open("sample.log",'w')
attachment.write(body)
encoders.encode_base64(attchment_package)
em.attach(attachment)
context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
 smtp.login(email_sendr,email_pwd)
 smtp.sendmail(email_sendr,email_rvr,em.as_string())

