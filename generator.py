# -*- coding: utf-8 -*-
"""
Auto Blogger Engine - Ultimate Hands-On Code & Prompt Included Edition
"""
import os
import datetime

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "article_template.html")
DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")

TREND_TOPICS = [
    {
        "id": "art-1",
        "file_name": "art-1.html",
        "tag": "AI・自動化",
        "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80",
        "title": "【2026年最新】人間が何もしない「完全自動化AIメディア」で不労収入を得る全手順",
        "summary": "AIが自動でトレンドニュースを収集し、記事を執筆して広告収益を生むシステムが話題に。設定方法とマネタイズの仕組みを徹底解説。",
        "toc": [
            "1. はじめに：なぜ概念論ではなく「動くコード」が必要なのか？",
            "2. 労働型副業 vs AI自動メディアの比較",
            "3. 【実践コード】Netlify APIで自動デプロイするPythonスクリプト",
            "4. 【コピペ用】高品質SEO記事を自動生成するAIプロンプト例",
            "5. 放置型マネタイズを成立させる3つの収益柱",
            "6. よくある質問 (FAQ)",
            "7. まとめ：今日から始める次世代の不労型ビジネス"
        ],
        "content": """
<h2>1. はじめに：なぜ概念論ではなく「動くコード」が必要なのか？</h2>
<p>2026年現在、多くの副業解説記事は「AIを使えば自動化できます」という概要だけを語り、<b>具体的なプログラムコードや設定手順を隠しています。</b></p>
<p>本記事では、机上の空論を排除し、あなたが今すぐコピペして動かせる<b>「全自動デプロイのPythonソースコード」</b>と<b>「AI執筆プロンプト」</b>を完全公開します。これらを組み合わせることで、完全手作業ゼロの自動メディアが完成します。</p>

<h2>2. 労働型副業 vs AI自動メディアの比較</h2>
<table class="pro-table">
  <thead>
    <tr>
      <th>項目</th>
      <th>従来の手動副業</th>
      <th>全自動AIメディア</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>労働時間</b></td>
      <td>毎日 2〜4時間（労働必須）</td>
      <td><b>0時間（完全自動更新）</b></td>
    </tr>
    <tr>
      <td><b>月間コンテンツ量</b></td>
      <td>10〜30本が限界</td>
      <td><b>100〜300本以上</b></td>
    </tr>
    <tr>
      <td><b>収益の持続性</b></td>
      <td>手を止めたらゼロ</td>
      <td><b>24時間365日ストック収益</b></td>
    </tr>
    <tr>
      <td><b>初期コスト</b></td>
      <td>0円〜数万円</td>
      <td><b>0円〜月数百円</b></td>
    </tr>
  </tbody>
</table>

<h2>3. 【実践コード】Netlify APIで自動デプロイするPythonスクリプト</h2>
<p>以下は、ローカルで生成したHTMLファイルをZIP圧縮し、NetlifyのAPIを叩いて一瞬で本番サイトへ上書き更新する実際のPythonコードです。</p>

<div class="code-block-header">📄 deploy_automation.py （コピペして使用可能）</div>
<pre><code>import os
import zipfile
import urllib.request
import json
import ssl

NETLIFY_TOKEN = "nfp_YOUR_PERSONAL_ACCESS_TOKEN"
SITE_ID = "YOUR_NETLIFY_SITE_ID"
DIST_DIR = "./dist"
ZIP_PATH = "./dist.zip"

def deploy():
    # 1. 成果物ディレクトリをZIP圧縮
    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(DIST_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, DIST_DIR))

    # 2. Netlify Direct Deploy APIへ送信
    url = f"https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys"
    with open(ZIP_PATH, 'rb') as f:
        zip_data = f.read()

    req = urllib.request.Request(url, data=zip_data, method='POST')
    req.add_header("Authorization", f"Bearer {NETLIFY_TOKEN}")
    req.add_header("Content-Type", "application/zip")

    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"🎉 デプロイ成功！本番URL: {res.get('ssl_url')}")

if __name__ == "__main__":
    deploy()
</code></pre>

<h2>4. 【コピペ用】高品質SEO記事を自動生成するAIプロンプト例</h2>
<p>AI（ChatGPTやClaude）に薄い文章を書かせないための、実践的な指示文（プロンプト）のテンプレートです。</p>

<div class="code-block-header">📝 AI執筆用システムプロンプト指示文</div>
<pre><code>【役割】
あなたは月間100万PVのWebメディアを運営するプロのSEOライターです。

【指示】
以下の[キーワード]に基づいて、読者の悩みを解決する3,000文字以上の深掘り記事を作成してください。

【必須構成要素】
1. H2見出しを4つ〜5つ作成し、目次と100%一致させること。
2. 抽象的な説明を避け、「ステップ1」「ステップ2」などの具体的な手順を入れること。
3. 従来手法と最新手法の比較表（HTML tableタグ）を必ず1つ挿入すること。
4. 記事の末尾に、よくある質問（FAQ）を2つ入れること。

[キーワード]: 2026年 AI 自動化 副業
</code></pre>

<div class="cta-box">
  <h3>🚀 手作業ゼロで自動収益化を始めたい方へ</h3>
  <p>最新のAI自動化テンプレートと構築手順ガイドを無料で公開中！</p>
  <a href="art-3.html" class="cta-button">👉 自動ストック資産の構築ガイドを見る</a>
</div>

<h2>5. 放置型マネタイズを成立させる3つの収益柱</h2>
<p><b>1. Google AdSense：</b> 記事内の自動広告を閲覧・クリックされるだけで収益発生。</p>
<p><b>2. Amazon / 楽天アフィリエイト：</b> 紹介ガジェットの購入経由で3%〜10%の報酬。</p>
<p><b>3. 高単価ASPアフィリエイト：</b> 無料体験登録1件あたり1,000円〜10,000円の高額報酬。</p>

<h2>6. よくある質問 (FAQ)</h2>
<div class="faq-list">
  <div class="faq-item">
    <div class="faq-q">Q. プログラミング初心者でも構築できますか？</div>
    <div class="faq-a">A. はい。上記で公開しているPythonコードとプロンプトをコピーしてそのまま使うだけで即座に自動化が可能です。</div>
  </div>
  <div class="faq-item">
    <div class="faq-q">Q. サーバー代などの維持費はいくらかかりますか？</div>
    <div class="faq-a">A. Netlify等の静的ホスティングを活用すれば、月間の維持費は完全無料（0円）で運用可能です。</div>
  </div>
</div>

<h2>7. まとめ：今日から始める次世代の不労型ビジネス</h2>
<p>概念論に時間を費やすのは終わりです。上記で提供したスクリプトとプロンプトを活用し、今日からあなたの「全自動ストック資産」を稼働させましょう。</p>
"""
    },
    {
        "id": "art-2",
        "file_name": "art-2.html",
        "tag": "ADHD・時短ハック",
        "img": "https://images.unsplash.com/photo-1507413245164-6160d8298b31?auto=format&fit=crop&w=800&q=80",
        "title": "ADHD・集中力が続かない人のための「AIを外付け脳にする」最強ライフハック",
        "summary": "集中力が続かない・タスク管理が苦手な人ほどAIとの相性は抜群。行動ハードルを極限まで下げる5秒ルールの活用法。",
        "toc": [
            "1. なぜADHD気質・集中力に悩む人ほどAIとの相性が抜群なのか？",
            "2. 行動ハードルをゼロにする「5秒ルール」と「微小タスク分解」",
            "3. ADHD脳を覚醒させるツール＆AI活用マトリックス",
            "4. 脳内ドーパミンを味方につける「即時フィードバック」の仕組み化",
            "5. よくある質問 (FAQ)",
            "6. まとめ：根性に頼らず「環境とAI」で成果を出すロードマップ"
        ],
        "content": """
<h2>1. なぜADHD気質・集中力に悩む人ほどAIとの相性が抜群なのか？</h2>
<p>「やるべきことがあるのに手につかない」「気が散って別のことを始めてしまう」——こうした悩みを持つ人にとって、AIは単なるツールではありません。脳のワーキングメモリを補う<b>「最強の外付け前頭葉（脳）」</b>となります。</p>

<h2>2. 行動ハードルをゼロにする「5秒ルール」と「微小タスク分解」</h2>
<p>ADHD脳が行動を起こせない最大の理由は「タスクが大きすぎて脳が負担を感じているから」です。AIに「資料作成を5秒でできる極小タスクに分解して」と頼むことで、<b>「ファイルを開く」「タイトルを1行書く」</b>といった超低ハードルな行動にまで分解できます。</p>

<h2>3. ADHD脳を覚醒させるツール＆AI活用マトリックス</h2>
<table class="pro-table">
  <thead>
    <tr>
      <th>悩み・ボトルネック</th>
      <th>従来のアプローチ（失敗）</th>
      <th>AI外付け脳ソリューション</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>作業に取りかかれない</b></td>
      <td>気合・根性で頑張る</td>
      <td><b>AIに「5秒タスク」に分解してもらう</b></td>
    </tr>
    <tr>
      <td><b>途中で気が散る</b></td>
      <td>スマホを隠す</td>
      <td><b>AIとペアワーク（10分ごとに進捗報告）</b></td>
    </tr>
    <tr>
      <td><b>優先順位がわからない</b></td>
      <td>ToDoリストを手書き</td>
      <td><b>AIに箇条書きを入力し「順序決め」を命令</b></td>
    </tr>
  </tbody>
</table>

<div class="cta-box">
  <h3>⚡️ デスク環境から集中力を高めたい方へ</h3>
  <p>作業効率が3倍になる最新のAIデバイス＆時短ガジェットを厳選紹介！</p>
  <a href="art-4.html" class="cta-button">👉 おすすめ神AIガジェット5選を見る</a>
</div>

<h2>4. 脳内ドーパミンを味方につける「即時フィードバック」の仕組み化</h2>
<p>ADHD傾向のある脳は「遠い将来のご褒美」では動けません。タスク完了時の音やアニメーション演出、レベルアップ表示などのゲーミフィケーションを取り入れることで、即時ドーパミンを放出させます。</p>

<h2>5. よくある質問 (FAQ)</h2>
<div class="faq-list">
  <div class="faq-item">
    <div class="faq-q">Q. AIへのプロンプト（命令文）を考えるのが面倒です。</div>
    <div class="faq-a">A. 「今から何をすればいい？」とひとこと送るだけでOKです。複雑なプロンプトは一切不要です。</div>
  </div>
</div>

<h2>6. まとめ：根性に頼らず「環境とAI」で成果を出すロードマップ</h2>
<p>自分の集中力や意志の弱さを根性で治そうとするのはやめましょう。弱みは優秀なテクノロジーに任せ、自分は最も得意なクリエイティブに専念するのが最高戦略です。</p>
"""
    },
    {
        "id": "art-3",
        "file_name": "art-3.html",
        "tag": "副業・マネタイズ",
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        "title": "【放置型】月1万〜5万円を固く稼ぐデジタルストック資産の作り方",
        "summary": "労働型副業を卒業し、一度作ったら完全放置でチャリンチャリンとお金が入る仕組みづくりの現実的なルート。",
        "toc": [
            "1. フロー収入（労働）vs ストック収入（資産）の違い",
            "2. 放置で月1万〜5万円を生むデジタル資産の比較モデル",
            "3. 完全自動化ストック資産を構築する3ステップ",
            "4. よくある質問 (FAQ)",
            "5. まとめ：労働から脱却するためのロードマップ"
        ],
        "content": """
<h2>1. フロー収入（労働）vs ストック収入（資産）の違い</h2>
<p>多くの副業初心者が陥る罠が「ライティング受託」などの<b>フロー型労働</b>です。作業した瞬間はお金になりますが、手を止めた瞬間に収入はゼロになります。</p>
<p>一方で本記事で解説する<b>「デジタルストック資産」</b>とは、一度構築すれば24時間365日放置で収益を発生させ続ける仕組みのことです。</p>

<h2>2. 放置で月1万〜5万円を生むデジタル資産の比較モデル</h2>
<table class="pro-table">
  <thead>
    <tr>
      <th>資産タイプ</th>
      <th>難易度</th>
      <th>放置度</th>
      <th>想定月収</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>① AI自動更新メディア</b></td>
      <td>★☆☆（自動化可能）</td>
      <td><b>★★★★★（完全放置）</b></td>
      <td><b>月1万〜10万円</b></td>
    </tr>
    <tr>
      <td><b>② 放置型Webツール</b></td>
      <td>★★☆</td>
      <td>★★★★☆</td>
      <td>月3万〜20万円</td>
    </tr>
    <tr>
      <td><b>③ テンプレート販売</b></td>
      <td>★★☆</td>
      <td>★★★☆☆</td>
      <td>月1万〜5万円</td>
    </tr>
  </tbody>
</table>

<div class="cta-box">
  <h3>💰 今すぐ完全自動化メディアを立ち上げたい方へ</h3>
  <p>AIテクノロジーを活用した全自動Webメディアの全手順をチェック！</p>
  <a href="art-1.html" class="cta-button">👉 完全自動化メディアの全手順を見る</a>
</div>

<h2>3. 完全自動化ストック資産を構築する3ステップ</h2>
<p><b>【ステップ1：ターゲットと広告モデルの選定】</b> Google AdSense等の自動収益モデルを選択。</p>
<p><b>【ステップ2：AIプログラムによるシステム構築】</b> コンテンツ生成からデプロイまでをプログラム化。</p>
<p><b>【ステップ3：全自動同期と放置運用】</b> API連携で人が介在しなくても勝手に更新・集客される構造を完成。</p>

<h2>4. よくある質問 (FAQ)</h2>
<div class="faq-list">
  <div class="faq-item">
    <div class="faq-q">Q. 収益が発生するまでどれくらいの期間がかかりますか？</div>
    <div class="faq-a">A. Google検索にインデックス・評価されるまで通常1〜2ヶ月程度の成熟期間が必要です。</div>
  </div>
</div>

<h2>5. まとめ：労働から脱却するためのロードマップ</h2>
<p>自分の時間を売るのをやめ、テクノロジーに働かせる思考へ切り替えましょう。今日構築した仕組みが、数ヶ月後のあなたに持続的な不労所得をもたらします。</p>
"""
    },
    {
        "id": "art-4",
        "file_name": "art-4.html",
        "tag": "最新ガジェット",
        "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
        "title": "2026年絶対買うべき！作業効率が3倍になる神AIデバイス＆ガジェット5選",
        "summary": "デスク環境をスマート化し、無駄な作業時間を一瞬でゼロにする最新のAIウェアラブル＆時短ガジェット特集。",
        "toc": [
            "1. デスク環境のスマート化が「人生の時間」を買い戻す理由",
            "2. 2026年絶対買うべき！神AIデバイス5選スペック比較",
            "3. よくある質問 (FAQ)",
            "4. まとめ：ガジェット投資で毎日1時間の自由を手に入れよう"
        ],
        "content": """
<h2>1. デスク環境のスマート化が「人生の時間」を買い戻す理由</h2>
<p>私たちは毎日、「手動での文字起こし」「ファイルの探索」などの無駄な動作に平均2時間以上を奪われています。2026年最新のAIガジェットを導入することは、<b>「自分の人生時間を直接買い戻す投資」</b>です。</p>

<h2>2. 2026年絶対買うべき！神AIデバイス5選スペック比較</h2>
<table class="pro-table">
  <thead>
    <tr>
      <th>デバイス名</th>
      <th>主なAI機能</th>
      <th>時間削減効果</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>① AI文字起こしボイスレコーダー</b></td>
      <td>リアルタイム要約・マインドマップ化</td>
      <td><b>1日 45分節約</b></td>
    </tr>
    <tr>
      <td><b>② 脳波測定AIヘッドセット</b></td>
      <td>集中度測定＆BGM自動生成</td>
      <td><b>1日 30分節約</b></td>
    </tr>
    <tr>
      <td><b>③ AIショートカットキーパッド</b></td>
      <td>ワンタップでプロンプト呼び出し</td>
      <td><b>1日 20分節約</b></td>
    </tr>
    <tr>
      <td><b>④ スマートドッキングステーション</b></td>
      <td>画面共有・データ転送AI最適化</td>
      <td><b>1日 15分節約</b></td>
    </tr>
    <tr>
      <td><b>⑤ AIスマートデスクライト</b></td>
      <td>姿勢・疲れ目検知と自動調光</td>
      <td><b>疲労度 50%軽減</b></td>
    </tr>
  </tbody>
</table>

<div class="cta-box">
  <h3>🧠 ADHD・集中力不足で悩んでいる方へ</h3>
  <p>AIを外付けの脳にして行動ハードルをゼロにする最強のライフハックはこちら！</p>
  <a href="art-2.html" class="cta-button">👉 AIを外付け脳にするライフハックを見る</a>
</div>

<h2>3. よくある質問 (FAQ)</h2>
<div class="faq-list">
  <div class="faq-item">
    <div class="faq-q">Q. ガジェットを購入する優先順位はどう決めればいいですか？</div>
    <div class="faq-a">A. 自分が一番ストレスを感じている作業（例: 会議の議事録なら①のボイスレコーダー）から導入するのが最も投資効果が高いです。</div>
  </div>
</div>

<h2>4. まとめ：ガジェット投資で毎日1時間の自由を手に入れよう</h2>
<p>環境を整えることは、自分の可能性を最大化する最も手軽なアプローチです。最新のAIガジェットを取り入れて、無駄なストレスのないスマートなライフスタイルを始めましょう。</p>
"""
    }
]

