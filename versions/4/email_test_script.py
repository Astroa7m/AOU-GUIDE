import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("fake.dr.abrar@gmail.com", "iloe gfvm jskg pgdb")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("fake.dr.abrar@gmail.com", "200304om@aou.edu.om", message)
# terminating the session
s.quit()