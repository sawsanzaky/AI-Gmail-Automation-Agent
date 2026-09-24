import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ============================================================
# Gmail API permissions
# ============================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

# ============================================================
# File configuration
# ============================================================

CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


# ============================================================
# Connect to Gmail
# ============================================================

def get_gmail_service():

    print("\n========================================")
    print("      AI Gmail Automation Agent")
    print("========================================")
    print("Connecting to Google Gmail API...\n")

    creds = None

    # --------------------------------------------------------
    # Check credentials.json
    # --------------------------------------------------------

    if not os.path.exists(CREDENTIALS_FILE):
        raise FileNotFoundError(
            f"\nERROR: {CREDENTIALS_FILE} was not found.\n"
            f"Make sure it is inside the project folder:\n"
            f"{os.getcwd()}\n"
        )

    print(f"✓ Found {CREDENTIALS_FILE}")

    # --------------------------------------------------------
    # Load existing token
    # --------------------------------------------------------

    if os.path.exists(TOKEN_FILE):

        print(f"✓ Found {TOKEN_FILE}")
        print("Loading existing Google authentication...")

        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )

    # --------------------------------------------------------
    # Authenticate if necessary
    # --------------------------------------------------------

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            print("Refreshing Google authentication...")

            creds.refresh(Request())

        else:

            print("\n----------------------------------------")
            print("Google authorization is required.")
            print("----------------------------------------")
            print("A browser window will open.")
            print("Sign in with your Google account:")
            print("sawsanzaky93@gmail.com")
            print("----------------------------------------\n")

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            # Start local OAuth server
            creds = flow.run_local_server(
                host="localhost",
                port=0,
                open_browser=True
            )

        # ----------------------------------------------------
        # Save authentication token
        # ----------------------------------------------------

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

        print("\n✓ Google authentication saved to token.json")

    # --------------------------------------------------------
    # Build Gmail service
    # --------------------------------------------------------

    print("Creating Gmail API service...")

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    print("✓ Gmail API connection successful!\n")

    return service


# ============================================================
# Get latest emails
# ============================================================

def get_latest_emails(max_results=5):

    service = get_gmail_service()

    print("Reading Gmail messages...")

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    print(f"✓ Found {len(messages)} email(s).\n")

    return messages


# ============================================================
# Get complete email information
# ============================================================

def get_email_details(message_id):

    service = get_gmail_service()

    message = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    return message


# ============================================================
# Test Gmail connection
# ============================================================

if __name__ == "__main__":

    try:

        print("\nStarting Gmail test...\n")

        emails = get_latest_emails(5)

        if not emails:

            print("No emails were found.")

        else:

            print("Latest Gmail message IDs:")
            print("----------------------------------------")

            for index, email in enumerate(emails, start=1):

                print(
                    f"{index}. "
                    f"Message ID: {email.get('id')}"
                )

        print("\n========================================")
        print("Gmail test completed.")
        print("========================================")

    except Exception as error:

        print("\n========================================")
        print("ERROR")
        print("========================================")
        print(type(error).__name__)
        print(str(error))
        print("========================================")

        raise
