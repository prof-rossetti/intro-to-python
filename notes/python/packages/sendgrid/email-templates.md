

Sendgrid Email Templates

> Thanks to former student @mgallea for sharing the email template capabilities


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
