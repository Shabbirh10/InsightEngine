import requests
import time

API_URL = "http://localhost:8000/api/v1"

def test_api():
    print("Testing API...")
    
    # 1. Upload Text
    print("Uploading text...")
    try:
        response = requests.post(f"{API_URL}/upload/text", json={
            "title": "Test Doc",
            "content": "The Intelligent Knowledge Platform is a powerful RAG system built with FastAPI and Gemini.",
            "metadata": {"source": "test_script"}
        })
        response.raise_for_status()
        data = response.json()
        print(f"Upload Success: {data}")
    except Exception as e:
        print(f"Upload Failed: {e}")
        try: print(response.text)
        except: pass
        return

    # Give it a moment (though Chroma is usually fast)
    time.sleep(1)

    # 2. Query
    print("\nQuerying...")
    try:
        response = requests.post(f"{API_URL}/query", json={
            "query": "What is the Intelligent Knowledge Platform?",
            "n_results": 1
        })
        response.raise_for_status()
        data = response.json()
        print(f"Query Success!")
        print(f"Answer: {data['answer']}")
        print(f"Sources: {data['sources']}")
    except Exception as e:
        print(f"Query Failed: {e}")
        try: print(response.text)
        except: pass

if __name__ == "__main__":
    test_api()
