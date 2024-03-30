from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()
import os

llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.1, google_api_key = os.getenv('API_KEY'))

