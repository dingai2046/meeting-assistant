# Meeting Assistant - 企业会议助理

悉尼企业老板定制的企业会议翻译+总结+团队分工执行安排的私人助理

## 功能特性

✅ **实时翻译** - 中英双语实时翻译
✅ **会议总结** - 自动生成会议纪要
✅ **任务分配** - 智能分配团队任务
✅ **本地部署** - 保护商业机密

## 快速开始

```bash
# 一键部署
./deploy.sh

# 手动启动
python3 backend/main.py
```

访问 http://localhost:3000

## 技术栈

- 语音识别: OpenAI Whisper
- 翻译: Claude API
- 后端: Python FastAPI
- 前端: HTML + Tailwind + Alpine.js

## 项目状态

当前版本: Phase 1 MVP
- [x] 基础框架
- [ ] Whisper 集成
- [ ] Claude 翻译
- [ ] 完整测试
