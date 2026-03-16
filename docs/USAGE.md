# 使用指南

## 安装

```bash
cd ~/meeting-assistant
./deploy.sh
```

## 配置

1. 设置 Claude API Key:
```bash
export ANTHROPIC_API_KEY="your-api-key"
```

2. 修改团队配置:
编辑 `config/team.json`

## 使用

1. 启动服务:
```bash
./scripts/start-meeting.sh
```

2. 打开浏览器访问: http://localhost:3000

3. 点击"开始录音"开始会议

## 功能

- **实时翻译**: 自动中英互译
- **会议记录**: 保存在 memory/meetings/
- **任务管理**: 保存在 memory/tasks/
