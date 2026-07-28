# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - Netlify Direct Automated Deployer (SSL & Direct Site ID Fixed)
"""
import os
import zipfile
import urllib.request
import urllib.error
import json
import ssl

NETLIFY_TOKEN = "nfp_831zneGh45wcjkTXGuUa57jvCoWF6V4Habe3"
SITE_ID = "e2fca3e7-4282-4b09-8aca-fb0741cbb6a9"  # Fixed Direct Site ID
DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")
ZIP_PATH = os.path.join(os.path.dirname(__file__), "dist.zip")

ssl_context = ssl._create_unverified_context()

def create_zip():
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(DIST_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, DIST_DIR)
                zipf.write(file_path, arcname)

def deploy_to_netlify():
    print("📦 デプロイ用パッケージを作成中...")
    create_zip()

    deploy_url = f"https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys"

    print(f"🚀 Netlifyへ完全自動デプロイを開始中... (Site ID: {SITE_ID})")
    with open(ZIP_PATH, 'rb') as f:
        zip_data = f.read()

    req = urllib.request.Request(deploy_url, data=zip_data, method='POST')
    req.add_header("Authorization", f"Bearer {NETLIFY_TOKEN}")
    req.add_header("Content-Type", "application/zip")

    try:
        with urllib.request.urlopen(req, data=zip_data, context=ssl_context) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            deployed_url = result.get('ssl_url') or result.get('url')
            print(f"🎉 [SUCCESS] 本番サイトへの完全自動デプロイが完了しました！")
            print(f"👉 本番URL: {deployed_url}")
    except urllib.error.HTTPError as e:
        print(f"❌ Deploy error: {e.code} - {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"❌ Deploy error: {e}")

if __name__ == "__main__":
    deploy_to_netlify()
