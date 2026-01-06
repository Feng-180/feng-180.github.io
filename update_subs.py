import datetime

def generate_page():
    # 你的粉色/暗黑系 UI 模板
    html_template_top = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TERMINAL_EXIT // 存档</title>
        <style>
            :root { --p-pink: #ff79c6; --bg: #0b0b0e; --card: #16161e; --text: #a0a0b0; --cyan: #8be9fd; --orange: #ffb86c; }
            body { background: var(--bg); color: var(--text); font-family: 'Courier New', monospace; padding: 20px; display: flex; flex-direction: column; align-items: center; }
            .container { width: 100%; max-width: 450px; border: 1px solid #1a1a20; padding: 25px; border-radius: 12px; background: #0f0f13; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            .header-title { text-align: center; color: #fff; font-size: 1.5rem; letter-spacing: 4px; margin-bottom: 20px; }
            .node-box { border: 1px solid #222; padding: 15px; margin-bottom: 20px; border-radius: 5px; background: #121217; }
            .node-line { display: flex; justify-content: space-between; font-size: 12px; margin: 8px 0; border-bottom: 1px solid #1a1a20; padding-bottom: 4px; }
            .status { color: #50fa7b; font-weight: bold; }
            .btn { display: block; width: 100%; padding: 14px 0; margin: 12px 0; text-align: center; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 14px; transition: 0.3s; color: #fff; border: 1px solid rgba(255,255,255,0.1); }
            .btn-copy { border-left: 4px solid var(--p-pink); background: linear-gradient(90deg, #1e1e26, #0f0f13); }
            .btn-clash { border-left: 4px solid var(--orange); background: linear-gradient(90deg, #1e1e26, #0f0f13); }
            .btn:hover { filter: brightness(1.3); transform: scale(1.02); }
            .footer { text-align: center; font-size: 10px; color: #444; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div style="font-size: 10px; color: #444; text-align: center; margin-bottom: 10px;">TERMINAL_EXIT // 返回</div>
            <div class="header-title">同步魔法术式</div>
            <div class="node-box">
                <div style="color: #444; font-size: 10px; margin-bottom: 15px;">GLOBAL_NODE_ARCHIVE</div>
    """

    html_template_bottom = """
            </div>
            <p style="text-align: center; font-size: 12px; color: #6272a4;">点击下方按钮操作最新选定的源</p>
        </div>
        <div class="footer">LAST_SYNC_TIME: {time}</div>
        <script>
            function copyUrl(url) {
                navigator.clipboard.writeText(url);
                alert('🌸 术式链接已复制到剪贴板');
            }
        </script>
    </body>
    </html>
    """

    node_items = ""
    with open("sources.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "#" in line:
                name, url = line.strip().split("#")
                node_items += f"""
                <div class="node-line">
                    <span style="color:var(--text)">[{name}]</span>
                    <span class="status" onclick="copyUrl('{url}')" style="cursor:pointer">ONLINE 📋</span>
                </div>
                <a href="clash://install-config?url={url}" class="btn btn-clash">一键导入 {name} 到 Clash</a>
                """

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    full_html = html_template_top + node_items + html_template_bottom.replace("{time}", now)

    with open("nodes.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("💖 存档页面生成成功！")

if __name__ == "__main__":
    generate_page()