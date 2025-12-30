# facebook-page_content-and-posts-analysis
This project analyzes Facebook Page identity and recent post content using LLM-based analysis.
It extracts Facebook page and per-post narratives, aggregates overall themes, and compares declared page identity with actual posting behavior.

## Data Source

- Facebook Pages Scraper (Apify Actor)
  - Facebook Pages Scraper: https://console.apify.com/actors/4Hv5RhChiaDk6iwad
  - Facebook Posts Scraper: https://console.apify.com/actors/KoJrdxJCTtpon81KY
- Input files:
  - facebook_page.csv
  - facebook_post.csv

## Analysis Pipeline (Run Order)

Step 1 — Per-post LLM Analysis  

Analyze each Facebook post individually.

```bash
python analyze_per_post.py
```

Step 2 — Chunk-level Post Aggregation

Aggregate per-post results in small chunks to avoid token limits.
```bash
python overall_chunk_analysis.py
```
