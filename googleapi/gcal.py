import datetime
import pickle
import time
import json

from apiclient.discovery import build

credentials = pickle.load(open("./googleapi/token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)


def get_raw_events():
    all_calendars = service.calendarList().list().execute()
    calendar_id = all_calendars['items'][0]['id']
    return json.loads(str(service.events().list(calendarId=calendar_id).execute()['items']).replace('"', '').replace("'", '"').replace("True", "true").replace("False", "false"))


def get_future_events():
    all_events = get_raw_events()
    formatted_events = []
    date = datetime.datetime.now
    for event in all_events:
        if "dateTime" not in event['start']:
            continue
        if event['start']['dateTime'] > date().isoformat():
            formatted_events.append(event)
    return formatted_events


def get_formatted_events():
    for event in get_future_events():
        yield(event['summary'], event['start']['dateTime'][:10], event['start']['dateTime'][11:16])

# while True:
#     for event in get_future_events():
#         print(event['summary'], event['start']['dateTime'][11:16])
#     time.sleep(5)

# print(get_raw_events())
