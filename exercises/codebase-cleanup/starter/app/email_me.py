




import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

# obtain api key at https://sendgrid.com/
# and verify single sender with a given email address...
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")

# configure the client

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>

#
# compile the message
#

subject="Emailing Myself"
print(subject)

html="<p>Hello World</p>"
print(html)

message = Mail(
    from_email=SENDER_ADDRESS,
    to_emails=SENDER_ADDRESS, # emailing ourselves
    subject=subject,
    html_content=html
)

#
# send the message
#

response = client.send(message)
print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
print(response.status_code) #> 202 indicates SUCCESS
