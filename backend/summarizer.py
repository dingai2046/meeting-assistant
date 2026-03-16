import anthropic
import os
from pathlib import Path
from datetime import datetime

class SummarizerService:
    def __init__(self):
        api_key = os.getenv('ANTHROPIC_API_KEY', 'sk-MozRhnuiW6imbHoabpPAPYf9fKMgHOxwNIiTP5IVInNrC7jn')
        base_url = os.getenv('ANTHROPIC_BASE_URL', 'https://vipclaude.codes/')
        
        self.client = anthropic.Anthropic(api_key=api_key, base_url=base_url)
        self.model = "claude-haiku-4-5-20251001"
    
    def summarize_meeting(self, transcripts):
        if not transcripts:
            return "无会议记录"
        
        content = "会议对话：\n\n"
        for t in transcripts:
            content += f"{t.get('original', '')} → {t.get('translation', '')}\n"
        
        prompt = f"""{content}

请生成会议纪要，包含：
## 会议主题
## 关键讨论点
## 决策事项
## 行动项
## 未解决问题"""
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text.strip()
        except Exception as e:
            return f"总结失败: {str(e)}"
    
    def save_summary(self, meeting_id, summary):
        path = Path(f"memory/meetings/{meeting_id}_summary.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# 会议总结 - {meeting_id}\n\n{summary}")
        return str(path)
