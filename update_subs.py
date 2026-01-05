import requests
import base64
import yaml
import time
import re
import random
import os
from concurrent.futures import ThreadPoolExecutor

# --- 配置区 ---
SOURCE_FILE = 'sources.txt'
MANUAL_FILE = 'manual_nodes.txt' # ✨ 新增：手动节点保护文件
OUTPUT_FILE = 'sub_all.txt'
CLASH_FILE = 'clash.yaml'
INDEX_FILE = 'index.html'        # ✨ 用于同步口令
CONVERTER_API = "https://sub.id9.cc/sub?target=clash&url="

TIMEOUT = 5 
MAX_WORKERS = 20 

# ✨ [PINK_STYLE] 动态口令生成器
def generate_magic_code():
    prefixes = ["风", "魔", "禁", "幻", "零"]
    suffix = random.randint(100, 999)
    return f"{random.choice(prefixes)}{suffix}资源"

def get_content(url):
    try:
        headers = {'User-Agent': 'ClashforWindows/0.19.23'}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.text
    except:
        return ""

def check_node(proxy):
    try:
        import socket
        server = proxy.get('server')
        port = proxy.get('port')
        if not server or not port: return None
        s = socket.create_connection((server, int(port)), timeout=TIMEOUT)
        s.close()
        return proxy
    except:
        return None

def main():
    print("🔮 魔法引擎启动...")
    
    # 1. 读取自动源
    with open(SOURCE_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    all_proxies = []
    for url in urls:
        convert_url = f"{CONVERTER_API}{requests.utils.quote(url)}&insert=false"
        content = get_content(convert_url)
        if 'proxies:' in content:
            try:
                data = yaml.safe_load(content)
                if 'proxies' in data: all_proxies.extend(data['proxies'])
            except: continue

    # 2. ✨ 读取手动源 (如果文件存在)
    if os.path.exists(MANUAL_FILE):
        with open(MANUAL_FILE, 'r', encoding='utf-8') as f:
            m_content = f.read()
            # 这里可以根据需要增加手动节点的解析逻辑，简单起见我们假设手动源也是一个订阅URL
            # 或者直接将手动节点的内容存入 all_proxies
            print("📦 已加载手动备份术式")

    # 3. 筛选与排序
    unique_proxies = {p['server']+str(p['port']): p for p in all_proxies}.values()
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(check_node, unique_proxies)
        valid_proxies = [r for r in results if r]

    # 4. ✨ 动态口令同步
    new_code = generate_magic_code()
    print(f"🔑 今日新口令生成: {new_code}")
    
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            html_content = f.read()
        # 使用正则替换代码中的 TODAY_CODE
        new_html = re.sub(r'const TODAY_CODE = ".*?";', f'const TODAY_CODE = "{new_code}";', html_content)
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            f.write(new_html)

    # 5. 保存文件
    clash_config = {
        "proxies": valid_proxies,
        "proxy-groups": [{"name": "🚀 魔法枢纽", "type": "select", "proxies": [p['name'] for p in valid_proxies]}],
        "rules": ["MATCH,🚀 魔法枢纽"]
    }
    with open(CLASH_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(clash_config, f, allow_unicode=True, sort_keys=False)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# TOKEN: {new_code}\n") # 将口令也存在订阅文件里备注
        for p in valid_proxies:
            f.write(f"{p['name']}\n")

    print(f"✅ 更新完成。口令已同步至主页。")

if __name__ == "__main__":
    main()