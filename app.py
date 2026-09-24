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
    :root {
        --bg-deep: #07111f;
        --bg-mid: #0f1d34;
        --bg-soft: #122a45;
        --panel: rgba(11, 22, 38, 0.72);
        --panel-border: rgba(148, 163, 184, 0.18);
        --text: #e2e8f0;
        --muted: #94a3b8;
        --primary: #7c3aed;
        --secondary: #22d3ee;
        --accent: #f59e0b;
        --success: #34d399;
    }

    html, body {
        height: 100%;
    }

    body {
        background: radial-gradient(circle at top left, rgba(124, 58, 237, 0.35), transparent 28%),
                    radial-gradient(circle at bottom right, rgba(34, 211, 238, 0.25), transparent 25%),
                    linear-gradient(135deg, var(--bg-deep), var(--bg-mid) 45%, var(--bg-soft));
    }

    .stApp {
        background: transparent;
    }

    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, rgba(124, 58, 237, 0.28), transparent 23%),
                    radial-gradient(circle at bottom right, rgba(34, 211, 238, 0.22), transparent 20%),
                    linear-gradient(135deg, rgba(7, 17, 31, 0.96), rgba(15, 29, 52, 0.96));
    }

    [data-testid="stAppViewContainer"] > .main {
        background: transparent;
    }

    [data-testid="stHeader"] {
        background: rgba(15, 23, 42, 0.35);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(148, 163, 184, 0.18);
    }

    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.72);
        border-right: 1px solid rgba(148, 163, 184, 0.14);
        backdrop-filter: blur(18px);
    }

    .main-title {
        position: relative;
        z-index: 2;
        font-size: 38px;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin-bottom: 8px;
        background: linear-gradient(90deg, #f8fafc, #7dd3fc, #c4b5fd, #f8fafc);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 18px rgba(125, 211, 252, 0.18);
    }

    .subtitle {
        position: relative;
        z-index: 2;
        color: #dbeafe;
        font-size: 17px;
        margin-bottom: 28px;
        opacity: 0.95;
    }

    .scene {
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }

    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(18px);
        opacity: 0.62;
        animation: float 18s ease-in-out infinite alternate;
    }

    .orb-1 {
        width: 420px;
        height: 420px;
        background: radial-gradient(circle, rgba(124, 58, 237, 0.8), rgba(124, 58, 237, 0.18), transparent 68%);
        top: 6%;
        left: 8%;
    }

    .orb-2 {
        width: 460px;
        height: 460px;
        background: radial-gradient(circle, rgba(34, 211, 238, 0.8), rgba(34, 211, 238, 0.18), transparent 70%);
        bottom: 8%;
        right: 8%;
        animation-delay: 1.5s;
    }

    .orb-3 {
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(251, 146, 60, 0.7), rgba(251, 146, 60, 0.18), transparent 72%);
        top: 25%;
        right: 28%;
        animation-delay: 3s;
    }

    .grid-glow {
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(148, 163, 184, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(148, 163, 184, 0.05) 1px, transparent 1px);
        background-size: 28px 28px;
        mask-image: radial-gradient(circle at center, black 35%, transparent 90%);
        opacity: 0.55;
    }

    .stAlert, .stSuccess, .stError, .stInfo {
        background: rgba(15, 23, 42, 0.68);
        border: 1px solid rgba(148, 163, 184, 0.18);
        backdrop-filter: blur(10px);
    }

    .email-card {
        position: relative;
        padding: 22px 22px 18px 22px;
        margin-bottom: 18px;
        border-radius: 18px;
        border: 1px solid rgba(148, 163, 184, 0.19);
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.86), rgba(17, 24, 39, 0.72));
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.28);
        backdrop-filter: blur(14px);
        overflow: hidden;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .email-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(96, 165, 250, 0.12);
    }

    .email-card::before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 4px;
        background: linear-gradient(180deg, #22d3ee, #7c3aed, #f59e0b);
    }

    .email-subject {
        font-size: 20px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 10px;
    }

    .email-label {
        display: inline-block;
        min-width: 70px;
        color: #93c5fd;
        font-weight: 700;
    }

    .stExpander {
        background: rgba(15, 23, 42, 0.58);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 12px;
    }

    .stExpander > div {
        background: transparent;
    }

    @keyframes float {
        0% {
            transform: translate3d(0, 0, 0) scale(1);
        }
        100% {
            transform: translate3d(25px, -28px, 0) scale(1.08);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="scene">
        <div class="grid-glow"></div>
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>
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
