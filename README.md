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

### Step 1 — Per-post LLM Analysis  

Analyze each Facebook post individually.
```bash
python analyze_per_post.py
```
Output:

per_post_analysis.csv


### Step 2 — Chunk-level Post Aggregation

Aggregate per-post results in small chunks to avoid token limits.
```bash
python overall_chunk_analysis.py
```
Output:

overall_chunks.json


### Step 3 — Overall Post Analysis

Merge chunk-level outputs into a single overall post summary.
```bash
python analyze_overall_posts.py
```
Output:

overall_analysis.json


### Step 4 — Page Identity Analysis

Analyze the Facebook Page “About” and metadata using LLM.
```bash
python python analyze_page.py
```
Output:

page_analysis.json


### Step 5 — Page vs Post Comparative Analysis

Compare declared page identity with actual posting behavior.
```bash
python comparative_analysis.py
```
Output:

comparative_analysis.json


### Step 6 — Visualization of Post Analysis

Generate posting activity and content distribution plots.
```bash
python plot.py
```

Output:

figures/weekly_posting_activity.png
