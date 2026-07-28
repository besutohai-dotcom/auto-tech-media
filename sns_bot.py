# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - Automated SNS Growth Bot
"""
import os
import random

SITE_URL = "https://superb-fox-32e811.netlify.app/"

SNS_POST_TEMPLATES = [
    "⚡️【2026年最新】「{title}」\n\nAIを駆使して完全自動化で成果を出す時代が到来しました。まだ手動で消耗していませんか？\n\n▼ 記事の全貌はこちら（完全無料）👇\n{url} \n\n#AI副業 #自動化 #時短ハック",
    "🧠 ADHD・めんどくさがり屋ほど成功する！\n「{title}」\n\n意志の力に頼らず、AIを外付け脳にして成果を10倍にする思考法をまとめました💡\n\n▼ 今すぐ読む👇\n{url} \n\n#生産性 #自己啓発 #ADHD",
    "🔥【放置型マネタイズ】自分が動かなくてもチャリンチャリンとお金が入る仕組みの作り方。\n\n「{title}」\n\n▼ 詳細ロードマップはこちら👇\n{url} \n\n#副業初心者 #不労所得 #AI活用"
]

def generate_sns_posts():
    posts = []
    titles = [
        "人間が何もしない「完全自動化AIメディア」で不労収入を得る全手順",
        "ADHD・集中力が続かない人のための「AIを外付け脳にする」最強ライフハック",
        "【放置型】月1万〜5万円を固く稼ぐデジタルストック資産の作り方",
        "2026年絶対買うべき！作業効率が3倍になる神AIデバイス＆ガジェット5選"
    ]

    for title in titles:
        template = random.choice(SNS_POST_TEMPLATES)
        post_text = template.format(title=title, url=SITE_URL)
        posts.append(post_text)

    output_path = os.path.join(os.path.dirname(__file__), "dist", "sns_posts.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n=========================================\n\n".join(posts))

    print(f"✅ [SUCCESS] 全自動SNS投稿テキストが生成されました: {output_path}")

if __name__ == "__main__":
    generate_sns_posts()
