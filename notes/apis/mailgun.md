# Mailgun for Sending Email
 
We can use the Mailgun API to send emails!

## Setup

Create account with university email address (i.e. `MAILGUN_SENDER_ADDRESS`). Click verification link sent to that address. Login to mailgun console. Find and click nav link about "Sending" email. 

From the domains page, note the sandbox domain provided to you by default (i.e. `MAILGUN_DOMAIN` like "sandbox______.mailgun.org"). 

From the overview page, find and click on API Key settings link on bottom right, then on the API Keys page, scroll down and click the button to create a new API Key (i.e. `MAILGUN_API_KEY`).

> NOTE: Sandbox domains are restricted to authorized recipients only. So you'll only be able to send emails to yourself and a handful of "beta tester" friends and family until / unless you register your own domain later.

> NOTE: if you see 403 error when sending email to yourself, try registering your own email address as an "Authorized Recipient", and click the verification email, and try sending again


## Configuration

Strategy for secret credentials depends on development environment. If on Colab, use notebook secrets. Otherwise if developing in a local repo, use [environment variables](/notes/environment-variables/README.md), ideally in conjunction with a [".env" file approach](/notes/python/packages/dotenv.md).




A) Colab (reading notebook secrets):

```py
from google.colab import userdata

MAILGUN_SENDER_ADDRESS = userdata.get("MAILGUN_SENDER_ADDRESS") #  "example@georgetown.edu"
MAILGUN_DOMAIN = userdata.get("MAILGUN_DOMAIN") #  "sandbox______.mailgun.org"
MAILGUN_API_KEY = userdata.get("MAILGUN_API_KEY")
```


B) Local development (reading environment variables):

```py
import os
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_SENDER_ADDRESS = os.getenv("MAILGUN_SENDER_ADDRESS")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN") # "sandbox__________.mailgun.org"
```

## Usage

```py
import requests

def send_email(recipient_address=MAILGUN_SENDER_ADDRESS, subject="[Shopping Cart App] Testing 123", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    try:
        request_url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
        message_data = {
            'from': MAILGUN_SENDER_ADDRESS,
            'to': recipient_address,
            'subject': subject,
            'html': html_content,
        }
        response = requests.post(request_url,
            auth=('api', MAILGUN_API_KEY),
            data=message_data
        )
        print("RESULT:", response.status_code)
        response.raise_for_status()
        print("Email sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {str(e)}")



send_email()
```
