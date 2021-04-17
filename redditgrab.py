from dotenv import load_dotenv
import sys
import os
import praw
import json

load_dotenv()

client_id=os.environ.get('REDDIT_PERSONAL_USE_SCRIPT')
client_secret=os.environ.get('REDDIT_SECRET')
user_agent=os.environ.get('REDDIT_APP_NAME')
username=os.environ.get('REDDIT_USERNAME')
password=os.environ.get('REDDIT_PASSWORD')

reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)

subreddit = reddit.subreddit('teenagers')
postInfo = {
    "id": "",
    "title": "",
    "text": "",
    "emojiCoef": 0.0,
    "user": "",
    "topic": "",
    "subtopic": "",
    "url": ""
}
for submission in subreddit.top(limit=20):
    if submission.selftext == '':
        continue
    initialLength = len(submission.selftext)
    bodyText = submission.selftext.encode("ascii", "ignore")
    cleanedText = bodyText.decode(encoding='UTF-8',errors='strict')
    cleanedText = cleanedText.replace('\n', ' ')
    if len(bodyText) > 2000:
        bodyText = bodyText[0:2000]
    emojiCoefficient = round(1 - len(bodyText)/initialLength, 2)

    postInfo["id"] = submission.id + "#" + submission.subreddit_id
    postInfo["title"] = submission.title
    postInfo["text"] = cleanedText
    postInfo["emojiCoef"] = emojiCoefficient
    postInfo["user"] = str(submission.author)
    postInfo["topic"] = "reddit"
    postInfo["subtopic"] = submission.subreddit_name_prefixed
    postInfo["url"] = submission.url

    json_object = json.dumps(postInfo)



    