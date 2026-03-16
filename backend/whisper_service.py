import whisper
import json

class WhisperService:
    def __init__(self):
        with open('config/models.json') as f:
            config = json.load(f)
        model_name = config['whisper']['model']
        self.model = whisper.load_model(model_name)
    
    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result['text']
