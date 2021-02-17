# The `sendgrid` Package

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

First, [sign up for a SendGrid account](https://signup.sendgrid.com/), then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.

Then [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions. We'll want to store the API Key value in an [environment variable](/notes/environment-variables.md) called `SENDGRID_API_KEY`.

Also set an environment variable called `SENDER_ADDRESS` to be the same email address as the single sender address you just associated with your SendGrid account (e.g. "abc123@gmail.com").

Use a [".env" file approach](/notes/python/packages/dotenv.md) to managing these environment variables.

## Usage

Send yourself an email:

```py
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

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


### Email Templates

An alternative way to compile the email content is to use a "dynamic email template" whereby we'll specify some common HTML structure that will apply to all emails, and pass specific data to populate the template for each specific email. Let's try sending a simple receipt via template.

![](/img/notes/python/packages/sendgrid/receipt-screenshot.png)

Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "example-receipt", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called `SENDGRID_TEMPLATE_ID`.

![](/img/notes/python/packages/sendgrid/create-template.png)

Back in the SendGrid platform, click "Add Version" to create a new version of a "Blank Template" and select the "Code Editor" as your desired editing mechanism.

![](/img/notes/python/packages/sendgrid/create-template-version.png)

At this point you should be able to paste the following HTML into the "Code" tab, and the corresponding example data in the "Test Data" tab, and save each after you're done editing them.

Example "Code" template which will specify the structure of all emails:

```html
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```

> NOTE: the ["handlebars" syntax above](https://sendgrid.com/docs/for-developers/sending-email/using-handlebars) is like HTML, but allows us to construct HTML dynamically based on some data (in this case it wants us to pass it `human_friendly_timestamp`, `products`, and `total_price_usd` variables)

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

After configuring and saving the email template, we should be able to use it to send an email:

```py
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

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
