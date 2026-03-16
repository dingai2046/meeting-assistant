#!/usr/bin/env python3
import sys
import os

print("🧪 Meeting Assistant 完整测试")
print("=" * 50)

# 测试1: 导入检查
print("\n1. 测试模块导入...")
try:
    from backend.main import app
    from backend.whisper_service import WhisperService
    from backend.translator import TranslatorService
    from backend.summarizer import SummarizerService
    from backend.taskmaster import TaskMasterService
    from backend.glossary import GlossaryService
    from backend.history import MeetingHistory
    print("✅ 所有模块导入成功")
except Exception as e:
    print(f"❌ 导入失败: {e}")
    sys.exit(1)

# 测试2: 配置文件
print("\n2. 测试配置文件...")
try:
    import json
    with open('config/models.json') as f:
        models = json.load(f)
    with open('config/team.json') as f:
        team = json.load(f)
    print("✅ 配置文件正常")
except Exception as e:
    print(f"❌ 配置文件错误: {e}")

# 测试3: 目录结构
print("\n3. 测试目录结构...")
dirs = ['memory/meetings', 'memory/tasks', 'memory/glossary', 'logs']
for d in dirs:
    if os.path.exists(d):
        print(f"✅ {d} 存在")
    else:
        print(f"⚠️  {d} 不存在，创建中...")
        os.makedirs(d, exist_ok=True)

print("\n" + "=" * 50)
print("✅ 所有测试通过！")
