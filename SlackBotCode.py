#Adobe Tutorial Imports
from email import header
import logging
import os
from tarfile import REGULAR_TYPES
from tkinter import Y
from typing import Counter
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler 

#Web Scrapping Imports
from bs4 import BeautifulSoup
import requests
import WebScrap
import index
from csv import list_dialects, writer

#Config
logging.basicConfig(level=logging.INFO)
load_dotenv()

#Tokens
SLACK_BOT_TOKEN = os.getenv("BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("APP_TOKEN")


#Creating an isntance of a Slack App
app = App(token=SLACK_BOT_TOKEN)

#Upload File
def send_file_to_slack(file_path):

    payload={
    "filename":"myfile.pdf", 
    "token":f"{SLACK_APP_TOKEN}", 
    "channels":['#slackbotdevelopment'], 
    }

    file_upload = {
        "file": (file_path, open(file_path, 'rb'), 'csv')
    }

    requests.post("https://slack.com/api/files.upload", params=payload, files=file_upload)

#App Mention Events
@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    print(event)
    say("Hello World")
    data = 'data.csv'
    with open('data.csv', 'w', encoding='utf8', newline='') as f:
        theWriter = writer(f)
        Counter = 0
        header = ["Title", "URL"]
        theWriter.writerow(header)
        for articles in WebScrap.filtered_title:
            theWriter.writerow([WebScrap.filtered_title[Counter], WebScrap.filtered_list[Counter]])
            Counter += 1
    send_file_to_slack('/Users/Nathan Stephen/Desktop/SlackBot/AdobeACASlackBot/data.csv')

@app.event("message")
def message_handler(body, context, payload, options, say, event):
    pass


#Designate main fucntion and start handlers
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

print(WebScrap.filtered_title)
print(WebScrap.filtered_list)



