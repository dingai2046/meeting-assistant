import json
from datetime import datetime
from pathlib import Path

class MeetingRecorder:
    def __init__(self):
        self.meetings_dir = Path("memory/meetings")
        self.meetings_dir.mkdir(parents=True, exist_ok=True)
    
    def save_meeting(self, meeting_id, transcripts):
        # 保存 Markdown 格式
        md_path = self.meetings_dir / f"{meeting_id}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# 会议记录 - {meeting_id}\n\n")
            f.write(f"**时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## 对话记录\n\n")
            for t in transcripts:
                f.write(f"**原文**: {t['original']}\n")
                f.write(f"**翻译**: {t['translation']}\n\n")
        
        # 保存 JSON 格式
        json_path = self.meetings_dir / f"{meeting_id}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                "meeting_id": meeting_id,
                "timestamp": datetime.now().isoformat(),
                "transcripts": transcripts
            }, f, ensure_ascii=False, indent=2)
        
        return str(md_path)
