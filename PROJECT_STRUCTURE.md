# Meeting Assistant - 项目结构

## 项目概述
悉尼企业老板定制的企业会议翻译+总结+团队分工执行安排的私人助理

基于 OpenClaw 框架，支持中英双语实时翻译、自动会议总结、智能任务分配

## 目录结构

```
meeting-assistant/
├── README.md                 # 项目说明
├── deploy.sh                 # 一键部署脚本
├── requirements.txt          # Python 依赖
├── config/
│   ├── models.json          # AI 模型配置
│   └── team.json            # 团队成员配置
├── agents/
│   ├── translator/          # 翻译 Agent
│   ├── summarizer/          # 总结 Agent
│   └── taskmaster/          # 任务分配 Agent
├── backend/
│   ├── main.py              # FastAPI 主程序
│   ├── whisper_service.py   # 语音识别服务
│   ├── translator.py        # 翻译服务
│   └── websocket.py         # WebSocket 处理
├── frontend/
│   ├── index.html           # 主界面
│   └── assets/
│       └── styles.css       # 样式文件
├── memory/
│   ├── meetings/            # 会议记录
│   ├── tasks/               # 任务数据
│   └── glossary/            # 术语库
├── scripts/
│   └── start-meeting.sh     # 启动会议脚本
└── docs/
    ├── TECH_SPEC.md         # 技术规格
    └── DEV_PLAN.md          # 开发计划
```

## 核心文件说明

### 配置文件
- `SOUL.md`: 助理人格定义
- `USER.md`: 老板信息
- `MEETING.md`: 会议配置
- `TEAM.md`: 团队成员信息

### 后端服务
- `backend/main.py`: FastAPI 服务器，提供 API 和 WebSocket
- `backend/whisper_service.py`: 语音识别（Whisper）
- `backend/translator.py`: 翻译服务（Claude API）

### 前端界面
- `frontend/index.html`: 单页应用，显示实时翻译

### 数据存储
- `memory/meetings/`: 会议记录（.md + .json）
- `memory/tasks/`: 任务数据
- `memory/glossary/`: 术语库

## 技术栈
- 语音识别: OpenAI Whisper (本地)
- 翻译: Claude API (Haiku)
- 后端: Python FastAPI
- 前端: HTML + Tailwind CSS + Alpine.js
- 实时通信: WebSocket
