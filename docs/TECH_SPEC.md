# 技术规格文档

## Phase 1 MVP - 核心功能

### 1. 语音识别模块
**技术**: OpenAI Whisper (本地部署)
**输入**: 音频流 (WAV/MP3)
**输出**: 文本转录 (中文/英文)
**性能**: ~1秒延迟

### 2. 翻译模块
**技术**: Claude API (Haiku)
**输入**: 源语言文本
**输出**: 目标语言文本
**支持**: 中↔英双向翻译

### 3. Web UI
**技术**: HTML + Tailwind + Alpine.js
**功能**:
- 开始/停止录音按钮
- 实时显示翻译字幕
- 会议记录查看

### 4. 后端 API
**技术**: FastAPI + WebSocket
**端点**:
- POST /api/meeting/start - 开始会议
- POST /api/meeting/stop - 结束会议
- WS /ws/translation - 实时翻译流

## 依赖安装

```bash
# Python 依赖
pip install openai-whisper fastapi uvicorn anthropic websockets

# 系统依赖 (macOS)
brew install ffmpeg portaudio
```

## 配置文件

### config/models.json
```json
{
  "whisper": {
    "model": "base",
    "language": "auto"
  },
  "claude": {
    "model": "claude-haiku-3-5",
    "max_tokens": 1000
  }
}
```

## 数据流

1. 用户说话 → 麦克风录音
2. 音频 → Whisper → 文本
3. 文本 → Claude → 翻译
4. 翻译 → WebSocket → 前端显示
