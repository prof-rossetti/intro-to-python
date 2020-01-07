# The `twilio` Package

The `twilio` package provides some useful programmatic SMS and voice message capabilities via the [Twilio Service](https://www.twilio.com/).

Reference:

  + [Source](https://github.com/twilio/twilio-python)
  + [Package](https://pypi.python.org/pypi/twilio)
  + [Documentation](https://www.twilio.com/docs/libraries/python)

## Installation

Install `twilio`, if necessary:

```sh
pip install twilio
```

## Setup

For SMS capabilities, [sign up for a Twilio account](https://www.twilio.com/try-twilio), click the link in a confirmation email to verify your account, then confirm a code sent to your phone to enable 2FA.

Then [create a new project](https://www.twilio.com/console/projects/create) with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`, respectively.

You'll also need to [obtain a Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called `SENDER_SMS`.

Finally, set an environment variable called `RECIPIENT_SMS` to specify the recipient's phone number (including the plus sign at the beginning).

## Usage

Send yourself an SMS:

```python
import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

# AUTHENTICATE

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

content = "Hello, this is a message from your personal notification service. TODO: customize me!"

# ISSUE REQUEST (SEND SMS)

message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

# PARSE RESPONSE

print("----------------------")
print("SMS")
print("----------------------")
print("RESPONSE: ", type(message))
print("FROM:", message.from_)
print("TO:", message.to)
print("BODY:", message.body)
print("PROPERTIES:")
print(message._properties))
```
