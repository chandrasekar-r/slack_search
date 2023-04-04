import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_API_TOKEN'])

def fetch_all_channels():
    channels = []
    try:
        result = client.conversations_list()
        channels = result['channels']
    except SlackApiError as e:
        print(f"Error fetching channels: {e}")
    return channels

def fetch_messages(channel_id):
    messages = []
    try:
        result = client.conversations_history(channel=channel_id)
        messages = result['messages']
    except SlackApiError as e:
        print(f"Error fetching messages: {e}")
    return messages

def fetch_messages_from_all_channels():
    all_messages = []
    channels = fetch_all_channels()
    for channel in channels:
        messages = fetch_messages(channel['id'])
        all_messages.extend(messages)
    return all_messages
