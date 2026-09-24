import streamlit as st
from gmail_service import get_latest_emails, get_email_details


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Gmail Automation Agent",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# Custom CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #666;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .email-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
        background-color: #ffffff;
    }

    .email-subject {
        font-size: 20px;
        font-weight: 600;
    }

    .email-label {
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="main-title">🤖 AI Gmail Automation Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered Gmail monitoring and email automation'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("⚙️ Control Panel")

    st.success("🟢 Gmail Connected")

    max_emails = st.slider(
        "Number of emails",
        min_value=1,
        max_value=20,
        value=5
    )

    load_emails = st.button(
        "🔄 Load Emails",
        use_container_width=True
    )

    st.divider()

    st.subheader("System")

    st.write("📧 Gmail API")
    st.write("🤖 AI Agent")
    st.write("📊 Google Sheets")

    st.divider()

    st.caption(
        "AI Gmail Automation Agent"
    )


# ============================================================
# Load Emails
# ============================================================

if load_emails:

    with st.spinner("Reading Gmail messages..."):

        try:

            emails = get_latest_emails(max_emails)

            st.session_state["emails"] = emails

            st.success(
                f"✓ {len(emails)} email(s) loaded successfully."
            )

        except Exception as error:

            st.error(
                f"Gmail error: {error}"
            )


# ============================================================
# Display Emails
# ============================================================

if "emails" not in st.session_state:

    st.info(
        "👈 Click **Load Emails** to retrieve your latest Gmail messages."
    )

else:

    emails = st.session_state["emails"]

    st.subheader(
        f"📬 Latest Emails ({len(emails)})"
    )

    for index, email in enumerate(emails, start=1):

        try:

            message_id = email.get("id")

            message = get_email_details(message_id)

            payload = message.get(
                "payload",
                {}
            )

            headers = payload.get(
                "headers",
                []
            )

            sender = ""
            recipient = ""
            subject = ""
            date = ""

            for header in headers:

                name = header.get(
                    "name",
                    ""
                ).lower()

                value = header.get(
                    "value",
                    ""
                )

                if name == "from":
                    sender = value

                elif name == "to":
                    recipient = value

                elif name == "subject":
                    subject = value

                elif name == "date":
                    date = value


            # ------------------------------------------------
            # Email Card
            # ------------------------------------------------

            st.markdown(
                f"""
                <div class="email-card">

                <div class="email-subject">
                📧 {subject or "No Subject"}
                </div>

                <br>

                <div>
                <span class="email-label">From:</span>
                {sender}
                </div>

                <div>
                <span class="email-label">To:</span>
                {recipient}
                </div>

                <div>
                <span class="email-label">Date:</span>
                {date}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # Email Details
            # ------------------------------------------------

            with st.expander(
                f"View Email #{index} Details"
            ):

                st.write(
                    "**Message ID:**",
                    message_id
                )

                st.write(
                    "**Subject:**",
                    subject
                )

                st.write(
                    "**From:**",
                    sender
                )

                st.write(
                    "**To:**",
                    recipient
                )

                st.write(
                    "**Date:**",
                    date
                )

        except Exception as error:

            st.error(
                f"Unable to read email #{index}: {error}"
            )
