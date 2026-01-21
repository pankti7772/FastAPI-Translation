from transformers import MarianMTModel, MarianTokenizer

# Model name for English to French
MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"

class TranslationModel:
    def __init__(self):
        print(f"Loading model: {MODEL_NAME}...")
        self.tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        self.model = MarianMTModel.from_pretrained(MODEL_NAME)
        print("Model loaded successfully.")

    def translate(self, text: str) -> str:
        # Tokenize the text
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        
        # Generate translation
        translated = self.model.generate(**inputs)
        
        # Decode the translation
        translated_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
        return translated_text

# Global instance
translation_model = TranslationModel()
