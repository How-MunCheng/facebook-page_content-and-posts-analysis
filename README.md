# facebook-page_content-and-posts-analysis
Scraping and LLM-based analysis of Facebook Page content and posts.


- Public Facebook pages and posts were collected using Apify’s Facebook Pages Scraper actor.
- Scraping configurations and pipeline logic are included in this repository.

*Raw scraped data is excluded to comply with data governance and platform policies.


Pipeline Overview:

Apify Facebook Scraper

-Facebook Pages Scraper: https://console.apify.com/actors/4Hv5RhChiaDk6iwad

-Facebook Posts Scraper: https://console.apify.com/actors/KoJrdxJCTtpon81KY

        ↓

raw CSV (facebook_page.csv, facebook_post.csv)

        ↓

per-post LLM analysis

        ↓

per_post_analysis.csv

        ↓

chunked overall post analysis (LLM-safe)
        
        ↓

overall_chunks.json

        ↓

overall_analysis.json

        ↓

Page LLM analysis

        ↓

page_analysis.json

        ↓

Comparative LLM analysis

        ↓

comparative_analysis.json

        ↓

Visualization
