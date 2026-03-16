#!/bin/bash

echo "🚀 Meeting Assistant 一键部署"
echo "================================"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未安装"
    exit 1
fi

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 检查 ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "📦 安装 ffmpeg..."
    brew install ffmpeg
fi

# 安装 Python 依赖
echo "📦 安装 Python 依赖..."
pip install -r requirements.txt

# 创建必要目录
mkdir -p memory/meetings memory/tasks memory/glossary logs

# 启动服务
echo "🎯 启动服务..."
python backend/main.py &

# 等待服务启动
sleep 3

# 打开浏览器
echo "🌐 打开浏览器..."
open http://localhost:3000

echo "✅ 部署完成！"
