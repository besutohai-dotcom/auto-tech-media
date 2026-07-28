# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - Netlify Direct Automated Deployer (SSL Fixed)
"""
import os
import zipfile
import urllib.request
import urllib.error
import json
import ssl

NETLIFY_TOKEN = "nfp_831zneGh45wcjkTXGuUa57jvCoWF6V4Habe3"
SITE_NAME = "auto-tech-media-official.netlify.app"
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

def get_site_id():
    url = "https://api.netlify.com/api/v1/sites"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {NETLIFY_TOKEN}")
    try:
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for site in data:
                if site.get('name') == "auto-tech-media-official" or site.get('url') == f"https://{SITE_NAME}":
                    return site['id']
            if data:
                return data[0]['id']
    except Exception as e:
        print(f"Site lookup info: {e}")
    return None

def deploy_to_netlify():
    print("📦 デプロイ用パッケージを作成中...")
    create_zip()

    print("🔍 Netlify サイト情報を取得中...")
    site_id = get_site_id()

    deploy_url = f"https://api.netlify.com/api/v1/sites/{site_id}/deploys" if site_id else "https://api.netlify.com/api/v1/deploys"

    print(f"🚀 Netlifyへ完全自動デプロイを開始中... (Site ID: {site_id})")
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
