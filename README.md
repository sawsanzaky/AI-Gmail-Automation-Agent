<div align="center">

# 🤖 AI Gmail Automation Agent

<p>
  <strong>Transform unstructured Gmail messages into actionable business data with AI.</strong>
</p>

<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  </a>
  <a href="https://groq.com/">
    <img src="https://img.shields.io/badge/AI-Groq-6C47FF?style=for-the-badge" alt="Groq AI" />
  </a>
  <a href="https://developers.google.com/gmail/api">
    <img src="https://img.shields.io/badge/Gmail-API-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail API" />
  </a>
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  </a>
  <a href="https://drive.google.com/">
    <img src="https://img.shields.io/badge/Google%20Drive-Cloud-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" alt="Google Drive" />
  </a>
</p>

<p>
  <a href="#-features">Features</a> •
  <a href="#-workflow">Workflow</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-usage">Usage</a>
</p>

</div>

---

## 📌 Overview

**AI Gmail Automation Agent** is an AI-powered email automation platform built with Python, Groq, the Gmail API, Excel, Google Drive, and Streamlit.

It retrieves Gmail messages, analyzes their content with generative AI, classifies and prioritizes them, creates concise summaries and suggested actions, and organizes the results into an Excel-based business workflow synchronized with Google Drive.

<div align="center">

### Gmail → AI Agent → Analyze → Structure → Excel → Google Drive → Dashboard

</div>

## ✨ Features

<table>
  <tr>
    <td>📧 <strong>Email Retrieval</strong></td>
    <td>Connect to Gmail and process incoming messages.</td>
  </tr>
  <tr>
    <td>🤖 <strong>AI Analysis</strong></td>
    <td>Use Groq-powered generative AI to understand email content.</td>
  </tr>
  <tr>
    <td>🏷️ <strong>Classification</strong></td>
    <td>Classify messages by category, intent, and business type.</td>
  </tr>
  <tr>
    <td>🚨 <strong>Priority Detection</strong></td>
    <td>Identify urgent and high-value messages that need attention.</td>
  </tr>
  <tr>
    <td>📝 <strong>Summarization</strong></td>
    <td>Generate clear summaries and recommended next steps.</td>
  </tr>
  <tr>
    <td>📊 <strong>Excel Automation</strong></td>
    <td>Convert analyzed emails into structured business records.</td>
  </tr>
  <tr>
    <td>☁️ <strong>Google Drive Sync</strong></td>
    <td>Synchronize workflow files with Google Drive.</td>
  </tr>
  <tr>
    <td>📈 <strong>Streamlit Dashboard</strong></td>
    <td>Explore results through an interactive web dashboard.</td>
  </tr>
</table>

## 🔄 Workflow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Gmail Inbox  │ ──▶ │  AI Analysis │ ──▶ │ Classification│
└──────────────┘     └──────────────┘     └──────────────┘
                                                │
                                                ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Streamlit   │ ◀── │ Google Drive │ ◀── │ Excel Output │
│  Dashboard   │     │     Sync     │     │   & Actions  │
└──────────────┘     └──────────────┘     └──────────────┘
```

## 🎯 Business Value

Manual email processing often requires people to read every message, determine its purpose and priority, extract important information, write summaries, enter data into Excel, and track follow-up actions.

This project automates that repetitive workflow to help organizations:

- Reduce manual email processing time
- Minimize missed or incorrectly classified requests
- Create consistent business records
- Prioritize urgent communication
- Improve follow-up visibility
- Centralize email intelligence in a searchable workflow

## 🛠️ Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Core application and automation logic |
| Groq | Generative AI analysis and summarization |
| Gmail API | Email retrieval and integration |
| Excel | Structured business workflow output |
| Google Drive API | Cloud file synchronization |
| Streamlit | Interactive dashboard and user interface |

## 📁 Project Structure

```text
AI-Gmail-Automation-Agent/
├── 📄 README.md
├── 🐍 *.py                 # Application and automation modules
├── 📊 *.xlsx               # Generated Excel workflow files
├── 🔐 credentials.json     # Google OAuth credentials (do not commit)
├── 🔑 token.json           # Generated Gmail authentication token
└── ⚙️ .env                 # Local environment variables (do not commit)
```

> The exact files may vary depending on your local configuration. Never commit API keys, OAuth secrets, or generated tokens.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sawsanzaky/AI-Gmail-Automation-Agent.git
cd AI-Gmail-Automation-Agent
```

### 2. Create a virtual environment

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

## 🔐 Configuration

Create a `.env` file in the project root and add your configuration values:

```env
GROQ_API_KEY=your_groq_api_key
```

To enable Gmail and Google Drive access:

1. Create or select a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Gmail API and Google Drive API.
3. Configure the OAuth consent screen.
4. Create OAuth client credentials for a desktop application.
5. Download the credentials file and place it in the project directory using the filename expected by the application.
6. Follow the browser authentication flow when the application runs.

> Keep `.env`, OAuth credentials, and token files private. Add them to `.gitignore` before pushing the project.

## ▶️ Usage

Run the Streamlit dashboard with:

```bash
streamlit run app.py
```

If your application entry point has a different name, replace `app.py` with the appropriate Python file.

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🖼️ Dashboard Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/ad31c6c7-1d70-4c08-a58b-3fc9ed6a16d7" alt="AI Gmail Automation Agent dashboard preview" width="100%" />
</p>

## 🛡️ Security Notes

- Do not commit `.env`, `credentials.json`, `token.json`, or API keys.
- Use the minimum Google API scopes required by the application.
- Rotate exposed credentials immediately.
- Review AI-generated classifications and suggested actions before using them for critical business decisions.

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a pull request.

## 📄 License

Add your preferred license information here.

<div align="center">
  <br />
  <strong>Automate email. Organize information. Focus on what matters.</strong>
</div>
