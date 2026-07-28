# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - SNS Marketing Bot with Official Site URL
"""
import os
import json

DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")
OUTPUT_PATH = os.path.join(DIST_DIR, "sns_posts.txt")

SITE_URL = "https://auto-tech-media-official.netlify.app"

def generate_sns_posts():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR, exist_ok=True)

    from generator import TREND_TOPICS

    posts = []
    for topic in TREND_TOPICS:
        post = f"""🚀 【2026年最新AI自動化ニュース】
「{topic['title']}」

▼ 今すぐ完全無料で読む👇
{SITE_URL}/{topic['file_name']}

#AI自動化 #副業 #生産性向上 #{topic['tag'].replace('・', '')}
========================================="""
        posts.append(post)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n\n".join(posts))

    print(f"✅ [SUCCESS] 最新公式URL付きSNS投稿テキストが生成されました: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_sns_posts()
