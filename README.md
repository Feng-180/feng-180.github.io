# 风の魔法禁书录 | TERMINAL V3.0

一个极具赛博朋克风格的静态网站，集成了时钟入口、联系站长、社群同步、节点订阅功能于一体。

> 我曾经来过这个世界 😎

## 🎨 功能特性

### 1. **时钟引导页** (`index.html`)
- 极简设计的数字时钟显示
- 隐藏的秘密入口（连点5次解锁）
- 粒子背景、呼吸光效、CRT 扫描线

### 2. **主控台** (`portal.html`) - v3.0
- 打字机效果的系统状态显示
- 粒子网络背景动画
- 三大功能模块导航：
  - 📞 **联系站长** - 一键复制站长 QQ 并拉起聊天
  - 💬 **魔法阵地** - QQ 群组同步
  - 🔐 **神秘节点** - 需密码验证的节点列表
- 音乐播放器控制
- 访客计数器

### 3. **节点列表页** (`nodes.html`)
- 全球节点订阅库展示
- 搜索过滤、统计栏、一键复制全部链接
- 支持 Clash 快速导入
- Matrix 代码雨背景效果
- 回到顶部按钮

### 4. **404 错误页** (`404.html`)
- 赛博朋克故障风格
- 自动倒计时返回首页

### 5. **自动化更新系统** (GitHub Actions)
- 每天北京时间 06:00 和 18:00 自动运行 `update_subs.py`
- URL 健康检测，自动标记 ACTIVE / OFFLINE
- 自动提交和推送更改

## 📁 文件结构

```
feng-180.github.io/
├── index.html              # 时钟引导页
├── portal.html             # 主控台 (v3.0)
├── nodes.html              # 节点列表（自动生成）
├── 404.html                # 错误页
├── update_subs.py          # 节点更新脚本 (v3.0)
├── sources.txt             # 节点源配置
├── sub_all.txt             # 聚合订阅文件
├── bgm.mp3                 # 背景音乐
├── logo.png                # Logo / Favicon
├── CNAME                   # 自定义域名
├── .github/
│   └── workflows/
│       └── auto.yml        # GitHub Actions 自动化配置
└── README.md               # 本文件
```

## 🚀 快速开始

### 本地开发
```bash
# 克隆仓库
git clone https://github.com/Feng-180/feng-180.github.io.git
cd feng-180.github.io

# 使用 Python 简单服务器预览
python3 -m http.server 8000

# 访问 http://localhost:8000
```

### 更新节点列表
```bash
# 编辑 sources.txt，添加或修改节点源
# 格式：名称#链接 或 名称,链接

# 运行更新脚本
python3 update_subs.py

# 脚本会自动生成 nodes.html 和 sub_all.txt
```

## 🔧 自定义配置

### 修改访问密钥与联系方式
编辑 `portal.html`，找到配置部分：
```javascript
const CONFIG = {
  ownerQQ: "2902939692",       // 站长 QQ
  qqGroup: "691105381",        // QQ 群号
  accessKeyHash: "sha256(...)",// 节点列表访问密钥（SHA-256 哈希值）
  redirectUrl: "nodes.html"
};
```

如需修改密码，用以下命令生成新哈希值：
```bash
node -e "const c=require('crypto');console.log(c.createHash('sha256').update('你的新密码').digest('hex'))"
```

### 添加新的节点源
编辑 `sources.txt`：
```
FreeFQ_高频更新#https://raw.githubusercontent.com/freefq/free/master/v2
Pawdroid_修正源#https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub
你的源名称#你的源链接
```

### 自定义打字机文本
编辑 `portal.html`，找到 `phrases` 数组：
```javascript
const phrases = ["SYSTEM STATUS: ONLINE", "SCANNING NETWORK...", "DETECTING MAGIC...", "WELCOME TRAVELER"];
```

## 🎯 使用流程

1. 访问时钟页面，连点 5 次进入主控台
2. 点击 **联系站长**，自动复制站长 QQ 并拉起 QQ
3. 私聊站长获取 ACCESS KEY（访问口令）
4. 返回主控台，点击 **神秘节点**，输入口令
5. 进入节点列表，复制订阅链接或导入 Clash

## 🔐 安全性说明

- 本项目为**纯前端静态网站**，无后端服务器
- 不存储任何用户信息
- 节点列表受密码保护

## 📊 GitHub Actions 自动化

### 工作流触发条件
- **定时触发**：每天 UTC 22:00 和 10:00（北京时间 06:00 和 18:00）
- **手动触发**：在 GitHub Actions 页面手动运行

### 工作流步骤
1. 检出仓库代码（checkout@v4）
2. 设置 Python 3.11 环境（setup-python@v5）
3. 运行 `update_subs.py` 更新节点（含 URL 健康检测）
4. 配置 Git 用户信息
5. 提交并推送更改

## 🎨 设计风格

- **配色**：赛博朋克风格（青色 #00f2ff + 粉色 #ff0055）
- **字体**：等宽代码字体 + 系统字体混搭
- **动画**：粒子网络、故障特效、打字机效果
- **响应式**：完全适配移动设备

## 📱 浏览器兼容性

- Chrome / Edge / Firefox（最新版本）
- Safari（iOS 13+）
- 移动浏览器（iOS Safari、Chrome Mobile）

## 🛠️ 常见问题

### Q: 如何修改节点更新频率？
A: 编辑 `.github/workflows/auto.yml`，修改 `cron` 表达式。

### Q: 节点列表为什么没有更新？
A: 检查以下几点：
1. GitHub Actions 是否启用
2. `sources.txt` 中的链接是否有效
3. 查看 Actions 日志了解错误详情

## 📝 更新日志

### v3.0 (2025-02)
- 删除支付/教程页面，简化使用流程
- 新增「联系站长」卡片，一键复制 QQ 并拉起聊天
- 主控台精简为 3 模块（联系站长 / 魔法阵地 / 神秘节点）
- 升级 GitHub Actions (checkout@v4, setup-python@v5, Python 3.11)
- `update_subs.py` v3.0：URL 健康检测、ACTIVE/OFFLINE 标记
- 新增 404 错误页（赛博朋克故障风格）
- 全站 SEO 优化（meta 标签、Open Graph、Favicon）
- 节点页新增搜索、统计栏、一键复制全部、回到顶部

### v2.1
- 初始版本

## 📄 许可证

MIT License

## 📧 联系方式

- QQ: 2902939692
- QQ 群: 691105381

---

**Made with ❤️ by Feng-180**
