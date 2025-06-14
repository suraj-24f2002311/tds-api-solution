# 📘 TDS Virtual TA - Tools in Data Science Project (Jan 2025)

This is a Virtual Teaching Assistant API project for the **Tools in Data Science** course from **IIT Madras Online BSc** (Jan 2025 term). It answers student questions using pre-scraped content from course Discourse posts and content, as per project instructions.

---

## 🔗 API Endpoint

actual one 
http://127.0.0.1:8000


### Method: `POST`

### Request format (JSON):

json
{
  "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
  "image": "base64-encoded image string "
}

# curl command 
curl "http://127.0.0.1:8000" \
  -H "Content-Type: application/json" \
  -d "{\"question\": \"Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?\", \"image\": \"$(base64 -w0 project-tds-virtual-ta-q1.webp)\"}"



# response 
{
  "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
      "text": "Use the model that’s mentioned in the question."
    },
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
      "text": "My understanding is that you just have to use a tokenizer, similar to what Prof. Anand used, to get the number of tokens and multiply that by the given rate."
    }
  ]
}


# Setup 
pip install -r requirements.txt

# to run locally
uvicorn main:app --host 0.0.0.0 --port 8000 --reload



# bonus 
MIT LICENCE for public use 
