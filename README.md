# 风の魔法禁书录

赛博朋克风格的静态网站，集成时钟入口、联系站长、社群同步、节点订阅、科学上网指南于一体。

> 我曾经来过这个世界

## 功能特性

### 1. 时钟引导页 (`index.html`)
- 极简数字时钟显示
- 隐藏秘密入口（连点 5 次解锁）
- 粒子背景、呼吸光效、CRT 扫描线

### 2. 主控台 (`portal.html`)
- 打字机效果的状态显示
- 粒子网络背景动画
- 四大功能模块导航：
  - **联系站长** — 一键复制站长 QQ 并拉起聊天
  - **魔法阵地** — QQ 群组同步
  - **神秘节点** — 需口令验证的节点列表
  - **科学上网指南** — 从入门到上手的完整指南
- 音乐播放器、访客计数器

### 3. 科学上网指南 (`guide.html`)
- 紫色主题赛博风格
- 科学上网概念介绍与能力解锁展示
- 推荐客户端（Clash Verge / V2RayN / Shadowrocket / Surfboard / NekoBox）
- 三步快速上手流程
- 粒子背景、滚动入场动画

### 4. 节点列表页 (`nodes.html`)
- 全球节点订阅库展示
- 搜索过滤、统计栏、一键复制全部链接
- 支持 Clash 快速导入
- Matrix 代码雨背景效果
- 由 `update_subs.py` 自动生成

### 5. 404 错误页 (`404.html`)
- 赛博朋克故障风格
- 自动倒计时返回首页

### 6. 自动化更新系统 (GitHub Actions)
- 每天北京时间 06:00 和 18:00 自动运行 `update_subs.py`
- URL 健康检测，自动标记在线/离线状态
- 自动提交和推送更改

## 文件结构

```
feng-180.github.io/
├── index.html              # 时钟引导页
├── portal.html             # 主控台
├── guide.html              # 科学上网指南
├── nodes.html              # 节点列表（自动生成）
├── 404.html                # 错误页
├── update_subs.py          # 节点更新脚本
├── sources.txt             # 节点源配置（8 个精选源）
├── sub_all.txt             # 聚合订阅文件（自动生成）
├── bgm.mp3                 # 背景音乐
├── logo.png                # Logo / Favicon
├── CNAME                   # 自定义域名
├── .github/
│   └── workflows/
│       └── auto.yml        # GitHub Actions 自动化配置
└── README.md               # 本文件
```

## 快速开始

### 本地开发
```bash
git clone https://github.com/Feng-180/feng-180.github.io.git
cd feng-180.github.io
python3 -m http.server 8000
# 访问 http://localhost:8000
```

### 更新节点列表
```bash
# 编辑 sources.txt，格式：名称#链接
python3 update_subs.py
# 自动生成 nodes.html 和 sub_all.txt
```

## 自定义配置

### 修改访问密钥与联系方式
编辑 `portal.html` 中的 `CONFIG` 对象：
```javascript
const CONFIG = {
  ownerQQ: "2902939692",
  qqGroup: "691105381",
  accessKeyHash: "sha256(...)",  // 访问口令的 SHA-256 哈希值
  redirectUrl: "nodes.html"
};
```

生成新的哈希值：
```bash
node -e "const c=require('crypto');console.log(c.createHash('sha256').update('你的新密码').digest('hex'))"
```

### 添加节点源
编辑 `sources.txt`：
```
源名称#https://example.com/subscribe/link
```

## 使用流程

1. 访问时钟页面，连点 5 次进入主控台
2. 点击「联系站长」，复制站长 QQ 获取访问口令
3. 返回主控台，点击「神秘节点」，输入口令
4. 进入节点列表，复制订阅链接或导入 Clash
5. 点击「科学上网指南」查看客户端使用教程

## 设计说明

- **配色**：赛博朋克风格（青色 `#00f2ff` + 粉色 `#ff0055` + 紫色 `#a855f7`）
- **字体**：Noto Sans SC（Google Fonts）+ 等宽代码字体
- **语言**：全站简体中文（技术产品名保持英文原名）
- **安全**：访问口令使用 SHA-256 哈希存储，源码中无明文密码
- **动画**：粒子网络、故障特效、打字机效果、滚动入场
- **响应式**：完全适配移动设备

## GitHub Actions 自动化

- **定时**：每天 UTC 22:00 和 10:00（北京时间 06:00 和 18:00）
- **环境**：checkout@v4、setup-python@v5、Python 3.11
- **流程**：运行脚本 → 健康检测 → 生成页面 → 提交推送

## 更新日志

### v4.0 (2026-02)
- 全站文本统一为简体中文，移除所有英文标签
- 全站启用 Noto Sans SC 字体（Google Fonts）
- 新增「科学上网指南」页面（紫色主题）
- 主控台新增第四模块「科学上网指南」入口
- 升级订阅源为 8 个精选高质量源
- 访问口令改用 SHA-256 哈希验证
- QQ 群链接修复
- `update_subs.py` 模板同步中文化

### v3.0 (2025-02)
- 删除支付/教程页面，简化流程
- 新增「联系站长」卡片
- 升级 GitHub Actions 至最新版本
- 新增 404 错误页
- 全站 SEO 优化
- 节点页新增搜索、统计、一键复制

### v2.1
- 初始版本

## 许可证

MIT License

## 联系方式

- QQ：2902939692
- QQ 群：691105381

---

**Made with care by Feng-180**
