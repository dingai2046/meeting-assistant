from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import os
from datetime import datetime
from pathlib import Path

from translator import TranslatorService
from summarizer import SummarizerService
from meeting_recorder import MeetingRecorder
from taskmaster import TaskMasterService

app = FastAPI(title="Meeting Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = TranslatorService()
summarizer = SummarizerService()
recorder = MeetingRecorder()
taskmaster = TaskMasterService()

# 存储会议记录
meeting_transcripts = {}

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/api/meeting/start")
async def start_meeting():
    meeting_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    meeting_transcripts[meeting_id] = []
    return {"status": "started", "meeting_id": meeting_id}

@app.post("/api/meeting/stop/{meeting_id}")
async def stop_meeting(meeting_id: str):
    transcripts = meeting_transcripts.get(meeting_id, [])
    if transcripts:
        recorder.save_meeting(meeting_id, transcripts)
    return {"status": "stopped", "count": len(transcripts)}

@app.post("/api/translate")
async def translate_text(payload: dict):
    text = payload.get("text", "")
    result = translator.detect_and_translate(text)
    return result

@app.post("/api/meeting/summarize/{meeting_id}")
async def summarize_meeting(meeting_id: str):
    transcripts = meeting_transcripts.get(meeting_id, [])
    summary = summarizer.summarize_meeting(transcripts)
    path = summarizer.save_summary(meeting_id, summary)
    
    # 同时提取任务
    tasks = taskmaster.extract_tasks(summary)
    if tasks.get('tasks'):
        taskmaster.save_tasks(meeting_id, tasks['tasks'])
    
    return {"status": "ok", "summary": summary, "tasks": tasks.get('tasks', []), "path": path}

@app.websocket("/ws/translation/{meeting_id}")
async def websocket_endpoint(websocket: WebSocket, meeting_id: str):
    await websocket.accept()
    if meeting_id not in meeting_transcripts:
        meeting_transcripts[meeting_id] = []
    try:
        while True:
            data = await websocket.receive_text()
            result = translator.detect_and_translate(data)
            meeting_transcripts[meeting_id].append(result)
            await websocket.send_json(result)
    except:
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7788))
    uvicorn.run(app, host="0.0.0.0", port=port)
