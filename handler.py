import os
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token=os.environ['TFANDKUSU_SLACK_API_KEY'])

def hello(event, context):
    response = client.chat_postMessage(
        channel='#random',
        text="Hello world!")
    return "Success"
