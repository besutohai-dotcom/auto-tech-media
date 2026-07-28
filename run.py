# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - One-Click Execution & Auto Deploy
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

from generator import generate_site
from deploy import deploy_to_netlify

if __name__ == "__main__":
    print("🚀 全自動AIマネタイズシステムを起動中...")
    generate_site()
    print("🌐 インターネット本番サイトへ自動送信中...")
    deploy_to_netlify()
    print("🎉 システム実行完了！本番サイトが完全に最新状態へ全自動更新されました。")
