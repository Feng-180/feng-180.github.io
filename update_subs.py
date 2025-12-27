import requests
import base64
import yaml
import time

# 你的源链接列表文件
SOURCE_FILE = 'sources.txt'
# 生成的最终订阅文件
OUTPUT_FILE = 'sub_all.txt'

def get_content(url):
    try:
        # 设置超时，防止某个源挂了导致整个 Action 失败
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"抓取失败 {url}: {e}")
    return ""

def main():
    with open(SOURCE_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    all_proxies = []
    
    # 基础的 Clash 配置头
    clash_config = {
        "port": 7890,
        "socks-port": 7891,
        "allow-lan": True,
        "mode": "rule",
        "log-level": "info",
        "external-controller": "127.0.0.1:9090",
        "proxies": []
    }

    for url in urls:
        content = get_content(url)
        if not content:
            continue
            
        # 逻辑：如果是 YAML 格式（通常包含 'proxies:'）
        if 'proxies:' in content:
            try:
                data = yaml.safe_load(content)
                if 'proxies' in data:
                    all_proxies.extend(data['proxies'])
            except:
                pass
        # 逻辑：如果是 Base64 格式（尝试通过转换器抓取节点）
        else:
            # 这里的 subUrl 需要指向一个在线转换后端来提取里面的纯节点列表
            # 为了简单起见，建议在这里直接存储原始链接，
            # 真正的“合并”交给网页端的一键导入代码（即我之前给你的双重编码逻辑）
            pass

    # 如果你希望脚本直接生成完整的 YAML
    if all_proxies:
        clash_config['proxies'] = all_proxies
        # 写入文件
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(clash_config, f, allow_unicode=True)
            print(f"成功更新 {len(all_proxies)} 个节点")
    else:
        # 如果脚本只负责汇总链接（保持你现在的逻辑），请确保网页端有转换器
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    main()