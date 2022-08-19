# run this file to set up your google account

# you will need to be a test user for this to work
# test users can be added at https://console.cloud.google.com/apis/credentials/consent?authuser=6&project=calcium-tea-354607&supportedpurview=project

# this will setup and save your credentials for future use

import pickle

from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("./googleapi/client_secrets.json", scopes=scopes)
credentials = flow.run_console()

pickle.dump(credentials, open("./googleapi/token.pkl", "wb")) 
