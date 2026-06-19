"""
YouTube Transcript Fetcher for AI-Powered SEO Content Production Research

Uses the youtube-transcript-api library (free, no API key needed) to fetch
transcripts from YouTube videos featuring our selected SEO experts.

Usage:
    python scripts/fetch_transcripts.py
"""

import os
import re
import sys
from datetime import datetime

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from youtube_transcript_api import YouTubeTranscriptApi


# --- Video catalog (VERIFIED video IDs from live YouTube DOM) ---------------
# Each entry: (expert_name, video_id, video_title, approx_date)
VIDEOS = [
    # -- Nathan Gotch (from @nathangotch/videos) ----------------------------
    (
        "Nathan Gotch",
        "-Buvu-F0_ts",
        "Is SEO finally dead - New 2026 study",
        "Jun 2026",
    ),
    (
        "Nathan Gotch",
        "H_l6nQjrc0Y",
        "7-Step SEO Campaign Checklist for 2026",
        "Jun 2026",
    ),
    # -- Aleyda Solis (from @AleydaSolis/videos) ----------------------------
    (
        "Aleyda Solis",
        "dmb3dMZpa2A",
        "Learn SEO with a Roadmap featuring Free Guides and Tools in LearningSEO.io",
        "2026",
    ),
    (
        "Aleyda Solis",
        "qwj163U5IX4",
        "Join the LRT SEOKtoberfest Challenge",
        "2025",
    ),
    # -- Clearscope / Bernard Huang (from @Clearscope/videos) ----------------
    (
        "Bernard Huang",
        "c-VtgjXWsK4",
        "The Future of Search - SEO AI SEO AEO GEO with Lily Ray Kevin Indig Ross Hudgens Steve Toth",
        "Jan 2026",
    ),
    (
        "Bernard Huang",
        "ohPxcZJbQi8",
        "AI SEO After the Hype - What Actually Works in 2026",
        "Jan 2026",
    ),
    # -- Kyle Roof (from search results) ------------------------------------
    (
        "Kyle Roof",
        "669n2T30ltE",
        "Kyle Roof Best LLM for SEO 2026 - We tested GPT-5.2 Claude Sonnet 4.6 Grok 4.2 and more",
        "2026",
    ),
    (
        "Kyle Roof",
        "o4fdHvfWO60",
        "Kyle Roof Which LLM is Best for SEO",
        "2026",
    ),
    # -- Kevin Indig (from search results) ----------------------------------
    (
        "Kevin Indig",
        "qujABKOAThA",
        "SEO in the Age of AI - Kevin Indig on Google Overviews E-Commerce and The Future of Search",
        "2026",
    ),
    # -- Eli Schwartz (from search results) ---------------------------------
    (
        "Eli Schwartz",
        "x5CgYCRLgbc",
        "Product-Led SEO in AI Era with Eli Schwartz",
        "2026",
    ),
    (
        "Eli Schwartz",
        "QPm1GA_5CZA",
        "Stop Chasing AI Citations - Eli Schwartz on SEO Google AI Mode and Product-Led SEO",
        "2026",
    ),
    # -- Ross Hudgens (from search results) ---------------------------------
    (
        "Ross Hudgens",
        "MTBIMRF1DLE",
        "What Your CMO Needs to Know About AI Search",
        "2026",
    ),
    # -- Steve Toth (verified working) --------------------------------------
    # Already in Clearscope roundtable (c-VtgjXWsK4) + standalone below
    # -- Brendan Hufford (from search results) ------------------------------
    (
        "Brendan Hufford",
        "MrxJTEfL_Og",
        "SEO Mistakes to Avoid - with Brendan Hufford",
        "2026",
    ),
    # -- Lily Ray (from search results) -------------------------------------
    (
        "Lily Ray",
        "gRfP9sM_ZfA",
        "20 for 20 - Lily Ray on navigating AI search overviews and more",
        "2026",
    ),
    # -- Steve Toth (from search results) -----------------------------------
    (
        "Steve Toth",
        "ohPxcZJbQi8",
        "AI SEO After the Hype - What Actually Works in 2026",
        "Jan 2026",
    ),
]

# Deduplicate by video_id (some experts share panel videos)
seen_ids = set()
unique_videos = []
for v in VIDEOS:
    if v[1] not in seen_ids:
        seen_ids.add(v[1])
        unique_videos.append(v)
VIDEOS = unique_videos

# --- Output directory -----------------------------------------------------
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "research",
    "youtube-transcripts",
)


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:80]


def fetch_and_save_transcript(
    api: YouTubeTranscriptApi, expert: str, video_id: str, title: str, date: str
) -> bool:
    """Fetch a YouTube transcript and save it as a markdown file."""
    expert_slug = slugify(expert)
    title_slug = slugify(title)
    filename = f"{expert_slug}_{title_slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    print(f"\n{'='*60}")
    print(f"Expert:  {expert}")
    print(f"Video:   {title}")
    print(f"ID:      {video_id}")
    print(f"File:    {filename}")
    print(f"{'='*60}")

    try:
        # New API (v1.2+): use instance method .fetch()
        result = api.fetch(video_id, languages=["en"])

        # Build the markdown content
        lines = [
            f"# {title}",
            "",
            f"**Expert:** {expert}  ",
            f"**Video URL:** https://www.youtube.com/watch?v={video_id}  ",
            f"**Date:** {date}  ",
            f"**Transcript fetched:** {datetime.now().strftime('%Y-%m-%d')}  ",
            f"**Method:** youtube-transcript-api (Python, free, no API key)  ",
            "",
            "---",
            "",
            "## Transcript",
            "",
        ]

        for snippet in result:
            text = snippet.text
            start = snippet.start
            minutes = int(start // 60)
            seconds = int(start % 60)
            lines.append(f"**[{minutes:02d}:{seconds:02d}]** {text}  ")

        content = "\n".join(lines) + "\n"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        word_count = len(content.split())
        print(f"  [OK] Saved ({word_count:,} words)")
        return True

    except Exception as e:
        print(f"  [FAIL] {type(e).__name__}: {e}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("YouTube Transcript Fetcher")
    print(f"Fetching transcripts for {len(VIDEOS)} videos")
    print(f"Output directory: {OUTPUT_DIR}")
    print("=" * 60)

    api = YouTubeTranscriptApi()
    success_count = 0
    fail_count = 0
    failed_videos = []

    for expert, video_id, title, date in VIDEOS:
        if fetch_and_save_transcript(api, expert, video_id, title, date):
            success_count += 1
        else:
            fail_count += 1
            failed_videos.append((expert, video_id, title))

    print(f"\n{'='*60}")
    print(f"DONE: {success_count} succeeded, {fail_count} failed")
    if failed_videos:
        print("\nFailed videos:")
        for expert, vid, title in failed_videos:
            print(f"  - [{expert}] {title} ({vid})")
    print("=" * 60)


if __name__ == "__main__":
    main()
