import os
from datetime import datetime, timedelta, timezone
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token=os.environ['TFANDKUSU_SLACK_API_KEY'])

def hello(event, context):
    jst = timezone(timedelta(hours=9), 'JST')
    now = datetime.now(jst)
    timestr = now.strftime('%Y/%m/%d %H:%M:%S')
    response = client.chat_postMessage(
        channel='#random',
        text="Current time is " + timestr)
    return "Success"
