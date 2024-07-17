import smtplib

my_email = 'rodzl12382@gmail.com'
password = 'Rlarodzl!23'

# connection = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs='kim.woongkeol@gmail.com', msg = 'Hello')
# connection.close()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(user=my_email,password=password)
    smtp_server.sendmail(from_addr=my_email, to_addrs='kim.woongkeol@gmail.com', msg = 'Hello')
