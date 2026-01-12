import datetime
import os
import base64

# ================= 配置区域 =================
SOURCE_FILE = "sources.txt"      # 输入：源文件
HTML_FILE = "nodes.html"         # 输出1：网页
TXT_FILE = "sub_all.txt"         # 输出2：纯订阅链接文件

# 默认源 (如果用户没有 sources.txt)
DEFAULT_SOURCES = """
V2Ray-Aggregator#https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt
Clash-Yaml-HighSpeed#https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml
Pawdroid-Base64#https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub
Free18-Daily#https://raw.githubusercontent.com/free18/v2ray/main/subscribe
"""
# ===========================================

def get_html_template(cards_html, update_time):
    """
    【赛博矩阵 V2.0】网页模板
    """
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>风の数据流 | NODE STREAM</title>
  <style>
    :root {{ --cyan: #00f2ff; --pink: #ff0055; --void: #05020a; --card-bg: rgba(16, 20, 30, 0.7); --font-code: "Consolas", monospace; }}
    * {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; outline: none; }}
    body {{ margin: 0; background: var(--void); color: #fff; font-family: sans-serif; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding-bottom: 80px; overflow-x: hidden; }}
    #matrix-canvas {{ position: fixed; inset: 0; z-index: 0; pointer-events: none; opacity: 0.3; }}
    
    .header-group {{ width: 90%; max-width: 600px; margin-top: 50px; position: relative; z-index: 2; }}
    .status-badge {{ font-family: var(--font-code); font-size: 10px; background: var(--cyan); color: #000; padding: 2px 8px; border-radius: 2px; display: inline-block; font-weight: bold; }}
    .page-title {{ font-size: 24px; margin: 10px 0; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; background: linear-gradient(90deg, #fff, #888); -webkit-background-clip: text; color: transparent; }}
    .update-time {{ font-size: 10px; color: #666; font-family: var(--font-code); margin-bottom: 30px; }}

    .card-grid {{ width: 90%; max-width: 600px; z-index: 2; display: grid; gap: 15px; }}
    .card {{ background: var(--card-bg); border: 1px solid rgba(255,255,255,0.08); padding: 15px; border-radius: 6px; backdrop-filter: blur(10px); transition: 0.3s; position: relative; overflow: hidden; }}
    .card:hover {{ transform: translateY(-2px); border-color: var(--cyan); box-shadow: 0 5px 20px rgba(0, 242, 255, 0.1); background: rgba(20, 25, 35, 0.9); }}
    .card::before {{ content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: var(--cyan); opacity: 0; transition: 0.3s; }}
    .card:hover::before {{ opacity: 1; }}

    .c-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
    .c-name {{ font-weight: bold; font-size: 14px; }}
    .c-tag {{ font-size: 9px; padding: 2px 5px; background: rgba(255,255,255,0.1); border-radius: 3px; color: #aaa; }}
    
    .link-box {{ font-family: var(--font-code); font-size: 10px; color: #666; background: #000; padding: 8px; border-radius: 4px; border: 1px dashed #333; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .card:hover .link-box {{ color: var(--cyan); border-color: rgba(0,242,255,0.3); }}
    
    .btn-row {{ margin-top: 10px; display: flex; gap: 10px; }}
    .btn {{ flex: 1; padding: 8px; font-size: 10px; text-align: center; border: 1px solid #333; color: #888; text-decoration: none; border-radius: 4px; transition: 0.2s; cursor: pointer; }}
    .btn:hover {{ border-color: var(--cyan); color: var(--cyan); background: rgba(0,242,255,0.05); }}
    .btn.clash:hover {{ border-color: var(--pink); color: var(--pink); background: rgba(255,0,85,0.05); }}

    .back-btn {{ margin-top: 40px; z-index: 5; padding: 10px 30px; border: 1px solid var(--cyan); color: var(--cyan); text-decoration: none; border-radius: 50px; font-size: 12px; transition: 0.3s; }}
    .back-btn:hover {{ background: var(--cyan); color: #000; box-shadow: 0 0 20px var(--cyan); }}

    #toast {{ position: fixed; top: 20px; left: 50%; transform: translateX(-50%) translateY(-100%); background: rgba(10,15,20,0.9); border: 1px solid var(--cyan); color: var(--cyan); padding: 10px 20px; border-radius: 4px; font-size: 12px; z-index: 999; opacity: 0; transition: 0.3s; }}
    #toast.show {{ transform: translateX(-50%) translateY(0); opacity: 1; }}
  </style>
</head>
<body>
  <canvas id="matrix-canvas"></canvas>
  <div id="toast">LINK COPIED</div>

  <div class="header-group">
    <div class="status-badge">SYSTEM ONLINE</div>
    <div class="page-title">全球节点订阅库</div>
    <div class="update-time">LAST SYNC: {update_time}</div>
  </div>

  <div class="card-grid">
    {cards_html}
  </div>

  <a href="index.html" class="back-btn">DISCONNECT // 返回</a>

  <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;
    const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const drops = [];
    const fontSize = 14;
    const columns = width / fontSize;
    for(let i=0; i<columns; i++) drops[i] = 1;

    function draw() {{
      ctx.fillStyle = 'rgba(5, 2, 10, 0.1)';
      ctx.fillRect(0, 0, width, height);
      ctx.fillStyle = '#003333';
      ctx.font = fontSize + 'px monospace';
      for(let i=0; i<drops.length; i++) {{
        const text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);
        if(drops[i]*fontSize > height && Math.random() > 0.975) drops[i] = 0;
        drops[i]++;
      }}
      requestAnimationFrame(draw);
    }}
    draw(); window.addEventListener('resize', ()=>{{ width=canvas.width=window.innerWidth; height=canvas.height=window.innerHeight; }});

    async function copyText(text) {{
      const t = document.getElementById('toast');
      try {{
        await navigator.clipboard.writeText(text);
        t.innerText = "COPIED SUCCESSFUL";
      }} catch (err) {{
        const ta = document.createElement("textarea");
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        t.innerText = "COPIED (FALLBACK)";
      }}
      t.classList.add('show');
      setTimeout(()=>t.classList.remove('show'), 2000);
    }}
  </script>
</body>
</html>
"""

def init_sources_if_missing():
    """初始化源文件"""
    if not os.path.exists(SOURCE_FILE):
        print(f"⚠️ {SOURCE_FILE} 不存在，生成默认源...")
        with open(SOURCE_FILE, "w", encoding="utf-8") as f:
            f.write(DEFAULT_SOURCES.strip())

def process_data():
    """核心处理逻辑"""
    cards_html = ""
    all_urls = []
    
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"): continue
                
            try:
                # 解析 Name#URL 或 Name,URL
                if "#" in line: parts = line.split("#", 1)
                elif "," in line: parts = line.split(",", 1)
                else: continue

                name = parts[0].strip()
                url = parts[1].strip()
                all_urls.append(url) # 收集所有链接

                # 生成HTML卡片
                cards_html += f"""
    <div class="card">
      <div class="c-top">
        <span class="c-name">{name}</span>
        <span class="c-tag">ACTIVE</span>
      </div>
      <div class="link-box" onclick="copyText('{url}')">{url}</div>
      <div class="btn-row">
        <div class="btn" onclick="copyText('{url}')">复制链接</div>
        <a class="btn clash" href="clash://install-config?url={url}">导入 Clash</a>
      </div>
    </div>
"""
            except Exception as e:
                print(f"❌ 行 {line_num} 错误: {e}")

    return cards_html, all_urls

def main():
    init_sources_if_missing()
    
    print("🔄 正在提取订阅源...")
    cards_html, all_urls = process_data()
    
    # 1. 生成网页
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    final_html = get_html_template(cards_html, now)
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"✅ 网页已生成: {HTML_FILE}")

    # 2. 生成 sub_all.txt (聚合文件)
    # 这里我们将所有链接按行写入，用户可以直接复制这个文件的 Raw 链接作为订阅
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_urls))
    print(f"✅ 聚合文件已生成: {TXT_FILE}")
    print(f"📅 完成时间: {now}")

if __name__ == "__main__":
    main()