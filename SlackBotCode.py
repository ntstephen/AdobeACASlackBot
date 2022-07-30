import logging


#Loading Assets
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler 

#Confused on this part???
logging.basicConfig(level=logging.INFO)

#Loading Slack Credentials 
load_dotenv()

SLACK_BOT_TOKEN = "xoxb-3885365966273-3875161703284-dwCjRJlilW1j1uIXwkLC6oqK"
SLACK_APP_TOKEN = "xapp-1-A03SCD4F080-3866115550438-9f3531f78401830bc1ee982a453a2eb8552e502436db32f489eea0a6e5dc93f0"

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