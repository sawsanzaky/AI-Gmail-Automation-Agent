<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:06B6D4&height=220&section=header&text=AI%20Gmail%20Automation%20Agent&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Turn%20inbox%20noise%20into%20structured%20business%20intelligence&descAlignY=60&descSize=18" width="100%" alt="AI Gmail Automation Agent banner" />

<p>
  <a href="https://github.com/sawsanzaky/AI-Gmail-Automation-Agent/stargazers"><img src="https://img.shields.io/github/stars/sawsanzaky/AI-Gmail-Automation-Agent?style=for-the-badge&logo=github&color=f59e0b" alt="GitHub stars" /></a>
  <a href="https://github.com/sawsanzaky/AI-Gmail-Automation-Agent/network/members"><img src="https://img.shields.io/github/forks/sawsanzaky/AI-Gmail-Automation-Agent?style=for-the-badge&logo=github&color=64748b" alt="GitHub forks" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" /></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
</p>

<p>
  <a href="https://groq.com/"><img src="https://img.shields.io/badge/Powered%20by-Groq-6C47FF?style=flat-square" alt="Powered by Groq" /></a>
  <a href="https://developers.google.com/gmail/api"><img src="https://img.shields.io/badge/Integration-Gmail%20API-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Gmail API" /></a>
  <a href="https://developers.google.com/sheets/api"><img src="https://img.shields.io/badge/Output-Google%20Sheets-34A853?style=flat-square&logo=googlesheets&logoColor=white" alt="Google Sheets" /></a>
</p>

<p><strong>Intelligent email processing and business workflow automation</strong></p>

<p>
  <a href="#-why-this-project">Why this project</a> ·
  <a href="#-capabilities">Capabilities</a> ·
  <a href="#-architecture">Architecture</a> ·
  <a href="#-quick-start">Quick start</a> ·
  <a href="#-configuration">Configuration</a>
</p>

</div>

---

## 🎯 Why this project?

Teams lose valuable time manually reading, classifying, summarizing, and routing email. **AI Gmail Automation Agent** creates a practical bridge between your Gmail inbox and your business operations.

It retrieves recent messages, asks an AI model to produce consistent business metadata, and writes the results to a structured Google Sheets workflow. A Streamlit interface provides a visual way to inspect the latest messages.

<div align="center">

| 📥 Capture | 🧠 Understand | 🗂️ Organize | 📊 Act |
|:---:|:---:|:---:|:---:|
| Gmail messages | AI summaries | Categories & priority | Sheets workflow |

</div>

## ✨ Capabilities

<table>
<tr>
<td width="50%">

### 📬 Gmail monitoring

- Authenticate with the Gmail API
- Retrieve recent messages
- Read sender, recipient, subject, date, and body
- Inspect messages through the Streamlit dashboard

</td>
<td width="50%">

### 🤖 AI email intelligence

- Generate concise business summaries
- Detect category and department
- Assign `Low`, `Medium`, or `High` priority
- Extract deadlines and required actions
- Identify email sentiment

</td>
</tr>
<tr>
<td width="50%">

### 🔁 Workflow automation

- Process new messages in batches
- Append AI results to Google Sheets
- Keep business information structured
- Reduce repetitive manual data entry

</td>
<td width="50%">

### 📈 Visual experience

- Clean Streamlit control panel
- Adjustable number of emails to load
- Expandable email detail cards
- Status indicators for connected services

</td>
</tr>
</table>

## 🧭 Workflow at a glance

```mermaid
flowchart LR
    A[(Gmail Inbox)] --> B[Fetch New Emails]
    B --> C[Extract Email Data]
    C --> D{Groq AI Agent}
    D --> E[Summary]
    D --> F[Category & Department]
    D --> G[Priority & Deadline]
    D --> H[Action & Sentiment]
    E --> I[(Google Sheets)]
    F --> I
    G --> I
    H --> I
    C --> J[Streamlit Dashboard]
    I --> K[Business Follow-up]

    classDef source fill:#EA4335,color:#fff,stroke:#b91c1c
    classDef ai fill:#6C47FF,color:#fff,stroke:#4c1d95
    classDef output fill:#34A853,color:#fff,stroke:#166534
    classDef ui fill:#FF4B4B,color:#fff,stroke:#991b1b
    class A source
    class D ai
    class I,K output
    class J ui
```

## 🏗️ Architecture

```mermaid
graph TD
    UI[app.py<br/>Streamlit UI] --> GS[gmail_service.py<br/>Gmail integration]
    AUTO[automation.py<br/>Batch orchestration] --> GS
    AUTO --> AI[ai_agent.py<br/>Groq analysis]
    AUTO --> SS[sheets_service.py<br/>Google Sheets / Drive]
    ENV[.env<br/>GROQ_API_KEY] --> AI
    GS --> AUTH[Google OAuth<br/>credentials & token]
```

## 📂 Project structure

```text
AI-Gmail-Automation-Agent/
├── app.py              # Streamlit dashboard for inspecting Gmail messages
├── automation.py       # Batch processing orchestration
├── ai_agent.py         # Groq-powered email analysis and JSON extraction
├── gmail_service.py    # Gmail API authentication and message retrieval
├── sheets_service.py   # Google Sheets / Drive integration
├── requirements.txt    # Python dependencies
├── .env                # Local secrets; never commit
└── README.md
```

## 🚀 Quick start

### 1. Clone the repository

```bash
git clone https://github.com/sawsanzaky/AI-Gmail-Automation-Agent.git
cd AI-Gmail-Automation-Agent
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> The application also imports `streamlit` and `groq`. If they are not already included in your local dependency file, install them with `pip install streamlit groq`.

### 4. Launch the dashboard

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 🔐 Configuration

### Groq

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### Google APIs

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a project.
3. Enable the **Gmail API**, **Google Sheets API**, and **Google Drive API**.
4. Configure the OAuth consent screen.
5. Create OAuth client credentials for a desktop application.
6. Download the credentials file expected by the Google service modules.
7. Complete the browser authentication flow on first run.

> Never publish API keys, OAuth client secrets, `credentials.json`, or generated token files. Confirm they are covered by `.gitignore` before committing.

## 🧪 AI output schema

For each processed message, the AI agent returns structured JSON:

```json
{
  "summary": "Concise business summary",
  "category": "Finance",
  "priority": "High",
  "deadline": "2026-10-01",
  "action_required": "Review and respond to the request",
  "department": "Finance",
  "sentiment": "Neutral"
}
```

This makes unstructured conversations easier to filter, prioritize, assign, and follow up.

## 🖼️ Dashboard preview

<div align="center">
  <img src="https://github.com/user-attachments/assets/ad31c6c7-1d70-4c08-a58b-3fc9ed6a16d7" alt="AI Gmail Automation Agent dashboard preview" width="95%" />
</div>

## 🛡️ Security checklist

- [ ] Keep `.env` out of version control.
- [ ] Do not commit Google OAuth credentials or tokens.
- [ ] Use the smallest practical Google API scopes.
- [ ] Rotate any credential that is accidentally exposed.
- [ ] Review AI-generated results before taking critical business actions.

## 🤝 Contributing

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Make and test your changes.
4. Commit and push your branch.
5. Open a pull request with a clear description.

## 📄 License

Add your preferred license information here.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,50:2563EB,100:0F172A&height=120&section=footer" width="100%" alt="Footer banner" />

<strong>Automate email. Surface intelligence. Move work forward.</strong>

</div>
