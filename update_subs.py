import requests
import base64

def main():
    # 读取你刚才创建的 sources.txt
    try:
        with open('sources.txt', 'r') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("错误：未找到 sources.txt")
        return

    all_content = []
    for url in urls:
        try:
            print(f"正在从源抓取: {url}")
            # 设置 Headers 模拟浏览器，防止被 GitHub 拦截
            res = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
            if res.status_code == 200:
                all_content.append(res.text)
        except Exception as e:
            print(f"抓取失败 {url}: {e}")

    # 合并内容并去重
    combined = "\n".join(all_content)
    # 过滤掉过短的行（无效节点）并去重
    lines = [line.strip() for line in combined.split('\n') if len(line.strip()) > 10]
    unique_lines = list(set(lines))

    # 将最终结果写入 sub_all.txt
    with open('sub_all.txt', 'w') as f:
        f.write("\n".join(unique_lines))
    print(f"成功！已汇总 {len(unique_lines)} 个节点。")

if __name__ == "__main__":
    main()