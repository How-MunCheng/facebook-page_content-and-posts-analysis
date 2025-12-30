import os, json, pandas as pd
from groq import Groq

MODEL = "llama-3.1-8b-instant"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

page = pd.read_csv("facebook_page.csv").iloc[0].to_dict()

with open("overall_analysis.json", encoding="utf-8") as f:
    post_summary = json.load(f)

PROMPT = f"""
You are a social media analyst.

Compare:
A) Facebook Page Identity
B) Actual Posting Behavior

PAGE DETAILS:
- Page name: {page.get("pageName")}
- Category: {page.get("category")}
- Intro: {page.get("intro")}
- Followers: {page.get("followers")}
- Likes: {page.get("likes")}
- Ad active: {page.get("ad_status")}
- Business area: {page.get("business_service_area")}

POST BEHAVIOR SUMMARY:
{json.dumps(post_summary, ensure_ascii=False)}

Return STRICT JSON:
{{
  "alignment_level": "high | medium | low",
  "key_mismatches": ["mismatch1", "mismatch2"],
  "comparison_summary": "Short analytical paragraph"
}}
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": PROMPT}],
    temperature=0
)

with open("comparative_analysis.json", "w", encoding="utf-8") as f:
    f.write(response.choices[0].message.content)

print("Saved comparative_analysis.json")
