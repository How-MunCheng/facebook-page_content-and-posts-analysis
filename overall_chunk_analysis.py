import os, json, pandas as pd
from groq import Groq

INPUT_CSV = "per_post_analysis.csv"
OUTPUT_JSON = "overall_chunks.json"
MODEL = "llama-3.1-8b-instant"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

df = pd.read_csv(INPUT_CSV)

records = []
for _, r in df.iterrows():
    records.append({
        "topics": r["main_topics"],
        "narrative": r["narrative"],
        "tone": r["tone"]
    })

CHUNK_SIZE = 15   # VERY SAFE
results = []

for i in range(0, len(records), CHUNK_SIZE):
    batch = records[i:i+CHUNK_SIZE]

    prompt = f"""
You analyze Facebook post summaries.

Return STRICT JSON ONLY:
{{
  "dominant_topics": [],
  "dominant_narratives": [],
  "tone_distribution": {{}}
}}

POST DATA:
{json.dumps(batch, ensure_ascii=False)}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    print(f"\n--- RAW RESPONSE CHUNK {i+1} ---")
    print(text if text else "[EMPTY RESPONSE]")

    # HARD SAFETY
    if not text or not text.startswith("{"):
        print("Skipped empty or invalid chunk")
        continue

    try:
        results.append(json.loads(text))
        print("Chunk saved")
    except json.JSONDecodeError:
        print("JSON parse failed — skipped")

# ALWAYS WRITE FILE (even partial)
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n Saved {len(results)} chunk analyses to {OUTPUT_JSON}")
