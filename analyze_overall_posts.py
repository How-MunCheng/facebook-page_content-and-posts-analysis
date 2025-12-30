import json
from collections import Counter

INPUT_FILE = "overall_chunks.json"
OUTPUT_FILE = "overall_analysis.json"

with open(INPUT_FILE, encoding="utf-8") as f:
    chunks = json.load(f)

if not chunks:
    raise RuntimeError("overall_chunks.json is empty")

topic_counter = Counter()
narrative_counter = Counter()
tone_counter = Counter()

for chunk in chunks:
    for t in chunk.get("dominant_topics", []):
        topic_counter[t.lower()] += 1

    for n in chunk.get("dominant_narratives", []):
        narrative_counter[n.lower()] += 1

    for tone, count in chunk.get("tone_distribution", {}).items():
        tone_counter[tone.lower()] += count

overall = {
    "dominant_topics": [t for t, _ in topic_counter.most_common(3)],
    "dominant_narratives": [n for n, _ in narrative_counter.most_common(3)],
    "overall_tone": tone_counter.most_common(1)[0][0] if tone_counter else "neutral",
    "overall_summary": (
        f"The page content is primarily focused on {', '.join([t for t, _ in topic_counter.most_common(3)])}. "
        f"Key narratives revolve around {', '.join([n for n, _ in narrative_counter.most_common(3)])}. "
        f"The overall tone of the posts is predominantly {tone_counter.most_common(1)[0][0] if tone_counter else 'neutral'}."
    )
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(overall, f, indent=2, ensure_ascii=False)

print("overall_analysis.json CREATED SUCCESSFULLY")
