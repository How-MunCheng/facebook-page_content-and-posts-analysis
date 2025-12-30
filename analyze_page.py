import json
import pandas as pd
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

df = pd.read_csv("facebook_page.csv")
page_text = "\n".join(df.astype(str).fillna("").values.flatten())

PROMPT = f"""
Analyze the following Facebook Page information.

Extract:
- declared_purpose
- declared_focus
- declared_topics (1–3)
- declared_tone
- target_audience
- page_summary (2–3 sentences)

Return STRICT JSON only.

PAGE INFO:
{page_text}
"""

resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0
)

with open("page_analysis.json", "w", encoding="utf-8") as f:
    f.write(resp.choices[0].message.content)

print("Saved page_analysis.json")
