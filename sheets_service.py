import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_google_service():

    creds = None

    if os.path.exists("google_token.json"):

        creds = Credentials.from_authorized_user_file(
            "google_token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            creds.refresh(
                Request()
            )

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(
                port=0
            )

        with open(
            "google_token.json",
            "w"
        ) as token:

            token.write(
                creds.to_json()
            )

    sheets = build(
        "sheets",
        "v4",
        credentials=creds
    )

    drive = build(
        "drive",
        "v3",
        credentials=creds
    )

    return sheets, drive


def create_spreadsheet(sheets, title):

    spreadsheet = {
        "properties": {
            "title": title
        }
    }

    result = sheets.spreadsheets().create(
        body=spreadsheet,
        fields="spreadsheetId,spreadsheetUrl"
    ).execute()

    spreadsheet_id = result["spreadsheetId"]

    headers = [[
        "Date",
        "Sender",
        "Subject",
        "Summary",
        "Category",
        "Priority",
        "Deadline",
        "Action Required",
        "Department",
        "Sentiment"
    ]]

    sheets.spreadsheets().values().update(

        spreadsheetId=spreadsheet_id,

        range="Sheet1!A1:J1",

        valueInputOption="RAW",

        body={
            "values": headers
        }

    ).execute()

    return result


def append_email_result(
    sheets,
    spreadsheet_id,
    email_data,
    ai_data
):

    from datetime import datetime

    row = [[

        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        email_data["sender"],

        email_data["subject"],

        ai_data.get(
            "summary",
            ""
        ),

        ai_data.get(
            "category",
            ""
        ),

        ai_data.get(
            "priority",
            ""
        ),

        ai_data.get(
            "deadline",
            ""
        ),

        ai_data.get(
            "action_required",
            ""
        ),

        ai_data.get(
            "department",
            ""
        ),

        ai_data.get(
            "sentiment",
            ""
        )

    ]]

    sheets.spreadsheets().values().append(

        spreadsheetId=spreadsheet_id,

        range="Sheet1!A:J",

        valueInputOption="USER_ENTERED",

        insertDataOption="INSERT_ROWS",

        body={
            "values": row
        }

    ).execute()