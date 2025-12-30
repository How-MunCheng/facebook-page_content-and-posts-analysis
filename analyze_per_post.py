import os
import json
import pandas as pd
from groq import Groq

INPUT_CSV = "facebook_post.csv"
OUTPUT_CSV = "per_post_analysis.csv"

MODEL = "llama-3.1-8b-instant"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PROMPT_TEMPLATE = """
You are a professional social media content analyst.

Analyze the Facebook post below.

POST METADATA:
- Likes: {likes}
- Total Reactions: {reactions}
- Shares: {shares}
- Comments: {comments}
- Posted time: {time}

POST TEXT:
{text}

Return STRICT JSON ONLY:
{{
  "post_id": "{post_id}",
  "main_topics": ["topic1", "topic2"],
  "narrative": "short phrase",
  "tone": "positive | neutral | negative | alarmist",
  "engagement_signal": "low | medium | high",
  "brief_summary": "1–2 sentences"
}}
"""

df = pd.read_csv(INPUT_CSV)

print("Loaded posts:", len(df))
print("Available columns:\n", df.columns.tolist())

results = []
processed = 0
skipped = 0

for idx, row in df.iterrows():
    text = str(row["Texttext"]) if pd.notna(row["Texttext"]) else ""

    if len(text.strip()) < 30:
        skipped += 1
        continue

    prompt = PROMPT_TEMPLATE.format(
        post_id=row["Post IDpostId"],
        likes=row["Likeslikes"],
        reactions=row["Top Reactions CounttopReactionsCount"],
        shares=row["Sharesshares"],
        comments=row["Commentscomments"],
        time=row["Timetime"],
        text=text[:3000]  # SAFE token limit
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content
        data = json.loads(content)

        results.append(data)
        processed += 1
        print(f"✔ Analyzed post {processed}: {data['post_id']}")

    except Exception as e:
        print("✘ Failed post:", row["Post IDpostId"], e)
        skipped += 1

print("\nSUMMARY")
print("Processed:", processed)
print("Skipped:", skipped)

pd.DataFrame(results).to_csv(
    OUTPUT_CSV,
    index=False,
    encoding="utf-8-sig"
)

print("Saved:", OUTPUT_CSV)
