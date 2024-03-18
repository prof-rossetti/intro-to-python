# The `sendgrid` Package

> FYI: [KNOWN ISSUES WITH SENDGRID](https://github.com/prof-rossetti/intro-to-python/issues/41)

The `sendgrid` package provides some useful emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

Reference:

  + [Source](https://github.com/sendgrid/sendgrid-python)
  + [Package](https://pypi.python.org/pypi/sendgrid)
  + [Example Usage](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py)
  + [SendGrid Account Types, including Free Tier](https://sendgrid.com/pricing/)
  + [SendGrid Account Signup](https://signup.sendgrid.com/)
  + [Obtaining API Keys](https://app.sendgrid.com/settings/api_keys)
  + [Email Templates](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/)


## Installation

Installing the package, as necessary:

```sh
pip install sendgrid

# optionally install a specific version:
#pip install sendgrid==6.6.0
```

> NOTE: we'll want to make sure the installed version is greater than 6.0.5, because earlier versions of this package worked differently, and the code examples in this document only apply to the newer versions.

## Setup

First, [sign up for a SendGrid account](https://signup.sendgrid.com/), and click the verification link sent to your email address.

Then follow the instructions to complete your "Single Sender Verification", clicking the link in another confirmation email to verify your single sender address. You should also be able to access via the settings menu:

![](https://user-images.githubusercontent.com/1328807/85074750-0cb54c00-b18b-11ea-940f-769cbcde53ad.png)

> NOTE: some students have reported that yahoo-issued, university-issued, and work-issued email addresses may be less likely to work. So if you run into issues with these kinds of addresses, perhaps try a Gmail address.

Moving forward we will reference this single sender address as the `SENDER_ADDRESS`.

Finally, [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions (i.e. the `SENDGRID_API_KEY`).

## Usage

### Authorization


We'll need to handle secret credentials differently, depending on the development environment.

#### Credentials in Colab

If working in a Colab notebook, we'll use [`getpass`](./../modules/getpass.md) to ask for a secure user input (for the API key, and the sender email address):

```py
from getpass import getpass

SENDGRID_API_KEY = getpass("Please input your Sendgrid API Key: ")
SENDER_ADDRESS = getpass("Please input your Sender Email Address: ")
```

#### Credentials in Local Development Project

Otherwise, if working locally, we'll use [Environment Variables](./../../environment-variables/README.md) to specify the secret credentials, ideally in conjunction with a [".env" file approach](/notes/python/packages/dotenv.md):

```py
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
```


### Sending Emails

After you have configured your credentials, use the code below to send yourself an email:

```py
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client)) #> <class 'sendgrid.sendgrid.SendGridAPIClient>

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
print("HTML:", html_content)

message = Mail(
    from_email=SENDER_ADDRESS, # needs to be the verified sender address
    to_emails=SENDER_ADDRESS, # can specify any recipient address, but self-sending here for demo purposes
    subject=subject,
    html_content=html_content
)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)

```

> NOTE: if you see a status code of 202, it means the message was sent successfully

Check your inbox:

![](/img/notes/python/packages/sendgrid/email-screenshot.png)

> NOTE: this message might take a minute to send, and it might be in your spam folder to start (in which case click "this email looks safe")


### Customizing HTML Content

For the mail object's `html_content` parameter, we can use a simple string like the example above, or we can start to use some HTML content:

```py
html_content = "Hello <strong>World</strong>"
print(html_content)
```

```py
html_content = f"""
<h3>Hello this is your receipt</h3>
<p>Date: ____________</p>
<ol>
    <li>You ordered: Product 1</li>
    <li>You ordered: Product 2</li>
    <li>You ordered: Product 3</li>
</ol>
"""
print(html_content)
```

> NOTE: for students unfamiliar with HTML syntax, first see these notes about [Basic HTML](https://www.w3schools.com/html/html_basic.asp) and [HTML Lists](https://www.w3schools.com/html/html_lists.asp).

### Attachments

References:
  + https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python
  + https://stackoverflow.com/questions/69419892/how-to-send-email-with-dataframe-as-attachment-using-sendgrid-api-in-python

Send email with file attachment(s):

```py
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId

#
# PREPARE MESSAGE
#

subject="Unemployment"
html="<p>This is your Unemployment Report! See attached files.</p>"

client = SendGridAPIClient(SENDGRID_API_KEY)
message = Mail(
    from_email=SENDER_ADDRESS,
    to_emails=SENDER_ADDRESS,
    subject=subject,
    html_content=html
)

# encoding CSV files:
csv_filepath = "my_data.csv" # path / name of existing file
encoded_csv = base64.b64encode(df.to_csv(index=False).encode()).decode()

# attaching the file:
message.attachment = Attachment(
    file_content = FileContent(encoded_csv),
    file_type = FileType('text/csv'),
    file_name = FileName('unemployment_report.csv'), # FileName('JuicyLiftWorkout.pdf')
    disposition = Disposition('attachment'),
    content_id = ContentId('Attachment 1')
)

# encoding binary files, like PDFs or images:
img_filepath = "my_image.png" # path / name of existing file
with open(img_filepath, 'rb') as f:
    data = f.read()
    f.close()
encoded_img = base64.b64encode(data).decode()

# attach the file:
message.attachment = Attachment(
    file_content = FileContent(encoded_img),
    file_type = FileType('image/png'),
    file_name = FileName('unemployment_chart.png'),
    disposition = Disposition('attachment'),
    content_id = ContentId('Attachment 2')
)

#
# SEND MESSAGE
#

response = client.send(message)
print(response.status_code)
```

> NOTE: common file attachment types include:
  + `'text/csv'`
  + `'image/png'`
  + `'image/jpeg'`
  + `'application/pdf'`



### [Email Templates](sendgrid/email-templates.md)
