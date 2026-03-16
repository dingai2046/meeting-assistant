#!/bin/bash

echo "🎯 启动会议助理..."

# 检查环境变量
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  请设置 ANTHROPIC_API_KEY 环境变量"
    exit 1
fi

# 启动后端
cd "$(dirname "$0")/.."
python3 backend/main.py
