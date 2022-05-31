# https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
# https://www.youtube.com/watch?v=4ssigWmExak
# pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


from google.oauth2 import service_account
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1hY6-iAXLCjycgzqewua6XAD9Ca-eq-MFnybWQrr9-O4'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
print(result)


