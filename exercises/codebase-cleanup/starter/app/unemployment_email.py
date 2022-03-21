

print("UNEMPLOYMENT REPORT...")


import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# docs: https://www.alphavantage.co/documentation/#unemployment
url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(url)
parsed_response = json.loads(response.text)
#print(parsed_response)

data = parsed_response["data"]
latest = data[0]
print(latest) #> {'date': '2022-02-01', 'value': '3.8'}


#exit()

#
# DATA AND CHARTING
#

from pandas import DataFrame
from plotly.express import bar


df = DataFrame(data)
print(df.head())

fig = bar(df, x="date", y="value", title="Unemployment Rates")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
# https://plotly.com/python/reference/layout/yaxis/
# https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix
fig.update_yaxes(
    #tickprefix="$",
    ticksuffix="%",
    showgrid=True
)

fig.show()

#breakpoint()


print("DATAVIZ EXPORT...")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
# fig.to_image(format="png")

# https://plotly.com/python/static-image-export/
# Image export using the "kaleido" engine requires the kaleido package,
#which can be installed using pip:
#    $ pip install -U kaleido
img_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.png")
fig.write_image(img_filepath)


print("CSV EXPORT...")
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
df.to_csv(csv_filepath, index=False)



#
# EMAIL
#
# with attachment: https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python
# (csv specific): https://stackoverflow.com/questions/69419892/how-to-send-email-with-dataframe-as-attachment-using-sendgrid-api-in-python

import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId

load_dotenv()

# obtain api key at https://sendgrid.com/
# and verify single sender with a given email address...
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")


#prep email

subject="Unemployment"
html="<p>Unemployment Report</p>"

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html)

# for CSV files:
encoded_csv = base64.b64encode(df.to_csv(index=False).encode()).decode()

# attach the file:
message.attachment = Attachment(
    file_content = FileContent(encoded_csv),
    file_type = FileType('text/csv'), # FileType('application/pdf')
    file_name = FileName('unemployment_report.csv'), # FileName('JuicyLiftWorkout.pdf')
    disposition = Disposition('attachment'),
    content_id = ContentId('Attachment 1')
)


# for binary files, like PDFs and images:
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



#send email
response = client.send(message)
print(response.status_code)
