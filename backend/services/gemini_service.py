import google.generativeai as genai
from ..core.config import get_settings
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

settings = get_settings()

class GeminiService:
    def __init__(self):
        try:
            if not settings.GOOGLE_API_KEY or "your_gemini_api_key_here" in settings.GOOGLE_API_KEY:
                print("CRITICAL WARNING: GOOGLE_API_KEY is not set or is using the default placeholder in .env")
            
            genai.configure(api_key=settings.GOOGLE_API_KEY)
            self.model = genai.GenerativeModel('gemini-flash-latest')
        except Exception as e:
            print(f"Error configuring Gemini: {e}")
            self.model = None

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=20), retry=retry_if_exception_type(Exception))
    def generate_content(self, prompt: str):
        if not self.model:
            return "Gemini model not initialized. Check API Key."
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                print(f"Rate limit hit. Retrying... Error: {e}")
                raise e # Re-raise to trigger retry
            return f"Error generating content: {e}"

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=2, max=20), retry=retry_if_exception_type(Exception))
    def get_embedding(self, text: str):
        if not self.model:
            return []
        try:
            result = genai.embed_content(
                model="models/gemini-embedding-001",
                content=text,
                task_type="retrieval_document",
                title="Embedding of single string"
            )
            return result['embedding']
        except Exception as e:
            print(f"Error getting embedding: {e}")
            if "API_KEY_INVALID" in str(e) or "400" in str(e):
                print("SUGGESTION: Please check that your GOOGLE_API_KEY in .env is valid.")
            if "429" in str(e):
                print(f"Rate limit hit. Retrying... Error: {e}")
                raise e # Re-raise to trigger retry
            return []
