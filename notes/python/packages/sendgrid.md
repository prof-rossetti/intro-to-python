# The `sendgrid` Package

> FYI: [KNOWN ISSUES WITH SENDGRID](https://github.com/prof-rossetti/intro-to-python/issues/41)

The `sendgrid` package provides some useful emailing capabilities via the [SendGrid Email Delivery Service](https://sendgrid.com/solutions/email-api/). :mailbox_with_mail: :envelope:

Reference:

  + [Source](https://github.com/sendgrid/sendgrid-python)
  + [Package](https://pypi.python.org/pypi/sendgrid)
  + [Example Usage](https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail/mail_example.py)
  + [Heroku's SendGrid Guide](https://devcenter.heroku.com/articles/sendgrid)
  + [SendGrid Account Types, including Free Tier](https://sendgrid.com/pricing/)
  + [SendGrid Account Signup](https://signup.sendgrid.com/)
  + [Obtaining API Keys](https://app.sendgrid.com/settings/api_keys)
  + [Email Templates](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/)

> Thanks to former student @mgallea for discovering the email template capabilities

## Installation

From within an active virtual environment, install the `sendgrid` package:

```sh
pip install sendgrid

# optionally install a specific version:
#pip install sendgrid==6.6.0
```

> NOTE: we'll want to make sure the installed version is greater than 6.0.5, because earlier versions of this package worked differently, and the code examples in this document only apply to the newer versions.

## Setup

First, [sign up for a SendGrid account](https://signup.sendgrid.com/), then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account. You should also be able to access this via the settings menu:

![](https://user-images.githubusercontent.com/1328807/85074750-0cb54c00-b18b-11ea-940f-769cbcde53ad.png)

> NOTE: some students have reported that yahoo-issued, university-issued, and work-issued email addresses may be less likely to work. So if you run into issues with these kinds of addresses, perhaps try a Gmail address.


Then [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. We'll want to store the API Key value in an [environment variable](/notes/environment-variables/README.md) called `SENDGRID_API_KEY`.

Also set an environment variable called `SENDER_ADDRESS` to be the same email address as the single sender address you just associated with your SendGrid account.

## Usage

### Handling Secret Credentials

We'll need to handle secret credentials differently depending on our development environment.

If working in a Colab notebook, use [`getpass`](/notes/python/modules/getpass.md) to ask for a secure user input (at least for the API key, and probably also for your email address as well):


```py
# NOTEBOOK APPROACH (ask for secure user inputs)

from getpass import getpass
 
SENDGRID_API_KEY = getpass("Please input your Sendgrid API Key: ")
SENDER_ADDRESS = getpass("Please input your Sender Email Address: ")

```

Otherwise, if working locally, we'll use [Environment Variables](/notes/environment-variables/README.md) to specify the secret credentials, ideally in conjunction with a [".env" file approach](/notes/python/packages/dotenv.md):

```py
# LOCAL DEVELOPMENT APPROACH (use environment variables)

import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

```


### Sending Emails

Send yourself an email (using secret credentials from setup above):

```py
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
print("HTML:", html_content)

# FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
# ... but we can customize the `to_emails` param to send to other addresses
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

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

> NOTE: this message might take a minute to send, and it might be in your spam folder to start


### Compiling HTML Content

For the mail object's `html_content` parameter, we can use a simple string like the example above, or we can start to use some HTML content:

```py
# ...

html_content = "Hello <strong>World</strong>"
print(html_content)

# ...
```

... or we can even compile an entire HTML document into a single string:

```py
# ...

html_list_items = "<li>You ordered: Product 1</li>"
html_list_items += "<li>You ordered: Product 2</li>"
html_list_items += "<li>You ordered: Product 3</li>"

html_content = f"""
<h3>Hello this is your receipt</h3>
<p>Date: ____________</p>
<ol>
    {html_list_items}
</ol>
"""
print(html_content)

# ...
```

> NOTE: for students unfamiliar with HTML syntax, first see these notes about [Basic HTML](https://www.w3schools.com/html/html_basic.asp) and [HTML Lists](https://www.w3schools.com/html/html_lists.asp).

### Email Templates

An alternative way to compile the email content is to use a "dynamic email template" whereby we'll specify some common HTML structure that will apply to all emails, and pass specific data to populate the template for each specific email. Let's try sending a simple receipt via template.

![](/img/notes/python/packages/sendgrid/receipt-screenshot.png)

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called `SENDGRID_TEMPLATE_ID`.

![](/img/notes/python/packages/sendgrid/create-template.png)

Back in the SendGrid platform, click "Add Version" to create a new version of a "Blank Template" and select the "Code Editor" as your desired editing mechanism.

![](/img/notes/python/packages/sendgrid/create-template-version.png)

At this point you should be able to paste the following HTML into the "Code" tab, and the corresponding example data in the "Test Data" tab, and save each after you're done editing them.

Example "Code" template which will specify the structure of all emails :

```html
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}} </li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```

> NOTE: the ["handlebars" syntax above](https://sendgrid.com/docs/for-developers/sending-email/using-handlebars) is like HTML, but allows us to construct HTML dynamically based on some data (in this case it wants us to pass it `human_friendly_timestamp`, `products`, and `total_price_usd` variables)

> NOTE: the product-level information provided in the example code template references each product dictionary's "name" attribute (matching the template data below), but you'll probably want to include a formatted version of the product price as well.

Example "Test Data" which will populate the template:

```py
{
    "total_price_usd": "$99.99",
    "human_friendly_timestamp": "July 4th, 2099 10:00 AM",
    "products":[
        {"id": 100, "name": "Product 100"},
        {"id": 200, "name": "Product 200"},
        {"id": 300, "name": "Product 300"},
        {"id": 200, "name": "Product 200"},
        {"id": 100, "name": "Product 100"}
    ]
}
```

> NOTE: when we send real emails using this template, we'll pass dynamic data with different values, but it should resemble this test data structure.

Finally, configure the template's subject by clicking on "Settings" in the left sidebar. Choose an email subject like "Your Receipt from the Green Grocery Store". Then click "Save Template".

![](/img/notes/python/packages/sendgrid/template-settings.png)

After configuring and saving the email template, we should be able to use it to send an email (using secret credentials from setup above):

```py
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# colab notebook version (user input, doesn't have to be secure):
SENDGRID_TEMPLATE_ID = input("Please input your SENDGRID_TEMPLATE_ID: ") 
# OR local version (use env vars):
# SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")

# this must match the test data structure
template_data = {
    "total_price_usd": "$14.95",
    "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
    "products":[
        {"id":1, "name": "Product 1"},
        {"id":2, "name": "Product 2"},
        {"id":3, "name": "Product 3"},
        {"id":2, "name": "Product 2"},
        {"id":1, "name": "Product 1"}
    ]
} # or construct this dictionary dynamically based on the results of some other process :-D

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
message.template_id = SENDGRID_TEMPLATE_ID
message.dynamic_template_data = template_data
print("MESSAGE:", type(message))

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)
```

![](/img/notes/python/packages/sendgrid/receipt-screenshot.png)


### Attachments

References:
  + https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python
  + https://stackoverflow.com/questions/69419892/how-to-send-email-with-dataframe-as-attachment-using-sendgrid-api-in-python

Send email with attachment(s), using secret credentials from setup above :

```py
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId

# PREPARE MESSAGE

subject="Unemployment"
html="<p>This is your Unemployment Report! See attached files.</p>"

client = SendGridAPIClient(SENDGRID_API_KEY)
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html)

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


# SEND MESSAGE

response = client.send(message)
print(response.status_code)
```

> NOTE: common file attachment types include:
  + `'text/csv'`
  + `'image/png'`
  + `'image/jpeg'`
  + `'application/pdf'`
