import random
import smtplib

from details import email, password

otp = ''.join([str(random.randint(1, 9)) for i in range(6)])
toaddress = input("enter your email address:")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

subject = "Don't share your OTP with anyone"
txt = f'Subject:{subject}\n\n your OTP is '+otp
server.sendmail(email, toaddress, txt)
server.quit()
print("mail send!")

check = int(input("enter otp received: "))

if check == int(otp):
    print("OTP verified successfully!")
else:
    print("Wrong OTP entered! Resend OTP and try again.")