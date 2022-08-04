#Import
import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler 

#Config
logging.basicConfig(level=logging.INFO)
load_dotenv()

#Tokens
SLACK_BOT_TOKEN = os.getenv("BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("APP_TOKEN")
#print(SLACK_BOT_TOKEN)

#Creating an isntance of a Slack App
app = App(token=SLACK_BOT_TOKEN)

#App Mention Events
@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    say("Hello World")

@app.event("message")
def message_handler(body, context, payload, options, say, event):
    pass

#Designate main fucntion and start handlers
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()