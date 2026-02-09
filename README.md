# 风の魔法禁书录 | TERMINAL V2.1

一个极具赛博朋克风格的静态网站，集成了时钟、节点订阅、支付功能于一体。

> 我曾经来过这个世界 😎

## 🎨 功能特性

### 1. **时钟引导页** (`index.html`)
- 极简设计的数字时钟显示
- 隐藏的秘密入口（连点5次解锁）
- 赛博朋克风格的视觉特效

### 2. **主控台** (`portal.html`) - v2.1
- 打字机效果的系统状态显示
- 粒子网络背景动画
- 四大功能模块导航：
  - 📖 **使用教程** - 支付和使用指南
  - 💬 **魔法阵地** - QQ 群组同步
  - 🔐 **神秘节点** - 需密码验证的节点列表
  - 💳 **赞助支持** - 微信/支付宝支付入口（新增）
- 音乐播放器控制
- 访客计数器

### 3. **支付教程页** (`tutorial.html`) - v3.1 升级版
- **多支付方式切换**：微信支付 & 支付宝
- **交互式二维码展示**：
  - 点击放大全屏预览
  - 长按保存或截图
  - 支持 ESC 快捷键关闭
- **自动复制联系方式**：支付后一键复制 QQ
- **设备自适应**：手机端拉起 QQ，PC 端提示跳转
- 赛博朋克风格的支付界面

### 4. **节点列表页** (`nodes.html`)
- 全球节点订阅库展示
- 支持一键复制链接
- 支持 Clash 快速导入
- Matrix 代码雨背景效果

### 5. **自动化更新系统** (GitHub Actions)
- 每天自动运行 `update_subs.py` 脚本
- 自动更新节点列表
- 自动提交和推送更改
- 无需手动干预

## 📁 文件结构

```
feng-180.github.io/
├── index.html              # 时钟引导页
├── portal.html             # 主控台 (v2.1)
├── tutorial.html           # 支付教程 (v3.1)
├── nodes.html              # 节点列表
├── update_subs.py          # 节点更新脚本
├── sources.txt             # 节点源配置
├── sub_all.txt             # 聚合订阅文件
├── bgm.mp3                 # 背景音乐
├── skm.jpg                 # 收款二维码
├── logo.png                # Logo
├── .github/
│   └── workflows/
│       └── update-nodes.yml # GitHub Actions 自动化配置
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

### 配置支付功能
编辑 `tutorial.html`，修改以下配置：
```javascript
// 第 ~290 行
const CONFIG = { qq: "你的QQ号" };
```

如需使用不同的收款码图片：
1. 将微信收款码保存为 `skm.jpg`（或修改 HTML 中的图片路径）
2. 支付宝收款码可在 `tutorial.html` 中添加新的 `<img>` 标签

## 🔧 自定义配置

### 修改访问密钥
编辑 `portal.html`，找到配置部分：
```javascript
const CONFIG = {
  qqGroup: "691105381",      // QQ 群号
  accessKey: "资源风888",     // 节点列表访问密钥
  redirectUrl: "nodes.html"
};
```

### 添加新的节点源
编辑 `sources.txt`：
```
FreeFQ_高频更新#https://raw.githubusercontent.com/freefq/free/master/v2
Pawdroid_修正源#https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub
你的源名称#你的源链接
```

### 自定义打字机文本
编辑 `portal.html` 或 `tutorial.html`，找到 `phrases` 数组：
```javascript
const phrases = ["SYSTEM STATUS: ONLINE", "SCANNING NETWORK...", "DETECTING MAGIC...", "WELCOME TRAVELER"];
```

## 🎯 支付流程

1. 用户访问 **使用教程** 或 **赞助支持**
2. 选择支付方式（微信/支付宝）
3. 点击二维码查看大图
4. 扫码支付
5. 点击"已支付 → 唤醒站长"
6. 系统自动复制 QQ 号
7. 手机端拉起 QQ，PC 端提示添加

## 🔐 安全性说明

- 本项目为**纯前端静态网站**，无后端服务器
- 所有支付操作均由用户手动完成
- 不存储任何用户信息或支付数据
- 收款码为本地图片，不涉及第三方支付 API

## 📊 GitHub Actions 自动化

### 工作流触发条件
- **定时触发**：每天 UTC 0:00（北京时间 08:00）
- **手动触发**：在 GitHub Actions 页面手动运行

### 工作流步骤
1. 检出仓库代码
2. 设置 Python 环境
3. 运行 `update_subs.py` 更新节点
4. 配置 Git 用户信息
5. 提交并推送更改

### 查看自动化日志
访问 GitHub 仓库 → Actions 标签 → 查看最新的 "Auto Update Nodes" 工作流

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

### Q: 支付宝收款码如何添加？
A: 在 `tutorial.html` 中找到支付方式切换逻辑，添加新的收款码图片路径即可。

### Q: 如何修改节点更新频率？
A: 编辑 `.github/workflows/update-nodes.yml`，修改 `cron` 表达式：
```yaml
- cron: '0 0 * * *'  # 每天 UTC 0:00
- cron: '0 */6 * * *' # 每 6 小时
- cron: '0 0 * * 0'   # 每周日 UTC 0:00
```

### Q: 节点列表为什么没有更新？
A: 检查以下几点：
1. GitHub Actions 是否启用
2. `sources.txt` 中的链接是否有效
3. 查看 Actions 日志了解错误详情

### Q: 如何自定义支付方式标签？
A: 编辑 `tutorial.html` 中的支付标签 HTML：
```html
<div class="pay-tab wechat active" onclick="switchPayMethod('wechat')">
  💚 微信支付
</div>
```

## 📝 更新日志

### v2.1 (Portal)
- 添加赞助支持导航卡片
- 优化视觉效果和动画

### v3.1 (Tutorial)
- 支持微信和支付宝支付方式切换
- 添加全屏二维码预览功能
- 改进移动端交互体验
- 支持 ESC 快捷键关闭预览

### v1.0 (GitHub Actions)
- 配置自动化节点更新工作流
- 每天自动同步节点列表

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

- QQ: 2902939692
- QQ 群: 691105381

---

**Made with ❤️ by Feng-180**

*"Stay hungry. Stay foolish."*
