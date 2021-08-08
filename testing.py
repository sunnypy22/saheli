from Saheli.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from Saheli import settings

print("byeee")
subject = 'welcome to GFG world'
message = 'Hi Komal, How is your Sunday ?'
email_from = "sunnypatel834798@gmail.com"
user = "sehgalc655@gmail.com"
recipient_list = "sehgalc655@gmail.com"

send_mail(subject, message, "sunnypatel834798@gmail.com", [recipient_list], fail_silently = False)

# Construct an email message that uses the connection
