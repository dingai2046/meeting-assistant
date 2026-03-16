import json
from pathlib import Path

class GlossaryService:
    def __init__(self):
        self.glossary_path = Path("memory/glossary/terms.json")
        self.glossary_path.parent.mkdir(parents=True, exist_ok=True)
        self.load_glossary()
    
    def load_glossary(self):
        if self.glossary_path.exists():
            with open(self.glossary_path, 'r', encoding='utf-8') as f:
                self.terms = json.load(f)
        else:
            self.terms = {}
    
    def add_term(self, zh, en):
        self.terms[zh] = en
        self.save_glossary()
    
    def save_glossary(self):
        with open(self.glossary_path, 'w', encoding='utf-8') as f:
            json.dump(self.terms, f, ensure_ascii=False, indent=2)
    
    def get_translation(self, text):
        for zh, en in self.terms.items():
            if zh in text:
                text = text.replace(zh, f"{zh}({en})")
        return text
