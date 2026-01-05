import requests
import base64
import yaml
import time
import re
from concurrent.futures import ThreadPoolExecutor

# --- 配置区 ---
SOURCE_FILE = 'sources.txt'
OUTPUT_FILE = 'sub_all.txt'  # 原始通用订阅
CLASH_FILE = 'clash.yaml'     # 专门的 Clash 配置文件
CONVERTER_API = "https://sub.id9.cc/sub?target=clash&url=" # 转换后端

# ✨ [PINK_STYLE] 测速超时设置 (秒)
TIMEOUT = 5 
# ✨ [PINK_STYLE] 并发检测线程数
MAX_WORKERS = 20 

def get_content(url):
    """ ✨ [PINK_STYLE] 执行核心抓取术式 """
    try:
        headers = {'User-Agent': 'ClashforWindows/0.19.23'}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"❌ 抓取失败 {url}: {e}")
    return ""

def check_node(proxy):
    """ ✨ [PINK_STYLE] 节点生命力检测 (满分筛选逻辑) """
    try:
        # 提取节点服务器和端口
        server = proxy.get('server')
        port = proxy.get('port')
        if not server or not port:
            return None
        
        # 简单的 TCP 联通性测试
        import socket
        start_time = time.time()
        s = socket.create_connection((server, int(port)), timeout=TIMEOUT)
        delay = int((time.time() - start_time) * 1000)
        s.close()
        
        # 将延迟信息注入节点名 (实现“满分”标记)
        proxy['name'] = f"⚡{delay}ms | {proxy.get('name', 'Magic-Node')}"
        return proxy
    except:
        return None

def main():
    print("🔮 正在启动魔法术式：节点自动筛选与更新...")
    
    with open(SOURCE_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    all_proxies = []

    # 1. 遍历并转换源
    for url in urls:
        print(f"📡 正在解析源: {url[:30]}...")
        # 优先通过转换后端获取标准化的 YAML 格式节点
        convert_url = f"{CONVERTER_API}{requests.utils.quote(url)}&insert=false"
        content = get_content(convert_url)
        
        if 'proxies:' in content:
            try:
                data = yaml.safe_load(content)
                if 'proxies' in data:
                    all_proxies.extend(data['proxies'])
            except:
                continue

    # 2. 节点去重 (按服务器地址)
    unique_proxies = {p['server']+str(p['port']): p for p in all_proxies}.values()
    print(f"🔍 初始发现 {len(unique_proxies)} 个潜在节点，准备进行可用性筛选...")

    # 3. 多线程测速筛选 (剔除不可用)
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = executor.map(check_node, unique_proxies)
        for res in results:
            if res:
                valid_proxies.append(res)

    # 4. 排序：按延迟从小到大排列 (实现优质节点优先)
    # 逻辑：提取我们刚刚注入的名字中的延迟数字
    valid_proxies.sort(key=lambda x: int(re.search(r'\d+', x['name']).group()) if re.search(r'\d+', x['name']) else 999)

    # 5. 生成结果
    # 写入 Clash 专用文件
    clash_config = {
        "proxies": valid_proxies,
        "proxy-groups": [
            {
                "name": "🚀 魔法枢纽",
                "type": "select",
                "proxies": [p['name'] for p in valid_proxies]
            }
        ],
        "rules": ["MATCH,🚀 魔法枢纽"]
    }

    with open(CLASH_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(clash_config, f, allow_unicode=True, sort_keys=False)

    # 写入通用订阅文件 (Base64 格式，方便小火箭)
    # 这里我们采取简单策略：将有效的节点信息存入，或保持原始汇总
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # 为了兼容，我们把所有原始链接重新打包（示例逻辑）
        f.write("# UPDATED BY MAGIC_SYSTEM\n")
        # 如果需要生成 Base64，可以在此进行转换，这里先保持文本方便你手动修改
        for p in valid_proxies:
            f.write(f"{p['name']} -> {p['server']}:{p['port']}\n")

    print(f"✅ 术式同步完成！共存留 {len(valid_proxies)} 个满分节点。")

if __name__ == "__main__":
    main()