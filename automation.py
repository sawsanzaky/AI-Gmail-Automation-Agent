from gmail_service import (
    get_gmail_service,
    get_new_emails
)

from ai_agent import analyze_email

from sheets_service import (
    get_google_service,
    append_email_result
)


def process_emails(spreadsheet_id):

    gmail = get_gmail_service()

    sheets, drive = get_google_service()

    emails = get_new_emails(
        gmail,
        max_results=10
    )

    processed = 0

    for email in emails:

        try:

            ai_result = analyze_email(

                email["sender"],

                email["subject"],

                email["body"]

            )

            append_email_result(

                sheets,

                spreadsheet_id,

                email,

                ai_result

            )

            processed += 1

        except Exception as e:

            print(
                f"Error processing email: {e}"
            )

    return processed