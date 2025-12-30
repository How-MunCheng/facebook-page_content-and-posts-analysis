import json
import re

def extract_json(text: str) -> dict:
    text = text.strip()
    if not text:
        raise ValueError("LLM returned EMPTY output")

    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        raise ValueError("No JSON object found in LLM output")

    return json.loads(match.group())

def save_json_safely(path: str, text: str):
    data = extract_json(text)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
