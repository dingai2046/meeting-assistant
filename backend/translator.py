import anthropic
import os

class TranslatorService:
    def __init__(self):
        # 优先使用环境变量，否则用配置的 key
        api_key = os.getenv('ANTHROPIC_API_KEY', 'sk-MozRhnuiW6imbHoabpPAPYf9fKMgHOxwNIiTP5IVInNrC7jn')
        base_url = os.getenv('ANTHROPIC_BASE_URL', 'https://vipclaude.codes/')
        
        self.client = anthropic.Anthropic(
            api_key=api_key,
            base_url=base_url
        )
        self.model = "claude-haiku-4-5-20251001"
    
    def translate(self, text, target_lang='en'):
        if not text or not text.strip():
            return ""
        
        if target_lang == 'en':
            prompt = f"Translate to English only: {text}"
        else:
            prompt = f"只翻译成中文: {text}"
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text.strip()
        except Exception as e:
            return f"[错误: {str(e)}]"
    
    def detect_and_translate(self, text):
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in text)
        if has_chinese:
            return {
                "original": text,
                "translation": self.translate(text, 'en'),
                "direction": "zh→en"
            }
        else:
            return {
                "original": text,
                "translation": self.translate(text, 'zh'),
                "direction": "en→zh"
            }
