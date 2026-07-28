# -*- coding: utf-8 -*-
"""
Update Netlify Site Subdomain Name
"""
import urllib.request
import urllib.error
import json
import ssl

NETLIFY_TOKEN = "nfp_831zneGh45wcjkTXGuUa57jvCoWF6V4Habe3"
SITE_ID = "e2fca3e7-4282-4b09-8aca-fb0741cbb6a9"
NEW_NAME = "auto-tech-media-official"  # Cool clean URL

ssl_context = ssl._create_unverified_context()

def update_site_name():
    url = f"https://api.netlify.com/api/v1/sites/{SITE_ID}"
    data = json.dumps({"name": NEW_NAME}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='PATCH')
    req.add_header("Authorization", f"Bearer {NETLIFY_TOKEN}")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            new_url = res.get('ssl_url') or res.get('url')
            print(f"🎉 [SUCCESS] URLの変更が完了しました！")
            print(f"👉 新しいURL: {new_url}")
            return new_url
    except urllib.error.HTTPError as e:
        print(f"❌ Error: {e.code} - {e.read().decode('utf-8')}")
        # Try alternate name if taken
        alt_name = "auto-tech-media-japan"
        data = json.dumps({"name": alt_name}).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='PATCH')
        req.add_header("Authorization", f"Bearer {NETLIFY_TOKEN}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, context=ssl_context) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"👉 新しいURL: {res.get('ssl_url')}")

if __name__ == "__main__":
    update_site_name()
