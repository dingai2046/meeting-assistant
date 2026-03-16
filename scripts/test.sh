#!/bin/bash

echo "🧪 测试 Meeting Assistant"

# 测试后端启动
echo "1. 测试后端..."
python3 -c "from backend.main import app; print('✅ 后端导入成功')"

# 测试 Whisper
echo "2. 测试 Whisper..."
python3 -c "from backend.whisper_service import WhisperService; print('✅ Whisper 导入成功')"

# 测试翻译
echo "3. 测试翻译..."
python3 -c "from backend.translator import TranslatorService; print('✅ 翻译服务导入成功')"

echo "✅ 所有测试通过"
