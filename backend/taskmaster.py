import anthropic
import os
import json
from pathlib import Path
from datetime import datetime

class TaskMasterService:
    def __init__(self):
        api_key = os.getenv('ANTHROPIC_API_KEY', 'sk-MozRhnuiW6imbHoabpPAPYf9fKMgHOxwNIiTP5IVInNrC7jn')
        base_url = os.getenv('ANTHROPIC_BASE_URL', 'https://vipclaude.codes/')
        
        self.client = anthropic.Anthropic(api_key=api_key, base_url=base_url)
        self.model = "claude-haiku-4-5-20251001"
        
        with open('config/team.json') as f:
            self.team = json.load(f)['team_members']
    
    def extract_tasks(self, summary):
        prompt = f"""从会议纪要提取任务，输出JSON：

{summary}

格式：
{{"tasks": [{{"title": "任务", "assignee": "负责人", "priority": "high/medium/low", "deadline": "日期"}}]}}"""
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            text = message.content[0].text.strip()
            start = text.find('{')
            end = text.rfind('}') + 1
            if start >= 0 and end > start:
                return json.loads(text[start:end])
            return {"tasks": []}
        except:
            return {"tasks": []}
    
    def save_tasks(self, meeting_id, tasks):
        path = Path(f"memory/tasks/{meeting_id}_tasks.json")
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({"meeting_id": meeting_id, "tasks": tasks}, f, ensure_ascii=False, indent=2)
        return str(path)
