# Railway 部署指南

## 准备工作

1. 注册 Railway 账号：https://railway.app
2. 安装 Git（如果还没有）
3. 创建 GitHub 仓库

## 部署步骤

### 1. 初始化 Git 仓库

```bash
cd ~/meeting-assistant
git init
git add .
git commit -m "Initial commit"
```

### 2. 推送到 GitHub

```bash
# 在 GitHub 创建新仓库后
git remote add origin https://github.com/你的用户名/meeting-assistant.git
git branch -M main
git push -u origin main
```

### 3. 在 Railway 部署

1. 登录 Railway.app
2. 点击 "New Project"
3. 选择 "Deploy from GitHub repo"
4. 选择你的 meeting-assistant 仓库
5. Railway 会自动检测并部署

### 4. 配置环境变量（可选）

在 Railway 项目设置中添加：
- `ANTHROPIC_API_KEY`: 你的 API key（已内置默认值）
- `ANTHROPIC_BASE_URL`: API 地址（已内置默认值）

### 5. 获取部署地址

部署完成后，Railway 会给你一个 URL，类似：
`https://meeting-assistant-production.up.railway.app`

## 本地测试

```bash
cd ~/meeting-assistant
source venv/bin/activate
python backend/main.py
```

访问：http://localhost:7788

## 注意事项

- Railway 免费额度：每月 $5
- 超出后会暂停服务
- 可以升级到付费计划
