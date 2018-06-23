import datetime
import requests
import pytz

def mainMethod(*args):
    # To get a new Slack token, create an app on Slack's website, and get the token from there
    slackToken = "YOUR_SLACK_TOKEN_HERE"
    userTimeZone = "US/Pacific"

    # Get the current time in the specified timezone
    # Convert to AM/PM time, and round down to the half hour
    
    timezone = pytz.timezone(userTimeZone)
    timeNow = datetime.datetime.now(timezone)
    hour = timeNow.hour
    minute = timeNow.minute

    if hour > 12:
        hour = hour - 12

    if minute < 30:
        minute = 0
    elif minute > 30:
        minute = 30

    requestUrl = "https://slack.com/api/users.profile.set?token=" \
        + slackToken + "&profile=%7B%22status_text%22%3A%22" + str(hour) \
        + ":" + str(minute) + "%22%2C%22status_emoji%22%3A%22%3Aclock" + str(hour)
        
    # Only append the minute if it's on the half hour
    if minute == 30:
        requestUrl = requestUrl + str(minute)
    requestUrl = requestUrl + "%3A%22%7D"
    requests.post(requestUrl)