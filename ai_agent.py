import os
import json

from groq import Groq
from dotenv import load_dotenv


load_dotenv()


def analyze_email(sender, subject, body):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing in .env"
        )

    client = Groq(
        api_key=api_key
    )

    prompt = f"""
You are an AI Email Automation Agent.

Analyze the following email.

FROM:
{sender}

SUBJECT:
{subject}

EMAIL BODY:
{body}

Return ONLY valid JSON.

Use this structure:

{{
    "summary": "",
    "category": "",
    "priority": "",
    "deadline": "",
    "action_required": "",
    "department": "",
    "sentiment": ""
}}

Rules:

summary:
Give a concise business summary.

category:
Examples: Finance, HR, Sales, IT, Training, Procurement,
Customer Service, General.

priority:
Use only Low, Medium, or High.

deadline:
Extract any deadline mentioned.
If none exists, use "None".

action_required:
Describe what needs to be done.
If no action is required, use "None".

department:
Identify the most relevant department.

sentiment:
Use Positive, Neutral, or Negative.
"""

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    content = response.choices[0].message.content

    try:

        return json.loads(content)

    except json.JSONDecodeError:

        start = content.find("{")
        end = content.rfind("}") + 1

        if start >= 0 and end > start:

            return json.loads(
                content[start:end]
            )

        raise ValueError(
            "AI returned invalid JSON"
        )