def generate_site():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR, exist_ok=True)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    now_str = datetime.datetime.now().strftime("%Y-%m-%d")

    article_cards_html = ""
    for topic in TREND_TOPICS:
        article_cards_html += f"""
        <a href="{topic['file_name']}" class="recent-card" data-category="{topic['tag']}">
          <div class="recent-img-wrapper">
            <img src="{topic['img']}" alt="">
          </div>
          <div class="recent-content">
            <span class="badge-cat" style="font-size:0.7rem; padding:2px 8px; margin-bottom:0.4rem; display:inline-block;">{topic['tag']}</span>
            <h3>{topic['title']}</h3>
            <p>{topic['summary']}</p>
          </div>
        </a>
        """

    def render_toc_html(toc_list):
        items = "".join([f"<li>{item}</li>" for item in toc_list])
        return items

    # Generate index.html (Main Page)
    main_topic = TREND_TOPICS[0]

    index_html = template.replace("{{MAIN_TITLE}}", main_topic["title"])
    index_html = index_html.replace("{{MAIN_TAG}}", main_topic["tag"])
    index_html = index_html.replace("{{MAIN_DATE}}", now_str)
    index_html = index_html.replace("{{MAIN_HERO_IMG}}", main_topic["img"])
    index_html = index_html.replace("{{MAIN_TOC_ITEMS}}", render_toc_html(main_topic["toc"]))
    index_html = index_html.replace("{{MAIN_CONTENT}}", main_topic["content"])
    index_html = index_html.replace("{{ARTICLE_CARDS}}", article_cards_html)
    
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # Generate Individual Standalone Article Pages
    for topic in TREND_TOPICS:
        art_html = template.replace("{{MAIN_TITLE}}", topic["title"])
        art_html = art_html.replace("{{MAIN_TAG}}", topic["tag"])
        art_html = art_html.replace("{{MAIN_DATE}}", now_str)
        art_html = art_html.replace("{{MAIN_HERO_IMG}}", topic["img"])
        art_html = art_html.replace("{{MAIN_TOC_ITEMS}}", render_toc_html(topic["toc"]))
        art_html = art_html.replace("{{MAIN_CONTENT}}", topic["content"])
        art_html = art_html.replace("{{ARTICLE_CARDS}}", article_cards_html)
        
        page_path = os.path.join(DIST_DIR, topic["file_name"])
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(art_html)

    print(f"✅ [HANDS-ON CODE & PROMPT GENERATED] 実用コード・AIプロンプト完全収録の記事群を生成しました。")

if __name__ == "__main__":
    generate_site()
