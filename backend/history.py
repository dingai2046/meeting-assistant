from pathlib import Path
import json

class MeetingHistory:
    def __init__(self):
        self.meetings_dir = Path("memory/meetings")
    
    def list_meetings(self):
        meetings = []
        for file in self.meetings_dir.glob("*.json"):
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                meetings.append({
                    "id": data['meeting_id'],
                    "timestamp": data['timestamp'],
                    "count": len(data['transcripts'])
                })
        return sorted(meetings, key=lambda x: x['timestamp'], reverse=True)
    
    def search_meetings(self, keyword):
        results = []
        for file in self.meetings_dir.glob("*.md"):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                if keyword in content:
                    results.append(str(file))
        return results
